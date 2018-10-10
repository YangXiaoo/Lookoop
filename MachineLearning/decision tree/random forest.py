# coding:UTF-8
# 2018-10-8
# 随机森林树
import numpy as np
import random as rd
from math import log 
from CART import buildTree, predict

def loadData(file_name):
    '''导入数据
    input:  file_name(string):训练数据保存的文件名
    output: data_train(list):训练数据
    '''
    data_train = []
    f = open(file_name)
    for line in f.readlines():
        lines = line.strip().split("\t")
        data_tmp = []
        for x in lines:
            data_tmp.append(float(x))
        data_train.append(data_tmp)
    f.close()
    return data_train


def chooseSample(data, k):
	"""
	随机选取样本, 标签随机，数据随机
	data: 数据集
	k: 随机选取k个特征
	"""
	m, n = np.shape(data)

	# 特征标签索引
	feature_index = []
	for i in range(k):
		feature_index.append(rd.randint(0, n - 2))


	# 数据索引
	data_index = []
	for i in range(m):
		data_index.append(rd.randint(0, m - 1))

	data_sample = []
	for i in range(m):
		data_tmp = []
		for j in feature_index:
			data_tmp.append(data[data_index[i]][j])
		data_tmp.append(data[data_index[i]][-1]) # 标签
		data_sample.append(data_tmp)

	return data_sample, feature_index


def randomForestTraining(data_train, trees_num):
	"""
	trees_num: 分类树的个数
	data_train: 训练数据集
	"""
	trees_result = []
	trees_feature = []

	# 
	n = np.shape(data_train)[1]
	if n > 2:
		k = int(log(n - 1, 2)) + 1
	else:
		k = 1

	# 构建树
	for i in range(trees_num):
		data_sample, feature = chooseSample(data_train, k)
		tree = buildTree(data_sample)
		trees_result.append(tree)
		trees_feature.append(feature)

	return trees_result, trees_feature


def splitData(data_train, feature):
	"""
	根据feature提取数据
	"""
	m = np.shape(data_train)[0]
	data = []

	for i in range(m):
		data_tmp = []
		for j in feature:
			data_tmp.append(data_train[i][j])
		data_tmp.append(data_train[i][-1])
		data.append(data_tmp)

	return data


def getPredict(trees_result, trees_feature, data_train):
	"""
	预测
	"""
	tree_len = len(trees_result)
	m = np.shape(data_train)[0]

	result = []
	for i in range(tree_len):
		tree = trees_result[i]
		feature = trees_feature[i]
		data = splitData(data_train, feature)
		result_tmp = []
		for j in range(m):
			result_tmp.append(list(((predict(data[i][:], tree)).keys()))[0])
		result.append(result_tmp)
	return np.sum(result, axis=0)


def calCorrectRate(data_train, final_predict):
	m = len(final_predict)
	correct = 0
	for i in range(m):
		if data_train[i][-1] * final_predict[i] > 0:
			correct += 1
	return correct / m


if __name__ == "__main__":
    # 1、导入数据
    data_train = loadData("data.txt")
    # 2、训练random_forest模型
    print("train...")
    trees_result, trees_feature = randomForestTraining(data_train, 50)
    # 3、得到训练的准确性
    print("test...")
    result = getPredict(trees_result, trees_feature, data_train)
    corr_rate = calCorrectRate(data_train, result)
    print("correct rate: ", corr_rate)
    # # 4、保存最终的随机森林模型
    # save_model(trees_result, trees_feature, "result_file", "feature_file")