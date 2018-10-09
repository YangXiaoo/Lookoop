# coding:UTF-8
# 2018-10-8
# 随机森林树
import numpy as np
import random as rd
from math import log 
from CART import buildTree, predict

def load_data(file_name):
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
	trees_result = []
	trees_feature = []	`