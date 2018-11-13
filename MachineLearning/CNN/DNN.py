# coding:UTF-8
# 2018-11-13
# 全连接层实现，神经网络反向传播；全连接神经网络可以包含多层，但是只有最后一层输出前有激活函数。

import random
import math
import numpy as np 
import datetime
import Activators

class FullConnectedLayer(object):
	"""
	全连接层构造函数
	"""
	def __init__(self, input_size, output_size, activator, learning_rate):
		self.input_size = input_size
		self.output_size = output_size
		self.activator = activator

		# self.w = np.random.normal(0.0, pow(self.output_size, -0.5), (output_size, input_size))
		self.w = np.random.normal(-0.1, 0.1, (output_size, input_size))
		self.b = np.zeros((output_size, 1))

		self.learning_rate = learning_rate
		self.output = np.zeros((output_size, 1)) # 输出化初始为0向量

	def forward(self, input_array):
		self.input = input_array
		self.output = self.activator.forward(np.dot(self.w, input_array) + self.b)


	def backward(self, delta_array):
		

