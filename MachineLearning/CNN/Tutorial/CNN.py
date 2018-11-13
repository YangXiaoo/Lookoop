import numpy as np
import Activators   # 引入自定义的激活器模块
import math

# 获取卷积区域。input_array为单通道或多通道的矩阵顺。i为横向偏移，j为纵向偏移，stride为步幅，filter_width为过滤器宽度，filter_height为过滤器的高度
def get_patch(input_array, i, j, filter_width,filter_height, stride):
    '''
    从输入数组中获取本次卷积的区域，
    自动适配输入为2D和3D的情况
    '''
    start_i = i * stride
    start_j = j * stride
    if input_array.ndim == 2:  #如果只有一个通道
        return input_array[start_i:start_i + filter_height,start_j: start_j + filter_width]
    elif input_array.ndim == 3:  #如果有多个通道，也就是深度上全选
        return input_array[:,start_i: start_i + filter_height,start_j: start_j + filter_width]


# 获取一个2D区域的最大值所在的索引
def get_max_index(array):
    location = np.where(array == np.max(array))
    return location[0], location[1]


# 计算一个过滤器的卷积运算，输出一个二维数据。每个通道的输入是图片，但是可能不是一个通道，所以这里自动适配输入为2D和3D的情况。
def conv(input_array,kernel_array,output_array,stride, bias):
    output_width = output_array.shape[1]   # 获取输出的宽度。一个过滤器产生的输出一定是一个通道
    output_height = output_array.shape[0] # 获取输出的高度
    kernel_width = kernel_array.shape[-1]  # 过滤器的宽度。有可能有多个通道。多通道时shape=[深度、高度、宽度]，单通道时shape=[高度、宽度]
    kernel_height = kernel_array.shape[-2] # 过滤器的高度。有可能有多个通道。多通道时shape=[深度、高度、宽度]，单通道时shape=[高度、宽度]
    for i in range(output_height):
        for j in range(output_width):
            juanjiqu = get_patch(input_array, i, j, kernel_width,kernel_height, stride)   # 获取输入的卷积区。（单通道或多通道）
            # 这里是对每个通道的两个矩阵对应元素相乘求和，再将每个通道的和值求和
            kernel_values= (np.multiply(juanjiqu,kernel_array)).sum() # 卷积区与过滤器卷积运算。1，一个通道内，卷积区矩阵与过滤器矩阵对应点相乘后，求和值。2、将每个通道的和值再求和。
            output_array[i][j] = kernel_values + bias  #将卷积结果加上偏量



# 为数组增加Zero padding。zp步长，自动适配输入为2D和3D的情况
def padding(input_array, zp):
    if zp == 0: # 如果不补0
        return input_array
    else:
        if input_array.ndim == 3:   # 如果输入有多个通道
            input_width = input_array.shape[2]  # 获取输入的宽度
            input_height = input_array.shape[1]  # 获取输入的宽度
            input_depth = input_array.shape[0]  # 获取输入的深度
            padded_array = np.zeros((input_depth,input_height + 2 * zp,input_width + 2 * zp))  # 先定义一个补0后大小的全0矩阵
            padded_array[:,zp: zp + input_height,zp: zp + input_width] = input_array # 每个通道上，将中间部分替换成输入，这样就变成了原矩阵周围补0 的形式
            return padded_array
        elif input_array.ndim == 2:  # 如果输入只有一个通道
            input_width = input_array.shape[1] # 获取输入的宽度
            input_height = input_array.shape[0] # 虎丘输入的高度
            padded_array = np.zeros((input_height + 2 * zp,input_width + 2 * zp))  # 先定义一个补0后大小的全0矩阵
            padded_array[zp: zp + input_height,zp: zp + input_width] = input_array  # 将中间部分替换成输入，这样就变成了原矩阵周围补0 的形式
            return padded_array


# 对numpy数组进行逐个元素的操作。op为函数。element_wise_op函数实现了对numpy数组进行按元素操作，并将返回值写回到数组中
def element_wise_op(array, op):
    for i in np.nditer(array,op_flags=['readwrite']):
        i[...] = op(i)   # 将元素i传入op函数，返回值，再修改i

# Filter类保存了卷积层的参数以及梯度，并且实现了用梯度下降算法来更新参数。
class Filter(object):
    def __init__(self, width, height, depth,filter_num):
        # 卷积核每个元素初始化为[-sqrt(6 / (fan_in + fan_out)), sqrt(6 / (fan_in + fan_out))]。
        # 其中fan_in为输入通道数与滤波器宽高的乘机，即width*height*depth
        # 其中fan_out为输出通道数与滤波器宽高的乘机，即width*height*filter_num
        wimin = -math.sqrt(6 / (width*height*depth + width*height*filter_num))
        wimax = -wimin
        self.weights = np.random.uniform(wimin, wimax, (depth, height, width))  # 随机初始化卷基层权重一个很小的值，
        # self.weights = np.random.uniform(-1e-2, 1e-2,(depth, height, width))  # 随机初始化卷基层权重一个很小的值，
        self.bias = 0  # 初始化偏量为0
        self.weights_grad = np.zeros(self.weights.shape)   # 初始化权重梯度
        self.bias_grad = 0  # 初始化偏量梯度

    def __repr__(self):
        return 'filter weights:\n%s\nbias:\n%s' % (repr(self.weights), repr(self.bias))

    # 读取权重
    def get_weights(self):
        return self.weights

    # 读取偏量
    def get_bias(self):
        return self.bias

    # 更新权重和偏量
    def update(self, learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias_grad

# 用ConvLayer类来实现一个卷积层。下面的代码是初始化一个卷积层，可以在构造函数中设置卷积层的超参数
class ConvLayer(object):
    #初始化构造卷积层：输入宽度、输入高度、通道数、滤波器宽度、滤波器高度、滤波器数目、补零数目、步长、激活器、学习速率
    def __init__(self, input_width, input_height,channel_number, filter_width,filter_height, filter_number,
                 zero_padding, stride, activator,learning_rate):
        self.input_width = input_width   #  输入宽度
        self.input_height = input_height  # 输入高度
        self.channel_number = channel_number  # 通道数=输入的深度=过滤器的深度
        self.filter_width = filter_width  # 过滤器的宽度
        self.filter_height = filter_height  # 过滤器的高度
        self.filter_number = filter_number  # 过滤器的数量。
        self.zero_padding = zero_padding  # 补0圈数
        self.stride = stride # 步幅
        self.output_width = int(ConvLayer.calculate_output_size(self.input_width, filter_width, zero_padding,stride))  # 计算输出宽度
        self.output_height = int(ConvLayer.calculate_output_size(self.input_height, filter_height, zero_padding,stride))  # 计算输出高度
        self.output_array = np.zeros((self.filter_number,self.output_height, self.output_width)) # 创建输出三维数组。每个过滤器都产生一个二维数组的输出
        self.filters = []   # 卷积层的每个过滤器
        for i in range(filter_number):
            self.filters.append(Filter(filter_width,filter_height, self.channel_number,filter_number))
        self.activator = activator   # 使用rule激活器
        self.learning_rate = learning_rate  # 学习速率

    # 计算卷积层的输出。输出结果保存在self.output_array
    def forward(self, input_array):
        self.input_array = input_array  # 多个通道的图片，每个通道为一个二维图片
        self.padded_input_array = padding(input_array,self.zero_padding)  # 先将输入补足0
        for i in range(self.filter_number):  #每个过滤器都产生一个二维数组的输出
            filter = self.filters[i]
            conv(self.padded_input_array,filter.get_weights(), self.output_array[i],self.stride, filter.get_bias())
        # element_wise_op函数实现了对numpy数组进行按元素操作，并将返回值写回到数组中
        element_wise_op(self.output_array,self.activator.forward)

    # 后向传播。input_array为该层的输入，sensitivity_array为当前层的输出误差（和输出的维度相同），activator为激活函数
    def backward(self, input_array, sensitivity_array,activator):

        '''
        计算传递给前一层的误差项，以及计算每个权重的梯度
        前一层的误差项保存在self.delta_array
        梯度保存在Filter对象的weights_grad
        '''

        self.forward(input_array)   # 先根据输入计算经过该卷积层后的输出。（卷积层有几个过滤器，输出层的深度就是多少。输出每一层为一个二维数组）
        self.bp_sensitivity_map(sensitivity_array, activator)   # 将误差传递到前一层，self.delta_array存储上一次层的误差
        self.bp_gradient(sensitivity_array)   # 计算每个过滤器的w和b梯度

    # 按照梯度下降，更新权重
    def update(self):
        for filter in self.filters:
            filter.update(self.learning_rate)   # 每个过滤器


    # 将误差项传递到上一层。sensitivity_array: 本层的误差。activator: 上一层的激活函数
    def bp_sensitivity_map(self, sensitivity_array,activator):   # 公式9
        # 根据卷积步长，对原始sensitivity map进行补0扩展，扩展成如果步长为1的输出误差形状。再用公式8求解
        expanded_error_array = self.expand_sensitivity_map(sensitivity_array)
        # print(sensitivity_array)
        # full卷积，对sensitivitiy map进行zero padding
        # 虽然原始输入的zero padding单元也会获得残差，但这个残差不需要继续向上传递，因此就不计算了
        expanded_width = expanded_error_array.shape[2]   # 误差的宽度
        zp = int((self.input_width + self.filter_width - 1 - expanded_width) / 2)   # 计算步长
        padded_array = padding(expanded_error_array, zp)  #补0操作
        # 初始化delta_array，用于保存传递到上一层的sensitivity map
        self.delta_array = self.create_delta_array()
        # 对于具有多个filter的卷积层来说，最终传递到上一层的sensitivity map相当于所有的filter的sensitivity map之和
        for i in range(self.filter_number):   # 遍历每一个过滤器。每个过滤器都产生多通道的误差，多个多通道的误差叠加
            filter = self.filters[i]
            # 将滤波器每个通道的权重权重翻转180度。
            flipped_weights=[]
            for oneweight in filter.get_weights():  # 这一个滤波器下的每个通道都进行180翻转
                flipped_weights.append(np.rot90(oneweight, 2))
            flipped_weights = np.array(flipped_weights)
            # 计算与一个filter对应的delta_array
            delta_array = self.create_delta_array()
            for d in range(delta_array.shape[0]):   # 计算每个通道上的误差，存储在delta_array的对应通道上
                # print('大小：\n',flipped_weights[d])
                conv(padded_array[i], flipped_weights[d],delta_array[d], 1, 0)
            self.delta_array += delta_array   # 将每个滤波器每个通道产生的误差叠加

        # 将计算结果与激活函数的偏导数做element-wise乘法操作
        derivative_array = np.array(self.input_array)  # 复制一个矩阵，因为下面的会改变元素的值，所以深复制了一个矩阵
        element_wise_op(derivative_array,activator.backward)  # 逐个元素求偏导数。
        self.delta_array *= derivative_array  # 误差乘以偏导数。得到上一层的误差

    # 计算梯度。根据误差值，计算本层每个过滤器的w和b的梯度
    def bp_gradient(self, sensitivity_array):
        # 处理卷积步长，对原始sensitivity map进行扩展，扩展成如果步长为1的输出误差形状。再用公式8求解
        expanded_error_array = self.expand_sensitivity_map(sensitivity_array)
        for i in range(self.filter_number):  # 每个过滤器产生一个输出
            # 计算每个权重的梯度
            filter = self.filters[i]
            for d in range(filter.weights.shape[0]):   # 过滤器的每个通道都要计算梯度
                conv(self.padded_input_array[d],expanded_error_array[i],filter.weights_grad[d], 1, 0)   #  公式（31、32中间）

            # 计算偏置项的梯度
            filter.bias_grad = expanded_error_array[i].sum()   # 公式（34）

    # 对步长为S的sensitivitymap相应的位置进行补0，将其『还原』成步长为1时的sensitivitymap，再用式8进行求解
    def expand_sensitivity_map(self, sensitivity_array):
        depth = sensitivity_array.shape[0]   # 获取误差项的深度
        # 确定扩展后sensitivity map的大小，即计算stride为1时sensitivity map的大小
        expanded_width = (self.input_width - self.filter_width + 2 * self.zero_padding + 1)
        expanded_height = (self.input_height - self.filter_height + 2 * self.zero_padding + 1)
        # 构建新的sensitivity_map
        expand_array = np.zeros((depth, expanded_height, expanded_width))
        # 从原始sensitivity map拷贝误差值，每有拷贝的位置，就是要填充的0
        for i in range(self.output_height):
            for j in range(self.output_width):
                i_pos = i * self.stride
                j_pos = j * self.stride
                expand_array[:, i_pos, j_pos] = sensitivity_array[:, i, j]
        return expand_array

    # 创建用来保存传递到上一层的sensitivity map的数组。（上一层的输出也就是这一层的输入。所以上一层的误差项的维度和这一层的输入的维度相同）
    def create_delta_array(self):
        return np.zeros((self.channel_number,self.input_height, self.input_width))


    # 确定卷积层输出的大小
    @staticmethod
    def calculate_output_size(input_size,filter_size, zero_padding, stride):
        return (input_size - filter_size + 2 * zero_padding) / stride + 1



# Max Pooling层的实现。就是一个卷积区域取最大值，形成输出。除了Max Pooing之外，常用的还有Mean Pooling——取各样本的平均值。
# 采样层并不改变输入的通道数，也不补零，只是通过某种卷积方式实现降采样
class MaxPoolingLayer(object):
    # 构造降采样层，参数为输入宽度、高度、通道数、滤波器宽度、滤波器高度、步长
    def __init__(self, input_width, input_height,channel_number, filter_width,filter_height, stride):
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.stride = stride
        self.output_width = int((input_width -filter_width) / self.stride + 1)
        self.output_height = int((input_height -filter_height) / self.stride + 1)
        self.output_array = np.zeros((self.channel_number,self.output_height, self.output_width))

    # 前向计算。
    def forward(self, input_array):
        for d in range(self.channel_number):
            for i in range(self.output_height):
                for j in range(self.output_width):
                    self.output_array[d, i, j] = (get_patch(input_array[d], i, j,self.filter_width,self.filter_height,self.stride).max())   # 获取卷积区后去最大值

    # 后向传播误差
    def backward(self, input_array, sensitivity_array):
        self.delta_array = np.zeros(input_array.shape)
        for d in range(self.channel_number):
            for i in range(self.output_height):
                for j in range(self.output_width):
                    patch_array = get_patch(input_array[d], i, j,self.filter_width,self.filter_height,self.stride)  # 获取卷积区
                    k, l = get_max_index(patch_array)  # 获取最大值的位置
                    self.delta_array[d,i * self.stride + k,j * self.stride + l] = sensitivity_array[d, i, j]   # 更新误差
