# coding:UTF-8
# 2018-11-4
# 三个参数(均值， 方差， 最高值)
# 区域生长法

import numpy as np
import os
import cv2
import datetime
from threshed import loadData
from regression import *
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def getWeight(data, labels):
    """
    三个数据作为参数得到阈值
    """
    m, n = np.shape(data)
    print(m, n)
    # 重新清理数据
    new_data = []
    for i in range(m):
        mean_value = np.mean(data[i, :])
        cov = getCov(mean_value, data[i, :])
        max_value = np.max(data[i, :])
        new_data.append([mean_value, cov, max_value])

    new_data = np.mat(new_data)
    w = ridgeRegression(new_data, labels, 0.5)
    return w, new_data


def getCov(mean, data):
    """
    计算均方差
    """
    # print(mean, np.shape(data))
    data = np.mat(data[0])
    cov = 0
    m, n = np.shape(data)
    for i in range(m):
        for j in range(n):
            cov += float((data[i, j] - mean) * (data[i, j] - mean))
    cov = cov // (m * n)
    return cov


def plotScatter(data, labels, w, lim, save_name):
    actual_x = [] # 绘制直线的x轴坐标
    predict_x = [] # 绘制预测值的x坐标
    for i in labels:
        actual_x.append(int(i[0]))
        predict_x.append(i[0])
    actual_y = actual_x # 直线的y坐标

    # 得到预测值
    predition = data * w
    predict_y = [] # 预测值的y坐标
    for i in predition:
        predict_y.append(i[0])
    color = np.arctan2(predict_y, predict_x)
    # 绘制散点图
    plt.scatter(predict_x, predict_y, s = 10, c = color, alpha = 1)
    # 设置坐标轴范围
    plt.xlim(lim[0])
    plt.ylim(lim[1])

    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(actual_x, actual_y)
    plt.savefig(save_name)
    plt.show()


if __name__ == '__main__':
    data, labels = loadData("new_daaaa.txt")
    w, new_data = getWeight(data, labels)
    plotScatter(new_data, labels, w, [(0, 150), (0, 150)], 'sdd')
