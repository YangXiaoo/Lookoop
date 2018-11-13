# coding:UTF-8
# 2018-11-13
# 激活函数

import numpy as np

# rule激活器
class ReluActivator(object):
    def forward(self, weighted_input):    # 前向计算，计算输出
        return max(0, weighted_input)

    def backward(self, output):  # 后向计算，计算导数
        return 1 if output > 0 else 0


# IdentityActivator激活器.f(x)=x
class IdentityActivator(object):
    def forward(self, weighted_input):   # 前向计算，计算输出
        return weighted_input

    def backward(self, output):   # 后向计算，计算导数
        return 1


# Sigmoid激活器
class SigmoidActivator(object):
    def forward(self, weighted_input):
        return 1.0 / (1.0 + np.exp(-weighted_input))

    def backward(self, output):
        # output = SigmoidActivato.forward(weighted_input)
        return np.multiply(output, (1 - output))  # 对应元素相乘


# tanh激活器
class TanhActivator(object):
    def forward(self, weighted_input):
        return 2.0 / (1.0 + np.exp(-2 * weighted_input)) - 1.0

    def backward(self, output):
        return 1 - output * output


# softmax激活器
class SoftmaxActivator(object):
    def forward(self, weighted_input):  # 前向计算，计算输出
        return max(0, weighted_input)

    def backward(self, output):  # 后向计算，计算导数
        return 1 if output > 0 else 0
