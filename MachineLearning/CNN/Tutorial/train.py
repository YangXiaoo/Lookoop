# 使用全连接神经网络类，和手写数据加载器，实现验证码识别。

import datetime
import numpy as np
import Activators  # 引入激活器模块
import CNN   # 引入卷积神经网络
import MNIST  # 引入手写数据加载器
import DNN  # 引入全连接神经网络

# 网络模型类
class MNISTNetwork():
    # =============================构造网络结构=============================
    def __init__(self):
        # 初始化构造卷积层：输入宽度、输入高度、通道数、滤波器宽度、滤波器高度、滤波器数目、补零数目、步长、激活器、学习速率
        self.cl1 = CNN.ConvLayer(28, 28, 1, 5, 5, 6, 0, 1, Activators.SigmoidActivator(),0.02)  # 输入28*28 一通道，滤波器5*5的6个，步长为1，不补零，所以输出为24*24深度6
        # 构造降采样层，参数为输入宽度、高度、通道数、滤波器宽度、滤波器高度、步长
        self.pl1 = CNN.MaxPoolingLayer(24, 24, 6, 2, 2, 2)  # 输入24*24，6通道，滤波器2*2，步长为2，所以输出为12*12，深度保持不变为6
        # 初始化构造卷积层：输入宽度、输入高度、通道数、滤波器宽度、滤波器高度、滤波器数目、补零数目、步长、激活器、学习速率
        self.cl2 = CNN.ConvLayer(12, 12, 6, 5, 5, 12, 0, 1, Activators.SigmoidActivator(),0.02)  # 输入12*12，6通道，滤波器5*5的12个，步长为1，不补零，所以输出为8*8深度12
        # 构造降采样层，参数为输入宽度、高度、通道数、滤波器宽度、滤波器高度、步长
        self.pl2 = CNN.MaxPoolingLayer(8, 8, 12, 2, 2, 2)  # 输入8*8，12通道，滤波器2*2，步长为2，所以输出为4*4，深度保持不变为12。共192个像素
        # 全连接层构造函数。input_size: 本层输入向量的维度。output_size: 本层输出向量的维度。activator: 激活函数
        self.fl1 = DNN.FullConnectedLayer(192, 10, Activators.SigmoidActivator(),0.02)  # 输入192个像素，输出为10种分类概率,学习速率为0.05

    # 根据输入计算一次输出。因为卷积层要求的数据要求有通道数，所以onepic是一个包含深度，高度，宽度的多维矩阵
    def forward(self,onepic):
        # print('图片：',onepic.shape)
        self.cl1.forward(onepic)
        # print('第一层卷积结果：',self.cl1.output_array.shape)
        self.pl1.forward(self.cl1.output_array)
        # print('第一层采样结果：',self.pl1.output_array.shape)
        self.cl2.forward(self.pl1.output_array)
        # print('第二层卷积结果：',self.cl2.output_array.shape)
        self.pl2.forward(self.cl2.output_array)
        # print('第二层采样结果：',self.pl2.output_array.shape)
        flinput = self.pl2.output_array.flatten().reshape(-1, 1)  # 转化为列向量
        self.fl1.forward(flinput)
        # print('全连接层结果：',self.fl1.output.shape)
        return  self.fl1.output

    def backward(self,onepic,labels):
        # 计算误差
        delta = np.multiply(self.fl1.activator.backward(self.fl1.output), (labels - self.fl1.output))  # 计算输出层激活函数前的误差
        # print('输出误差：',delta.shape)

        # 反向传播
        self.fl1.backward(delta)  # 计算了全连接层输入前的误差，以及全连接的w和b的梯度
        self.fl1.update()  # 更新权重w和偏量b
        # print('全连接层输入误差：', self.fl1.delta.shape)
        sensitivity_array = self.fl1.delta.reshape(self.pl2.output_array.shape)  # 将误差转化为同等形状
        self.pl2.backward(self.cl2.output_array, sensitivity_array)  # 计算第二采样层的输入误差。参数为第二采样层的 1、输入，2、输出误差
        # print('第二采样层的输入误差：', self.pl2.delta_array.shape)
        self.cl2.backward(self.pl1.output_array, self.pl2.delta_array,Activators.SigmoidActivator())  # 计算第二卷积层的输入误差。参数为第二卷积层的 1、输入，2、输出误差，3、激活函数
        self.cl2.update()  # 更新权重w和偏量b
        # print('第二卷积层的输入误差：', self.cl2.delta_array.shape)
        self.pl1.backward(self.cl1.output_array, self.cl2.delta_array)  # 计算第一采样层的输入误差。参数为第一采样层的 1、输入，2、输出误差
        # print('第一采样层的输入误差：', self.pl1.delta_array.shape)
        self.cl1.backward(onepic, self.pl1.delta_array,Activators.SigmoidActivator())  # 计算第一卷积层的输入误差。参数为第一卷积层的 1、输入，2、输出误差，3、激活函数
        self.cl1.update()  # 更新权重w和偏量b
        # print('第一卷积层的输入误差：', self.cl1.delta_array.shape)



# 由于使用了逻辑回归函数，所以只能进行分类识别。识别ont-hot编码的结果
if __name__ == '__main__':

    # =============================加载数据集=============================
    train_data_set, train_labels = MNIST.get_training_data_set(600, False)  # 加载训练样本数据集，和one-hot编码后的样本标签数据集。样本数量越大，训练时间越久，也越准确
    test_data_set, test_labels = MNIST.get_test_data_set(100, False)  # 加载测试特征数据集，和one-hot编码后的测试标签数据集。训练时间越久，也越准确
    train_data_set = np.array(train_data_set).astype(bool).astype(int)    #可以将图片简化为黑白图片
    train_labels = np.array(train_labels)
    test_data_set = np.array(test_data_set).astype(bool).astype(int)    #可以将图片简化为黑白图片
    test_labels = np.array(test_labels)
    print('样本数据集的个数：%d' % len(train_data_set))
    print('测试数据集的个数：%d' % len(test_data_set))


    # =============================构造网络结构=============================
    mynetwork =MNISTNetwork()

    # 打印输出每层网络
    # print('第一卷积层：\n',mynetwork.cl1.filters)
    # print('第二卷积层：\n', mynetwork.cl2.filters)
    # print('全连接层w：\n', mynetwork.fl1.W)
    # print('全连接层b：\n', mynetwork.fl1.b)

    # =============================迭代训练=============================
    for i in range(10):  #迭代训练10次。每个迭代内，对所有训练数据进行训练，更新（训练图像个数/batchsize）次网络参数
        print('迭代：',i)
        for k in range(train_data_set.shape[0]):  #使用每一个样本进行训练
            # 正向计算
            onepic =train_data_set[k]
            onepic = np.array([onepic])  # 卷积神经网络要求的输入必须包含深度、高度、宽度三个维度。
            result = mynetwork.forward(onepic)   # 前向计算一次
            # print(result.flatten())
            labels = train_labels[k].reshape(-1, 1)  # 获取样本输出，转化为列向量
            mynetwork.backward(onepic,labels)



    # 打印输出每层网络
    # print('第一卷积层：\n',mynetwork.cl1.filters)
    # print('第二卷积层：\n', mynetwork.cl2.filters)
    # print('全连接层w：\n', mynetwork.fl1.W)
    # print('全连接层b：\n', mynetwork.fl1.b)

    # =============================评估结果=============================

    right = 0
    for k in range(test_data_set.shape[0]):  # 使用每一个样本进行训练
        # 正向计算
        onepic = test_data_set[k]
        onepic = np.array([onepic])  # 卷积神经网络要求的输入必须包含深度、高度、宽度三个维度。
        result = mynetwork.forward(onepic)  # 前向计算一次
        labels = test_labels[k].reshape(-1, 1)  # 获取样本输出，转化为列向量
        # print(result)
        pred_type = result.argmax()
        real_type = labels.argmax()

        # print(pred_type,real_type)
        if pred_type==real_type:
            right+=1


    print('%s after right ratio is %f' % (datetime.datetime.now(), right/test_data_set.shape[0]))  # 打印输出正确率
