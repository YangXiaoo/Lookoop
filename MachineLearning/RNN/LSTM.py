# coding:UTF-8
# 2018-11-22
# LSTM-长短时记忆网络

import matplotlib.pyplot as plt
import numpy as np


def elementWiseOp(array, op):
    """
    对array中的元素逐一处理
    op : 处理方法
    """
    for x in np.nditer(array, op_flags=['readwrite']):
        x[...] = op(x)


class IdentityActivator(object):
    def forward(self, weighted_input):   # 前向计算，计算输出
        return weighted_input

    def backward(self, output):   # 后向计算，计算导数
        return 1


class SigmoidActivator(object):
    def forward(self, weighted_input):
        return 1.0 / (1.0 + np.exp(-weighted_input))

    def backward(self, output):
        # output = SigmoidActivato.forward(weighted_input)
        return np.multiply(output, (1 - output))  # 对应元素相乘


class TanhActivator(object):
    def forward(self, weighted_input):
        return 2.0 / (1.0 + np.exp(-2 * weighted_input)) - 1.0

    def backward(self, output):
        return 1 - output * output


class LstmLayer(object):
	def __init__(self, input_width, state_width, learning_rate):
		self.input_width = input_width
		self.state_width = state_width
		self.learning_rate = learning_rate
		self.gate_activator = SigmoidActivator()
		self.output_activator = TanhActivator()
		self.times = 0 # 当前的时刻初始化为t0
		self.c_list = self.initStateVec() # 各个时刻单元状态向量c
		self.h_list = self.initStateVec() # 各个时刻输出向量h
		self.f_list = self.initStateVec() # 各个时刻的遗忘门f
		self.i_list = self.initStateVec() # 各个时刻的输入门i
		self.o_list = self.initStateVec() # 各个时刻的输出门o
		self.ct_list = self.initStateVec() # 各个时刻的即使状态c~
		self.Wfh, self.Wfx, self.bf = self.initWeightMat() # 遗忘门权重矩阵Wfh,Wfx,偏置项bf
        self.Wih, self.Wix, self.bi = self.initWeightMat() # 输入门权重矩阵Wih,Wix,偏置项bi
        self.Woh, self.Wox, self.bo = self.initWeightMat() # 输出门权重矩阵Wfh, Wfx, 偏置项bf
        self.Wch, self.Wcx, self.bc = self.initWeightMat() # 单元状态权重矩阵Wfh, Wfx, 偏置项bf


    def initStateVec(self):
    	"""
    	初始化保存状态的向量
    	"""
    	state = []
    	state.append(np.zeros((self.state_width, 1)))
    	return state


    def initWeightMat(self):
    	"""
    	初始化权重矩阵
    	"""
    	Wh = np.random.uniform(-1e-4, 1e-4, (self.state_width, self.state_width))
    	Wx = np.random.uniform(-1e-4, 1e-4, (self.state_width, self.input_width))
    	b = np.zeros((self.state_width, 1))
    	return Wh, Wx, b


    def forward(self, x):
    	"""
    	向前传播
    	根据式1-6计算
    	"""
    	self.times += 1
    	fg = self.calcGate(x, self.Wfx, self.Wfh, self.bf, self.gate_activator) # 遗忘门
    	ig = self.calcGate(x, self.Wix, self.Wih, self.bi, self.gate_activator) # 输入门
    	ct = self.calcGate(x, self.Wcx, self.Wch, self.bc, self.output_activator) # 即时状态
    	c = fg * self.c_list[self.times - 1] + ig * ct 
    	self.c_list.append(ct) # 存储上一次单元状态
    	og = self.calcGate(x, self.Wox, self.Woh, self.bo, self.gate_activator)
    	h = og * self.output_activator.forward(c)
    	self.h_list.append(h)


    def calcGate(self, x, Wx, Wh, b, activator):
    	"""
    	门的计算
    	"""
    	h = self.h_list[self.times - 1] # 获取上一次LSTM的输出
    	net = np.dot(Wh, h) + np.dot(Wx, x) + b 
    	gate = activator.forward(net)
    	return gate


    def backward(self, x, delta_h, activator):
    	"""
    	反向传播
    	x: 输入序列
    	delta_h: 输出序列误差
    	"""
    	self.calcDelta(delta_h, activator)
    	self.clacGradient(x)


    def calcDelta(self, delta_h, activator):
    	"""
    	计算误差
    	"""
    	# 初始化各个时刻的误差
    	self.delta_h_list = self.initDelta() # 输出误差项
    	self.delta_f_list = self.initDelta() # 遗忘门误差项
    	self.delta_i_list = self.initDelta() # 输入门误差项
    	self.delta_ct_list = self.initDelta() # 即时输出误差项
    	self.delta_o_list = self.initDelta() # 输出门误差项

    	self.delta_h_list[-1] = delta_h # 保存上一层传递下来的当前时刻的误差项

    	for k in range(self.times, 0, -1):
    		# 迭代计算每个时刻的误差项
    		self.calcDeltaK(k)




    def initDelta(self):
    	"""
    	初始化各项误差
    	"""
    	delta_list = []
    	for i in range(self.times + 1):
    		delta_list.append(np.zeros((self.state_width, 1)))
    	return delta_list


    def update(self):
    	"""
    	更新权重
    	"""
