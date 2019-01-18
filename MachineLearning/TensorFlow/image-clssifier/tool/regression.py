# coding:utf-8
# 2019-1-16
# regression

import numpy as np
import random as rd

class softmax_classifier(object):
    def __init__(self, feature, label, k, max_iteration, alpha):
        self.feature = feature
        self.label = label
        self.k = k
        self.max_iteration = max_iteration
        self.alpha = alpha

    def train(self):
        m, n = np.shape(self.feature)
        weights = np.mat(np.ones((n, self.k))) # n x k
        i = 0
        end, pre, gap = 0.0001, 1e5, 1
        while i <= self.max_iteration and gap > end:
            y = np.exp(self.feature * weights) # m x k
            if i % 500 == 0:
                error_rate = self.cost(y, self.label)
                gap = abs(error_rate - pre)
                pre = error_rate
                print("iteration: %d, error rate: %.10f, gap: %.10f" % (i, error_rate, gap))
            row_sum = -y.sum(axis=1) # 按行相加 m x 1         
            row_sum = row_sum.repeat(self.k, axis=1) # 每个样本都需要除以总值， 所以转换为 m x k
            y = y / row_sum # 得到-P(y|x,w)
            for x in range(m):
                y[x, self.label[x, 0]]  += 1

            weights = weights + (self.alpha / m) * self.feature.T * y
            i += 1
        self.weights = weights

        return weights


    def cost(self, err, label_data):
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


    def predict(self, test_data, label):
        '''
        预测
        '''
        h = test_data * self.weights
        predictions = h.argmax(axis=1) # 获得最大索引位置即标签
        nums = max(label.shape)
        correct = np.array([h == predictions]) + 0

        print("accury: %.5f" % correct.sum() / nums)