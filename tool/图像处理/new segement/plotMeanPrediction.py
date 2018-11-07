# coding:UTF-8
# 2018-11-7
# 绘制像素均值-最佳阈值直方图

from api import loadData, getHistogramMean
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


if __name__ == '__main__':
    print("loading data ...")
    feature, label = loadData("new_data.txt")
    x, y = [], []
    m, n = np.shape(feature)
    for i in range(m):
    	mean = getHistogramMean(feature[i, :])
    	x.append(int(mean))
    	y.append(int(label[i, :]))
    print(x, y)
    color = np.arctan2(y, x)
    # 绘制散点图
    plt.scatter(x, y, s = 10, c = color, alpha = 1)
    # 设置坐标轴范围
    plt.xlim([0, 150])
    plt.ylim([0, 150])

    plt.xlabel("mean value")
    plt.ylabel("prediction")
    # plt.plot(actual_x, actual_y)
    plt.savefig("save_name")
    plt.show()
