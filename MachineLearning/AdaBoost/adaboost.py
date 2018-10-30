# coding:UTF-8
# 2018-10-30
# AdaBoost(Adaptive boosting)
# 机器学习实战
# https://blog.csdn.net/gamer_gyt/article/details/51372309
import numpy as np

__equation = ['lt', 'gt']


def loadSimpData():
    """
    测试数据
    """
    datMat = np.mat([[ 1. ,  2.1],
        [ 2. ,  1.1],
        [ 1.3,  1. ],
        [ 1. ,  1. ],
        [ 2. ,  1. ]])
    classLabels = np.mat([1.0, 1.0, -1.0, -1.0, 1.0]).T
    return datMat,classLabels


def stumpClassify(data, fea_index, thresh_val, thresh_eq):
    """
    根据选定值与索引对数据进行分类
    """
    m = np.shape(data)[0]
    ret = np.ones((m, 1)) # m x 1
    if thresh_eq == 'lt':
        for i in range(m):
            if data[i, fea_index] <= thresh_val:
                ret[i, 0] = -1.0
    else:
        for i in range(m):
            # print(data[i], fea_index)
            if data[i, fea_index] > thresh_val:
                ret[i, 0] = -1.0
    return ret


def buildStump(data, labels, D, step):
    """
    data:数据集
    labels:标签
    D：数据集中每个样本的权重
    return:单层决策树(弱分类器)

    步骤：
    a. 将最小错误率设置为inf
    b. 对数据中的每一个特征
        c. 对每个步长
            d. 对每个不等号
                e. 建立一颗单层决策树并利用加权数据集对其进行测试,
                如果错误率低于最小错误率，则将当前单层树设置为最佳单层树
    f. 返回最佳单层决策树
    """
    m, n = np.shape(data)
    best_stump = {}
    # a. 将最小错误率设置为inf
    min_error = np.inf
    # b. 对数据中的每一个特征
    for i in range(n):
        # 计算步长大小
        range_min = data[:, i].min()
        range_max = data[:, i].max()
        step_size = (range_max - range_min) / float(step)
        # c. 对每个步长
        for j in range(-1, int(step) + 1):
            # d. 对每个不等号
            for inequal in __equation:
                thresh_val = range_min + float(j) * step_size
                # e. 建立一颗单层决策树并利用加权数据集对其进行测试,
                # 如果错误率低于最小错误率，则将当前单层树设置为最佳单层树
                prediction = stumpClassify(data, i, thresh_val, inequal)
                error = np.mat(np.ones((m, 1)))
                # 没有错的样本置为0
                for x in range(m):
                    if prediction[x, 0] == labels[x, 0]:
                        error[x, 0] = 0
                # 简写
                # error[prediction == labels] = 0
                weight_error = D.T * error # 计算权重的误差
                if weight_error < min_error:
                    min_error = weight_error
                    best_class_est = prediction.copy()
                    best_stump['fea'] = i # 最佳特征索引
                    best_stump['thresh'] = thresh_val
                    best_stump['ineq'] = inequal

    return best_stump, min_error, best_class_est


def adaBoostTrainDS(data, labels, max_iter=40):
    """
    data: 训练数据
    labels: 标签
    max_iter : 最大迭代次数

    算法步骤：
    a. 对每次迭代
        b. 利用buildStump找到最佳单层决策树
        c. 计算alpha
        d. 将最佳单层决策树加入到数组ret中
        e. 计算新的权重D
        f. 更新累计类别估计值
        g. 如果错误率为0，退出循环
    h. 返回数组ret
    """
    ret = []
    m = np.shape(data)[0] # 样本数量
    D = np.mat(np.ones((m, 1)) / m) # 初始化权重
    total_class_est = np.mat(np.zeros((m, 1))) # 累积类别估计值
    # a. 对每次迭代
    for i in range(max_iter):
        # b. 利用buildStump找到最佳单层决策树
        best_stump, error, class_est = buildStump(data, labels, D, 10)
        # c. 计算alpha
        alpha = float(0.5 * np.log((1 - error) / max(error, 1e-16))) #  max(error, 1e-16):防止溢出
        # d. 将最佳单层决策树加入到数组ret中
        best_stump['alpha'] = alpha
        ret.append(best_stump)
        # e. 计算新的权重D
        exp = np.exp(np.multiply(-1 * alpha * labels, class_est))
        D = np.multiply(D, exp)
        D = D / D.sum()
        # f. 更新累计类别估计值
        total_class_est += alpha * class_est
        # print(np.sign(total_class_est), labels)
        total_error = np.multiply((np.sign(total_class_est) != labels).T, np.ones((m, 1)))
        error_rate = total_error.sum() / m
        # g. 如果错误率为0，退出循环
        if error_rate == 0.0: break
    # h. 返回数组ret
    return ret, total_class_est


def adaClassify(data, classifier):
    """
    daat:需要分类的数据,矩阵形式
    classifier: 决策树数组
    """
    m = np.shape(data)[0]
    total_class_est = np.mat(np.zeros((m, 1)))
    for i in range(len(classifier)):
        # print(classifier[i])
        class_est = stumpClassify(data, \
                    classifier[i]['fea'], \
                    classifier[i]['thresh'], \
                    classifier[i]['ineq'])
        total_class_est += classifier[i]['alpha'] * class_est
        # print("error: ", total_class_est)
    return np.sign(total_class_est)


if __name__ == '__main__':
    data, labels = loadSimpData()
    # print(np.shape(data), np.shape(labels))
    classifier, _ = adaBoostTrainDS(data, labels)
    test_data = np.mat([[5, 5], [0, 0]])
    # print(classifier)
    res = adaClassify(test_data, classifier)
    print(res)

