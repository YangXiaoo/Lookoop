# coding:UTF-8
# 2018-10-11
# Linear Regression

import numpy as np

def loadData(file_path):
    """
    导入数据
    """
    f = open(file_path)
    feature = []
    label = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        feature_tmp.append(1)  # x0
        for i in range(len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        feature.append(feature_tmp)
        label.append(float(lines[-1]))
    f.close()
    return np.mat(feature), np.mat(label).T 


def leastSquare(feature, label):
    """
    基于矩阵表示的最小二乘法
    feature : m x n
    label : n x 1
    """
    w = (feature.T * feature).I * feature.T * label # n x 1
    return w

def firstDerivative(feature, label, w):
    """
    损失函数的一阶导数
    """
    m, n = np.shape(feature)
    g = np.mat(np.zeros((n, 1)))

    for i in range(m):
        error = label[i, 0] - feature[i, ] * w # feature[i, ] * w : 1 x n  x  n x 1
        for j in range(n):
            g[j, ] -= error * feature[i, j]

    return g

def secondDerivative(feature):
    m, n = np.shape(feature)
    G = np.mat(np.zeros((n, n)))
    for i in range(m):
        x_1 = feature[i, ].T
        x_2 = feature[i, ]
        G += x_1 * x_2
    return G


def getError(feature, label, w):
    """
    计算损失函数的值
    """
    loss = (label - feature * w).T * (label - feature * w) / 2
    return loss


def getMin(feature, label, sigma, delta, d, w, g):
    """
    Armijo搜索准则
    """
    m = 0
    while True:
        w_new = w + (sigma**m) * d
        left = getError(feature, label, w_new)
        right = getError(feature, label, w) + delta * (sigma**m) * g.T * d
        if left <= right:
            break
        else:
            m += 1
    return m

def newton(feature, label, max_iter, sigma, delta):
    n = np.shape(feature)[1]
    w = np.mat(np.zeros((n, 1)))

    it = 0
    while it <= max_iter:
        g = firstDerivative(feature, label, w)
        G = secondDerivative(feature)
        d = - G.I * g
        m = getMin(feature, label, sigma, delta, d, w, g)
        w = w + (sigma**m) * d 
        if it % 10 == 0:
            print("Iteration: ", it, "loss: ", getError(feature, label, w))
        it += 1
    return w


if __name__ == "__main__":
    # 1、导入数据集
    print("loading data...")
    feature, label = loadData("data.txt")
    # 2.1、最小二乘求解
    print("training...")
    # print "\t ---------- least_square ----------"
    # w_ls = least_square(feature, label)
    # 2.2、牛顿法
    print("newton...")
    w_newton = newton(feature, label, 50, 0.1, 0.5)
    print(w_newton)
    # # 3、保存最终的结果
    # print "----------- 3.save result ----------"
    # save_model("weights", w_newton)