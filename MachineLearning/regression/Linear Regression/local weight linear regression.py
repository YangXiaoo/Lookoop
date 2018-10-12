# coding:UTF-8
# 2018-10-11
# local Weight Linear Regression

import numpy as np
from newton import loadData

def LWLR(feature, label, k):
    """
    局部加权线性回归
    """
    m = np.shape(feature)[0]
    predict = np.zeros(m)

    weights = np.mat(np.eye(m))
    for i in range(m):
        for j in range(m):
            diff = feature[i, ] - feature[j, ]
            weights[j, j] = np.exp(diff * diff.T / (-2.0 * k**2))
        xwx = feature.T * (weights * feature)
        w = xwx.I * (feature.T * (weights * label))
        predict[i] = feature[i, ] * w
    return predict


if __name__ == '__main__':
    feature, label = loadData("data.txt")
    predict = LWLR(feature, label, 0.002)
    m = np.shape(predict)[0]
    for i in range(m):
        print(feature[i, 1], predict[i])