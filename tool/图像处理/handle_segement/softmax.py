# 2018-9-30
# Softmax Regression
# python 机器学习算法
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from api import loadData, handleHistogram, loadWeights


def train(feature, label, k, max_iteration, alpha):
    """
    梯度下降法
    """
    m, n = np.shape(feature)
    weights = np.mat(np.ones((n, k))) # n x k
    i = 0
    end, pre, gap = 0.0001, 1e5, 1
    while i <= max_iteration and gap > end:
        y = np.exp(feature * weights) # m x k
        if i % 500 == 0:
            error_rate = cost(y, label)
            gap = abs(error_rate - pre)
            pre = error_rate
            print("iteration: %d, error rate: %.10f, gap: %.10f" % (i, error_rate, gap))
        row_sum = -y.sum(axis=1) # 按行相加 m x 1         
        row_sum = row_sum.repeat(k, axis=1) # 每个样本都需要除以总值， 所以转换为 m x k
        y = y / row_sum # 得到-P(y|x,w)
        for x in range(m):
            y[x, label[x, 0]]  += 1

        weights = weights + (alpha / m) * feature.T * y
        i += 1
    return weights


def cost(err, label_data):
    '''
    计算损失函数值
    input:  err(mat):exp的值
            label_data(mat):标签的值
    output: sum_cost / m(float):损失函数的值
    '''
    m = np.shape(err)[0]
    sum_cost = 0.0
    for i in range(m):
        if err[i, label_data[i, 0]] / np.sum(err[i, :]) > 0:
            sum_cost -= np.log(err[i, label_data[i, 0]] / np.sum(err[i, :]))
        else:
            sum_cost -= 0
    return sum_cost / m


def load_data(num, m):
    '''
    导入测试数据
    input:  num(int)生成的测试样本的个数
            m(int)样本的维数
    output: testDataSet(mat)生成测试样本
    '''
    testDataSet = np.mat(np.ones((num, m)))
    for i in range(num):
        testDataSet[i, 1] = rd.random() * 6 - 3#随机生成[-3,3]之间的随机数
        testDataSet[i, 2] = rd.random() * 15#随机生成[0,15]之间是的随机数
    return testDataSet


def predict(test_data, weights):
    '''
    利用训练好的Softmax模型对测试数据进行预测
    input:  test_data(mat)测试数据的特征
            weights(mat)模型的权重
    output: h.argmax(axis=1)所属的类别
    '''
    h = test_data * weights
    print(h)
    return h.argmax(axis=1) # 获得最大索引位置即标签


def saveModel(file_name, weights):
    '''
    保存最终的模型
    input:  file_name(string):保存的文件名
            weights(mat):softmax模型
    '''
    f_w = open(file_name, "w")
    m, n = np.shape(weights)
    for i in range(m):
        w_tmp = []
        for j in range(n):
            w_tmp.append(str(weights[i, j]))
        f_w.write("\t".join(w_tmp) + "\n")
    f_w.close()



if __name__ == "__main__":
    inputfile = "data.txt"
    # 1、导入训练数据
    feature, label = loadData(inputfile)
    feature = handleHistogram(feature)
    print(np.shape(feature), np.shape(label))
    #print(feature)
    k = 256
    # 2、训练Softmax模型
    weights = train(feature, label, k, 200000, 0.1)
    # print(weights)
    # saveModel("weights.txt", weights)
    # np.save("weights.npy", weights)
    # 3. 预测   
    # weights = np.load("weights.npy")
    # weights = loadWeights("weights.txt")
    print(weights)
    actual_x = [] # 绘制直线的x轴坐标
    predict_x = [] # 绘制预测值的x坐标
    for i in label:
        actual_x.append(int(i[0]))
        predict_x.append(i[0])
    actual_y = actual_x # 直线的y坐标

    # 得到预测值
    predition = predict(feature, weights)
    m, n = np.shape(predition)
    error = np.mat(np.zeros((m)))
    predict_y = [] # 预测值的y坐标
    for i in predition:
        predict_y.append(i[0])
    color = np.arctan2(predict_y, predict_x)
    # 绘制散点图
    plt.scatter(predict_x, predict_y, s = 10, c = "k", alpha = 1)
    # 设置坐标轴范围
    plt.xlim([0, 150])
    plt.ylim([0, 150])
    error[predict_y == actual_x] = 1
    print("correct rate:", np.sum(error)/m)
    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(actual_x, actual_y, c="k")
    plt.savefig("soft_max_iteration_200000")
    plt.show()
