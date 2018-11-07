# coding:UTF-8
# 2018-10-25
# https://blog.csdn.net/zchshhh/article/details/78215087

import numpy as np 
from regression import *
from threshed import loadData
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def handleHistogram(data):
    """
    对直方图进行数据归一化处理
    """
    m, n = np.shape(data)
    ret = data
    for i in range(m):
        total = np.sum(data[i, :])
        for j in range(n):
            ret[i, j] = ret[i, j] / total * 40000
    print(ret)
    return ret
def plotScatter(data, labels, w, lim, save_name):
    """
    绘制散点图; 横坐标真实值，纵坐标预测值
    data : 数据
    labels:标签
    w:mat 权重
    lim:[(), ()] x,y轴范围
    save_name: 散点图保存名称
    """
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
    print("loading data ...")
    feature, label = loadData("new_daaaa.txt")
    feature = handleHistogram(feature)
    # 训练
    print ("traing...")
    method = ""  # 选择的方法
    if method == "bfgs":  # 选择BFGS训练模型
        print("using BFGS...")
        w0 = bfgs(feature, label, 0.5, 50, 0.4, 0.55)
    elif method == "lbfgs":  # 选择L-BFGS训练模型
        print("using L-BFGS...")
        w0 = lbfgs(feature, label, 0.5, 50, m=20)
    else:  # 使用最小二乘的方法
        print("using LMS...")
        w0 = ridgeRegression(feature, label, 0.5)
    print(w0)
    plotScatter(feature, label, w0, [(0,150), (0,150)], "dddd")


