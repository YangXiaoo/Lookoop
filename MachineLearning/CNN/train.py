# coding:UTF-8
# 2018-11-16
# TRAIN

import datetime
import numpy as np 
import Activators
import CNN
import DNN
from api import *

class netWord(object):
    def __init__(self):
        # 第一层卷积：图片输入宽度，高度，通道数，滤波器宽度，滤波器高度，滤波器数目，补零数目，步长，激活器，学习速率
        c_1_w, c_1_h = 256, 256
        self.conv_1 = CNN.ConvLayer(c_1_w, c_1_h, 1, 5, 5, 6, 0, 1, Activators.SigmoidActivator(), 0.01)

        # 下层采样
        # 计算下一层输入大小
        pl_1_w = CNN.ConvLayer.calOutputSize(c_1_w, 5, 0, 1) # 输入宽，滤波器宽，补零，步长
        pl_1_h = CNN.ConvLayer.calOutputSize(c_1_h, 5, 0, 1)
        # 输入的宽度，输入高度，通道数，滤波器宽度，滤波器高度
        self.pl_1 = CNN.MaxPoolingLayer(pl_1_w, pl_1_h, 6, 2, 2, 2)

        # 卷积
        c_2_w = CNN.ConvLayer.calOutputSize(pl_1_w, 2, 0, 2) # 输入宽，滤波器宽，补零，步长
        c_2_h = CNN.ConvLayer.calOutputSize(pl_1_h, 2, 0, 2)
        self.conv_2 = CNN.ConvLayer(c_2_w, c_2_h, 6, 5, 5, 12, 0, 1, Activators.SigmoidActivator(), 0.02)

        # 下层采样
        pl_2_w = CNN.ConvLayer.calOutputSize(c_2_w, 5, 0, 2)
        pl_2_h = CNN.ConvLayer.calOutputSize(c_2_h, 5, 0, 2)
        self.pl_2 = CNN.MaxPoolingLayer(pl_2_w, pl_2_h, 12, 2, 2, 2)

        # 全连接
        fl_1_w = CNN.ConvLayer.calOutputSize(pl_2_w, 2, 0, 2)
        fl_1_h = CNN.ConvLayer.calOutputSize(pl_2_h, 2, 0, 2)
        fl_1_n = int(fl_1_w * fl_1_h * 12) # 上一层输出=长*宽*深度
        self.fl_1 = DNN.FullConnectedLayer(fl_1_n, 10, Activators.SigmoidActivator(),0.02)


    def forward(self, input_data):
        """
        向前传播
        input_data： 输入图片数据
        """
        print("向前传播...")
        # 第一层卷积
        print("第一层卷积...")
        self.conv_1.forward(input_data)
        # 下层采样
        print("第二层下采样...")
        self.pl_1.forward(self.conv_1.output_array)
        # 卷积
        print("第三层卷积...")
        self.conv_2.forward(self.pl_1.output_array)
        # 下层采样
        print("第四层下采样...")
        self.pl_2.forward(self.conv_2.output_array)
        # 全连接层
        print("全连接层...")
        fl_1_input = self.pl_2.output_array.flatten().reshape(-1, 1) # m x 1
        self.fl_1.forward(fl_1_input)
        return self.fl_1.output 


    def backward(self, input_data, lables):
        """
        反向传播误差
        input_data： 输入图片数据
        labels: 图片对应的标签
        """
        # 最后一层的误差
        delta = np.multiply(self.fl_1.activator.backward(self.fl_1.output), (lables - self.fl_1.output))
        # 向前传递
        print("全连接层反向传播误差...")
        self.fl_1.backward(delta)
        self.fl_1.update()
        # 下层采样传递误差
        sensitivity_map = self.fl_1.delta.reshape(self.pl_2.output_array.shape)
        print("第四层下层采样层传播误差...")
        self.pl_2.backward(self.conv_2.output_array, sensitivity_map)
        print("第三层卷积层传播误差...")
        self.conv_2.backward(self.pl_1.output_array, self.pl_2.delta_array, Activators.SigmoidActivator())
        self.conv_2.update()
        print("第二层采样层传播误差...")
        self.pl_1.backward(self.conv_1.output_array, self.conv_2.delta_array)
        print("第一层卷积层传播误差...")
        self.conv_1.backward(input_data, self.pl_1.delta_array, Activators.SigmoidActivator())
        self.conv_1.update()


if __name__ == '__main__':
    data, labels = getTrainingData("C:\\Study\\test\\histogram_no_norm")
    data = np.array(data)
    network = netWord()
    max_iter = 10
    for i in range(max_iter):
        for k in range(data.shape[0]):
            input_data = data[k]
            input_data = np.array([input_data])
            result = network.forward(input_data)
            lable = lables[k].reshape(-1, 1)
            network.backward(input_data, lable)




