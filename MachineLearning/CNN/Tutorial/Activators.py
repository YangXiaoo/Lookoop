# 1. 当为array的时候，默认d*f就是对应元素的乘积，multiply也是对应元素的乘积，dot（d,f）会转化为矩阵的乘积， dot点乘意味着相加，而multiply只是对应元素相乘，不相加
# 2. 当为mat的时候，默认d*f就是矩阵的乘积，multiply转化为对应元素的乘积，dot（d,f）为矩阵的乘积

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

#Sigmoid激活器
class SigmoidActivator(object):
    def forward(self, weighted_input):
        return 1.0 / (1.0 + np.exp(-weighted_input))

    def backward(self, output):
        # return output * (1 - output)
        return np.multiply(output, (1 - output))  # 对应元素相乘

# tanh激活器
class TanhActivator(object):
    def forward(self, weighted_input):
        return 2.0 / (1.0 + np.exp(-2 * weighted_input)) - 1.0

    def backward(self, output):
        return 1 - output * output

# # softmax激活器
# class SoftmaxActivator(object):
#     def forward(self, weighted_input):  # 前向计算，计算输出
#         return max(0, weighted_input)
#
#     def backward(self, output):  # 后向计算，计算导数
#         return 1 if output > 0 else 0
