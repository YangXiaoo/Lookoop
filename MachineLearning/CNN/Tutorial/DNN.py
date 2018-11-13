# 实现神经网络反向传播算法，以此来训练网络。全连接神经网络可以包含多层，但是只有最后一层输出前有激活函数。
# 所谓向量化编程，就是使用矩阵运算。

import random
import math
import numpy as np
import datetime
import Activators  # 引入激活器模块

# 1. 当为array的时候，默认d*f就是对应元素的乘积，multiply也是对应元素的乘积，dot（d,f）会转化为矩阵的乘积， dot点乘意味着相加，而multiply只是对应元素相乘，不相加
# 2. 当为mat的时候，默认d*f就是矩阵的乘积，multiply转化为对应元素的乘积，dot（d,f）为矩阵的乘积



# 全连接每层的实现类。输入对象x、神经层输出a、输出y均为列向量
class FullConnectedLayer(object):
    # 全连接层构造函数。input_size: 本层输入列向量的维度。output_size: 本层输出列向量的维度。activator: 激活函数
    def __init__(self, input_size, output_size,activator,learning_rate):
        self.input_size = input_size
        self.output_size = output_size
        self.activator = activator
        # 权重数组W。初始化权重为(rand(output_size, input_size) - 0.5) * 2 * sqrt(6 / (output_size + input_size))
        wimin = (output_size - 0.5) * 2 * math.sqrt(6 / (output_size + input_size))
        wimax = (input_size-0.5)*2*math.sqrt(6/(output_size + input_size))
        # self.W = np.random.uniform(wimin,wimax,(output_size, input_size))  #初始化为-0.1~0.1之间的数。权重的大小。行数=输出个数，列数=输入个数。a=w*x，a和x都是列向量
        self.W = np.random.uniform(-0.1, 0.1,(output_size, input_size))  # 初始化为-0.1~0.1之间的数。权重的大小。行数=输出个数，列数=输入个数。a=w*x，a和x都是列向量
        # 偏置项b
        self.b = np.zeros((output_size, 1))  # 全0列向量偏重项
        # 学习速率
        self.learning_rate = learning_rate
        # 输出向量
        self.output = np.zeros((output_size, 1)) #初始化为全0列向量

    # 前向计算，预测输出。input_array: 输入列向量，维度必须等于input_size
    def forward(self, input_array):   # 式2
        self.input = input_array
        self.output = self.activator.forward(np.dot(self.W, input_array) + self.b)

    # 反向计算W和b的梯度。delta_array: 从上一层传递过来的误差项。列向量
    def backward(self, delta_array):
        # 式8
        self.delta = np.multiply(self.activator.backward(self.input),np.dot(self.W.T, delta_array))   #计算当前层的误差，以备上一层使用
        self.W_grad = np.dot(delta_array, self.input.T)   # 计算w的梯度。梯度=误差.*输入
        self.b_grad = delta_array  #计算b的梯度

    # 使用梯度下降算法更新权重
    def update(self):
        self.W += self.learning_rate * self.W_grad
        self.b += self.learning_rate * self.b_grad
