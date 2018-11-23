# coding:UTF-8
# 2018-11-22
# LSTM-长短时记忆网络
# https://zybuluo.com/hanbingtao/note/581764

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
        self.f_list.append(fg)

        ig = self.calcGate(x, self.Wix, self.Wih, self.bi, self.gate_activator) # 输入门
        self.i_list.append(ig)

        ct = self.calcGate(x, self.Wcx, self.Wch, self.bc, self.output_activator) # 即时状态
        self.ct_list.append(ct)

        c = fg * self.c_list[self.times - 1] + ig * ct
        self.c_list.append(c) # 存储上一次单元状态

        og = self.calcGate(x, self.Wox, self.Woh, self.bo, self.gate_activator)
        self.o_list.append(og)

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


    def calcDeltaK(self, k):
        """
        根据K时刻的delta_h，计算k时刻的delta_f, delta_i, delta_o, delta_ct，以及k-1时刻的delta_h....
        """
        # 获得k时刻向前计算的值
        ig = self.i_list[k]
        og = self.o_list[k]
        fg = self.f_list[k]
        ct = self.ct_list[k]
        c = self.c_list[k]
        c_prev = self.c_list[k - 1]
        tanh_c = self.output_activator.forward(c) # tanh(ct)
        delta_k = self.delta_h_list[k]

        # 根据公式9-12计算各个门的误差项
        delta_o = (delta_k * tanh_c * 
            self.gate_activator.backward(og))
        delta_f = (delta_k * og * 
            (1 - tanh_c * tanh_c) * c_prev *
            self.gate_activator.backward(fg))
        delta_i = (delta_k * og * 
            (1 - tanh_c * tanh_c) * ct *
            self.gate_activator.backward(ig))
        delta_ct = (delta_k * og * 
            (1 - tanh_c * tanh_c) * ig *
            self.output_activator.backward(ct))

        # 传递到长一层的误差
        delta_h_prev = (
                np.dot(delta_o.transpose(), self.Woh) +
                np.dot(delta_i.transpose(), self.Wih) +
                np.dot(delta_f.transpose(), self.Wfh) +
                np.dot(delta_ct.transpose(), self.Wch)
            ).transpose()

        # 保存全部delta值
        self.delta_h_list[k-1] = delta_h_prev
        self.delta_f_list[k] = delta_f
        self.delta_i_list[k] = delta_i
        self.delta_o_list[k] = delta_o
        self.delta_ct_list[k] = delta_ct


    def clacGradient(self, x):
        """
        计算梯度
        """
        self.Wfh_grad, self.Wfx_grad, self.bf_grad = self.initWeightMat() # 遗忘门权重矩阵Wfh,Wfx,偏置项bf
        self.Wih_grad, self.Wix_grad, self.bi_grad = self.initWeightMat() # 输入门权重矩阵Wih,Wix,偏置项bi
        self.Woh_grad, self.Wox_grad, self.bo_grad = self.initWeightMat() # 输出门权重矩阵Wfh, Wfx, 偏置项bf
        self.Wch_grad, self.Wcx_grad, self.bc_grad = self.initWeightMat() # 单元状态权重矩阵Wfh, Wfx, 偏置项bf

        # 计算对上一次输出的h的权重梯度
        for t in range(self.times, 0, -1):
            # 计算各个时刻的梯度
            Wfh_grad, bf_grad,Wih_grad,\
            bi_grad,Woh_grad, bo_grad,Wch_grad, bc_grad = self.calcGradientT(t)
            # 实际梯度是各时刻梯度之和
            self.Wfh_grad += Wfh_grad
            self.bf_grad += bf_grad
            self.Wih_grad += Wih_grad
            self.bi_grad += bi_grad
            self.Woh_grad += Woh_grad
            self.bo_grad += bo_grad
            self.Wch_grad += Wch_grad
            self.bc_grad += bc_grad

        # 计算对本次输入x的权重梯度
        xt = x.transpose()
        self.Wfx_grad = np.dot(self.delta_f_list[-1], xt)
        self.Wix_grad = np.dot(self.delta_i_list[-1], xt)
        self.Wox_grad = np.dot(self.delta_o_list[-1], xt)
        self.Wcx_grad = np.dot(self.delta_ct_list[-1], xt)


    def calcGradientT(self, t):
        '''
        计算每个时刻t权重的梯度
        '''
        h_prev = self.h_list[t-1].transpose()
        Wfh_grad = np.dot(self.delta_f_list[t], h_prev)
        bf_grad = self.delta_f_list[t]
        Wih_grad = np.dot(self.delta_i_list[t], h_prev)
        bi_grad = self.delta_f_list[t]
        Woh_grad = np.dot(self.delta_o_list[t], h_prev)
        bo_grad = self.delta_f_list[t]
        Wch_grad = np.dot(self.delta_ct_list[t], h_prev)
        bc_grad = self.delta_ct_list[t]
        return Wfh_grad, bf_grad, Wih_grad, bi_grad, \
               Woh_grad, bo_grad, Wch_grad, bc_grad


    def resetState(self):
        """
        初始化各个状态列表
        """
        self.times = 0
        self.c_list = self.initStateVec() # 各个时刻单元状态向量c
        self.h_list = self.initStateVec() # 各个时刻输出向量h
        self.f_list = self.initStateVec() # 各个时刻的遗忘门f
        self.i_list = self.initStateVec() # 各个时刻的输入门i
        self.o_list = self.initStateVec() # 各个时刻的输出门o
        self.ct_list = self.initStateVec() # 


    def update(self):
        '''
        按照梯度下降，更新权重
        '''
        self.Wfh -= self.learning_rate * self.Whf_grad
        self.Wfx -= self.learning_rate * self.Whx_grad
        self.bf -= self.learning_rate * self.bf_grad
        self.Wih -= self.learning_rate * self.Whi_grad
        self.Wix -= self.learning_rate * self.Whi_grad
        self.bi -= self.learning_rate * self.bi_grad
        self.Woh -= self.learning_rate * self.Wof_grad
        self.Wox -= self.learning_rate * self.Wox_grad
        self.bo -= self.learning_rate * self.bo_grad
        self.Wch -= self.learning_rate * self.Wcf_grad
        self.Wcx -= self.learning_rate * self.Wcx_grad
        self.bc -= self.learning_rate * self.bc_grad


def dataSet():
    """
    测试数据集
    """
    x = [np.array([[1], [2], [3]]),
         np.array([[2], [3], [4]])]
    d = np.array([[1], [2]])
    return x, d


def gradientCheck():
    """
    检查梯度
    """
    error_function = lambda o: o.sum()

    lstm = LstmLayer(3, 2, 1e-3)
    x, d = dataSet()

    # 向前传播
    lstm.forward(x[0])
    lstm.forward(x[1])


    # 求取sensitivity map
    sensitivity_array = np.ones(lstm.h_list[-1].shape,
                                dtype=np.float64)
    # 计算梯度
    lstm.backward(x[1], sensitivity_array, IdentityActivator())
    
    # 检查梯度
    epsilon = 10e-4
    for i in range(lstm.Wfh.shape[0]):
        for j in range(lstm.Wfh.shape[1]):
            lstm.Wfh[i,j] += epsilon
            lstm.resetState()
            lstm.forward(x[0])
            lstm.forward(x[1])
            err1 = error_function(lstm.h_list[-1])
            lstm.Wfh[i,j] -= 2*epsilon
            lstm.resetState()
            lstm.forward(x[0])
            lstm.forward(x[1])
            err2 = error_function(lstm.h_list[-1])
            expect_grad = (err1 - err2) / (2 * epsilon)
            lstm.Wfh[i,j] += epsilon
            print('weights(%d,%d): expected - actural %.4e - %.4e' % (i, j, expect_grad, lstm.Wfh_grad[i,j]))
    return lstm

if __name__ == '__main__':
    gradientCheck()