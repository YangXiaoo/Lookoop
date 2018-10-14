# coding:UTF-8
# 2018-10-14
# python 机器学习算法

import numpy as np 


class node(object):
    def __init__(self, fea = -1, value = None, results = None, right = None, left = None):
        self.fea = fea
        self.value = value
        self.results = results
        self.right = right
        self.left = left


def loadData(data_file):
    '''
    导入训练数据
    '''
    data = []
    f = open(data_file)
    for line in f.readlines():
        sample = []
        lines = line.strip().split("\t")
        for x in lines:
            sample.append(float(x))  # 转换成float格式
        data.append(sample)
    f.close()
    
    return data


def splitTree(data, fea, value):
    """
    根据value划分数据集
    fea: 划分数据集的索引
    """
    sub_1, sub_2 = [], []
    for i in data:
        if i[fea] >= value:
            sub_1.append(i)
        else:
            sub_2.append(i)

    return (sub_1, sub_2)



def leaf(data_set):
    """
    计算叶节点的值
    """
    data = np.mat(data_set)
    return np.mean(data[: , -1])


def errorCnt(data_set):
    """
    回归树的划分指标
    """
    data = np.mat(data_set)
    return np.var(data[:, -1]) * np.shape(data)[0]


def buildTree(data, min_sample, min_err):
    if len(data) <= min_sample:
        return node(results=leaf(data))

    best_error, best_criteria, best_set = errorCnt(data), None, None

    feature_num = len(data[0]) - 1
    for fea in range(feature_num):
        # 2.1 获得fea特征处所有的取值
        feature_values = {}
        for sample in data:
            feature_values[sample[fea]] = 1

        # 2.2 针对每一个可能的取值，尝试将数据集划分，并计算gini指数
        for value in feature_values.keys():
            # 根据数据中的value讲数据划分为左右子树
            (set_1, set_2) = splitTree(data, fea, value)
            if len(set_1) < 2 or len(set_2) < 2:
                continue

            # 计算划分后德 error值
            new_error = errorCnt(set_1) + errorCnt(set_2)

            # 判断新划分是否比旧划分好
            if new_error < best_error and len(set_1) > 0 and len(set_2) > 0:
                best_error = new_error
                best_criteria = (fea, value)
                best_set = (set_1, set_2)


    # 3. 判断是否结束
    if best_error > 0:
        right = buildTree(best_set[0], min_sample, min_err)
        left = buildTree(best_set[1], min_sample, min_err)
        return node(fea=best_criteria[0], value=best_criteria[1], right=right, left=left)
    else:
        return node(results=leaf(data))

def predict(sample, tree):
    if tree.results != None:
        return tree.results
    else:
        val_sample = sample[tree.fea]
        branch = None
        if val_sample >= tree.value:
            branch = tree.right
        else:
            branch = tree.left

        return predict(sample, branch)


def calError(data, tree):
    """
    计算误差
    """
    m = len(data)
    n = len(data[0]) - 1
    error = 0.0

    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(data[i][j])
        pre = predict(tmp, tree)

        error += (data[i][-1] - pre)**2

    return error / m 


if __name__ == "__main__":
    # 1、导入训练数据
    print("loading data...")
    data = loadData("sine.txt")
    # 2、构建CART树
    print("training...")
    regression_tree = buildTree(data, 30, 0.1)
    # 3、评估CART树
    print("caculating error...")
    err = calError(data, regression_tree)
    print ("error : ", err)