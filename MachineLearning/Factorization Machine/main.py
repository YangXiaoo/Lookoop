# 2018-10-1 - 2018-10-2
# Factorization Machine
# python 机器学习算法
import numpy as np
from random import normalvariate
import matplotlib.pyplot as plt

def loadData(file_name):
    feature = []
    label = []
    f = open(file_name)
    for line in f.readlines():
        line = line.strip().split("\t")
        feature_tmp = []
        for i in line[:-1]:
            feature_tmp.append(float(i))
        feature.append(feature_tmp)
        label.append(float(line[-1]) * 2 - 1)
    f.close()
    return feature, label

def sig(x):
    return 1.0 / (1 + np.exp(-x))

def initializeV(n, k):
    """
    初始交叉项系数
    """
    v = np.mat(np.zeros((n, k))) # n x k
    for i in range(n):
        for j in range(k):
            v[i, j] = normalvariate(0, 0.2) # 正态分布初始每一个权重
    return v

def train(feature, label, k, max_iteration, alpha):
    """
    训练
    k: 因子分解机FM算法的度
    """
    m, n = np.shape(feature)
    w = np.zeros((n, 1)) # n x 1
    w0 = 0
    v = initializeV(n, k) # n x k

    for it in range(max_iteration): # while i < max_iteration:
        for x in range(m):
            inter_1 = feature[x] * v # 1 x n  x  n x k --> 1 x k
            inter_2 = np.multiply(feature[x], feature[x]) * np.multiply(v, v) # 1 x n  x  n x k --> 1 x k
            interaction = np.sum(np.multiply(inter_1, inter_1) - inter_2) / 2.0

            p = w0 + feature[x] * w + interaction
            loss = sig(label[x] * p[0, 0]) - 1 # P43 # sig() - 1

            w0 = w0 - alpha * loss * label[x]
            for i in range(n):
                if feature[x, i] != 0:
                    w[i, 0] = w[i, 0] - alpha * loss * label[x] * feature[x, i]
                    # 对于f-{1, ..., k}
                    for j in range(k):
                        v[i, j] = v[i, j] - alpha * loss * label[x] * \
                        (feature[x, i] * inter_1[0, j] -\
                          v[i, j] * feature[x, i] * feature[x, i])

        if it % 1000 == 0:
            loss = getCost(getPredict(np.mat(feature), w0, w, v), label)
            print("iteration: %d, loss: %.10f" % (it, loss))
    return w0, w, v


def getCost(predict, label):
    m = len(predict)
    error = 0.0
    for i in range(m):
        error -= np.log(sig(predict[i] * label[i]))
    return error / m


def getPredict(feature, w0, w, v):
    m = np.shape(feature)[0]
    result = []
    for x in range(m):
        inter_1 = feature[x] * v # 1 x n  x  n x k --> 1 x k
        inter_2 = np.multiply(feature[x], feature[x]) * np.multiply(v, v) # 1 x n  x  n x k --> 1 x k
        interaction = np.sum(np.multiply(inter_1, inter_1) - inter_2) / 2.0

        p = w0 + feature[x] * w + interaction
        prediction = sig(p[0, 0])
        result.append(prediction)

    return result

def getAccurancy(predict, label):
    m = len(predict)
    print(m)
    error = 0
    for i in range(m):
        if float(predict[i]) < 0.5 and label[i] == 1:
            error += 1
        elif float(predict[i]) >= 0.5 and label[i] == -1:
            error += 1
        else:
            continue
    return 1 - float(error) / m


if __name__ == '__main__':
    data_file = "data.txt"
    feature, label = loadData(data_file)
    w0, w, v = train(np.mat(feature), label, 3, 5000, 0.001)
    predict_result = getPredict(np.mat(feature), w0, w, v)
    accurancy = getAccurancy(predict_result, label)
    print("Accurancy: %.5f" % accurancy)
