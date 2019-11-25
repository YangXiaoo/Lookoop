# coding:utf-8
import sys
sys.path.append("../../")

from util import io 

# 使用非线性最小二乘法拟合
from numpy.linalg import lstsq
import numpy as np

dataFilePath = "../../data/samples-data.data"
labelsFilePath = "../../data/samples-data-labels.data"
def getTrainData():
    """获取训练数据"""
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

X, Y = getTrainData()

def adapteData(X):
    """将数据变形为系数矩阵"""
    newData = []
    for data in X:
        x1 = data[0]
        x2 = data[1]
        x3 = data[2]
        x4 = data[3]
        x5 = data[4]
        tmp = [1, x1, x2, x3, x4, x5, x1*x2, x1*x3, x1*x4, x1*x5, x2*x3, x2*x4, x2*x5, x3*x4, x3*x5, x4*x5, x1**2, x2**2, x3**2, x4**2, x5**2]
        newData.append(tmp)
    newData = np.array(newData)

    return newData

newData = adapteData(X)
c = lstsq(newData, Y)[0]

diffValue = [X[0]] * c - Y[0]
print("[INFO] different value: {}".format(diffValue))

# c = newData / Y
# # print("[INFO] c : {}".format(c))

# diffValue = newData * c - Y
# print("[INFO] different value: {}".format(diffValue))
