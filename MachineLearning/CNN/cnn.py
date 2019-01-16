# coding:UTF-8
# 2018-11-12 ~ 11-16
# CNN 
# 卷积网络知识 https://blog.csdn.net/luanpeng825485697/article/details/79009241
# 代码：  https://blog.csdn.net/luanpeng825485697/article/details/79088938
# 吴恩达卷积参数符号表示：https://blog.csdn.net/ice_actor/article/details/78648780
# 公式+代码： https://www.zybuluo.com/hanbingtao/note/485480

import numpy as np 
import math
import Activators


class Filter(object):
    """
    构造过滤器
    """
    def __init__(self, width, height, depth, filter_num):
        """
        参数：过滤器宽度，过滤器高度，过滤器深度，过滤器数目
        """
        w_min = - math.sqrt(6 / (width * height * depth + width * height * filter_num))
        w_max = - w_min
        self.weights = np.random.uniform(w_min, w_max, (depth, height, width))
        # self.weights = np.random.uniform(-1e-2, 1e-2, (depth, height, width))

        self.bias = 0
        self.weights_grad = np.zeros(self.weights.shape)
        self.bias_grad = 0


    def __repr__(self):
        return 'filter weights:\n%s\nbias:\n%s' % (repr(self.weights), repr(self.bias))


    def getWeights(self):
        return self.weights


    def getBias(self):
        return self.bias


    def update(self, learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias


def getConvArea(input_array, i, j, filter_width, filter_height, stride):
    """
    获取卷积区域
    """
    start_i = i * stride
    start_j = j * stride
    if input_array.ndim == 2:
        return input_array[start_i : start_i + filter_height, start_j : start_j + filter_width]
    elif input_array.ndim == 3:
        return input_array[:, start_i : start_i + filter_height, start_j : start_j + filter_width]


def conv(input_array, kernel_array, output_array, stride, bias):
    """
    卷积计算
    参数：输入(图片数据)，卷积核，输出，步长，偏置
    """
    output_height, output_width = np.shape(output_array)
    # kernel_array可能有多个通道
    kernel_height = np.shape(kernel_array)[-2]
    kernel_width = np.shape(kernel_array)[-1]

    for i in range(output_height):
        for j in range(output_width):
            conv_area = getConvArea(input_array, i, j, kernel_width, kernel_height, stride)
            kernel_values = np.sum(np.multiply(conv_area, kernel_array))
            output_array[i][j] = kernel_values + bias


def getMaxIndex(array):
    """
    获得二位数组最大值的索引
    """
    location = np.where(array == np.max(array))
    return location[0], location[1]


class ConvLayer(object):
    """
    实现一个卷积层，构造函数中设置卷积层的超参数(手动设置)
    """
    def __init__(self, input_width, input_height, channel_number, filter_width, filter_height, filter_number, zero_padding, stride, activator, learning_rate):
        """
        参数分别为：卷积宽度，高度，通道数，滤波器宽度，滤波器高度，滤波器数目，补零数目，步长，激活器，学习速率
        """
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.filter_number = filter_number
        self.zero_padding = zero_padding
        self.stride = stride

        # 使用公式(3)计算feature map 尺寸
        self.output_width = int(ConvLayer.calOutputSize(self.input_width, filter_width, zero_padding, stride))
        self.output_height = int(ConvLayer.calOutputSize(self.input_height, filter_height, zero_padding, stride))
        # 构建 feature map, 三维数组，每个过滤器都产生一个二维数组
        self.output_array = np.zeros((self.filter_number, self.output_height, self.output_width))

        self.filters = [] # 卷积层的每个过滤器
        for i in range(filter_number):
            self.filters.append(Filter(filter_width, filter_height, self.channel_number, filter_number))

        self.activator = activator
        self.learning_rate = learning_rate


    def forward(self, input_array):
        """
        向前传递，结果保存在self.output_array里
        """
        self.input_array = input_array
        self.padded_input_array = ConvLayer.padding(input_array, self.zero_padding)
        for i in range(self.filter_number):
            filters = self.filters[i]
            conv(self.padded_input_array, filters.getWeights(), self.output_array[i], self.stride, filters.getBias())
            ConvLayer.elementWiseOp(self.output_array, self.activator.forward)


    def backward(self, input_array, sensitivity_array, activator):
        """
        误差反向传播,计算每个权重的梯度，前一层的误差存储在self.delta_array,梯度保存在Filter对象weights_grad里
        input_array: 该层的输入
        sensitivity_array: 当前层的输出误差
        activator: 激活函数
        """
        self.forward(input_array) # 根据输入计算经过该卷积层的后的输出
        self.bpSensitivityMap(sensitivity_array, activator) # 将误差传递到上一层
        self.bpGardient(sensitivity_array) # 计算每个过滤器的w和b


    def update(self):
        """
        按照梯度下降更新权重
        """
        for f in self.filters:
            f.update(self.learning_rate)


    def bpSensitivityMap(self, sensitivity_array, activator):
        """
        将误差传递到上一层，公式(15)
        sensitivity_array: 当前层的误差
        """
        expanded_error_array = self.expandSensitivityMap(sensitivity_array)
        expanded_width = np.shape(expanded_error_array)[2]

        # 获得步长,进行补零
        zp = int((self.input_width - expanded_width + self.filter_width - 1) / 2)
        padding_array = ConvLayer.padding(expanded_error_array, zp)

        self.delta_array = self.createDeltaArray() # 保存传递到上一层的sensitivity map
        for i in range(self.filter_number):
            # 对于多个filter的卷积层来说，最终传递给上一层的sensitivity map相当于所有filter的sensitivity map之和
            f = self.filters[i]
            flipped_weights = []
            for w in f.getWeights(): # 不同通道翻转
                flipped_weights.append(np.rot90(w, 2)) # 逆时针旋转（90×k）°，k取负数时表示顺时针旋转。
            flipped_weights = np.array(flipped_weights)
            delta_array = self.createDeltaArray()
            for d in range(np.shape(delta_array)[0]):
                conv(padding_array[i], flipped_weights[d], delta_array[d], 1, 0)
            self.delta_array += delta_array

        derivative_array = np.array(self.input_array)
        ConvLayer.elementWiseOp(derivative_array, activator.backward)
        self.delta_array *= derivative_array # 得到上一层误差


    def expandSensitivityMap(self, sensitivity_array):
        """
        对步长大于1时的sensitivity map相应位置进行补0，将其还原成步长为1时的sensitivity map,再用（14）[（8）]进行求解
        """
        depth = sensitivity_array.shape[0]

        # 获得stride=1时的sensitivity map大小
        expanded_width = ConvLayer.calOutputSize(self.input_width, self.filter_width, self.zero_padding, 1)
        expanded_height = ConvLayer.calOutputSize(self.input_height, self.filter_height, self.zero_padding, 1)
        expand_array = np.zeros((depth, expanded_height, expanded_width))

        for i in range(self.output_height):
            for j in range(self.output_width):
                i_pos = i * self.stride
                j_pos = j * self.stride
                expand_array[:, i_pos, j_pos] = sensitivity_array[:, i, j]
        return expand_array


    def bpGardient(self, sensitivity_array):
        """
        计算偏置项的梯度
        偏置项的梯度就是sensitivity map 所有误差项之和
        """
        expanded_error_array = self.expandSensitivityMap(sensitivity_array)
        for i in range(self.filter_number):
            f = self.filters[i]
            for d in range(f.weights.shape[0]):
                conv(self.padded_input_array[d], expanded_error_array[i], f.weights_grad[d], 1, 0)
            f.bias_grad = expanded_error_array[i].sum()


    def createDeltaArray(self):
        """
        初始化delta array
        """
        return np.zeros((self.channel_number, self.input_height, self.input_width))


    @staticmethod
    def calOutputSize(input_size, filter_size, zero_padding, stride):
        """
        计算feature map大小
        """
        return int((input_size - filter_size + 2 * zero_padding) / stride + 1)


    @staticmethod
    def padding(input_array, zp):
        """
        补零
        input_array: 输入数组
        zp: 补零数目
        """
        if zp == 0:
            return input_array
        if input_array.ndim == 3:
            d, h, w = np.shape(input_array)
            padding_array = np.zeros((d, h + 2 * zp, w + 2 * zp))
            padding_array[:, zp : zp + h, zp : zp + w] = input_array # 替换中间的0矩阵
        elif input_array.ndim == 2:
            h, w = np.shape(input_array)
            padding_array = np.zeros((h + 2 * zp, w + 2 * zp))
            padding_array[zp : zp + h, zp : zp + w] = input_array

        return padding_array


    @staticmethod
    def elementWiseOp(array, op):
        """
        对array中的元素逐一处理
        op : 处理方法
        """
        for x in np.nditer(array, op_flags=['readwrite']):
            x[...] = op(x)



class MaxPoolingLayer(object):
    """
    下采样类，不改变通道数目，不补零
    """
    def __init__(self, input_width, input_height, channel_number, filter_width, filter_height, stride):
        """
        输入宽度，高度，通道数，滤波器宽度，滤波器高度，步长
        """
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.stride = stride
        self.output_width = int((input_width -filter_width) / self.stride + 1)
        self.output_height = int((input_height -filter_height) / self.stride + 1)
        self.output_array = np.zeros((self.channel_number,self.output_height, self.output_width)) # 输出结果

    def forward(self, input_array):
        """
        前向传播
        卷积区域最大值
        """
        for d in range(self.channel_number):
            for i in range(self.output_height):
                for j in range(self.output_width):
                    self.output_array[d, i, j] = getConvArea(input_array[d], i, j, self.filter_width, self.filter_height, self.stride).max()


    def backward(self, input_array, sensitivity_array):
        """
        反向传播采样层的误差，将误差传递给上一层
        input_array: 上一层输出
        sensitivity_array： 当前层误差
        """
        self.delta_array = np.zeros(np.shape(input_array))
        for d in range(self.channel_number):
            for i in range(self.output_height):
                for j in range(self.output_width):
                    patch_array = getConvArea(input_array[d], i, j, self.filter_width, self.filter_height, self.stride)
                    m, n = getMaxIndex(patch_array)
                    self.delta_array[d, i * self.stride + m, j * self.stride + n] = sensitivity_array[d, i, j] # 更新误差


