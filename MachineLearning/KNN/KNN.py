# coding:UTF-8
# 2018-10-28 ~ 2018-10-29
# 机器学习实战

# 参考链接
# https://www.cnblogs.com/netuml/p/5721251.html

# from numpy import *
import math
import numpy as np

def eulerDistance(vecA, vecB):
    """
    计算欧式距离
    """
    dist = (vecA - vecB) * (vecA - vecB).T
    return math.sqrt(dist)


def classify(in_x, data, labels, k):
	"""
	in_x : 用于分类的输入向量
	data : 数据集,矩阵形式
	labeles : 标签，数组形式即可
	k ： 分类数量
	"""
	in_x = np.mat(in_x)
	m, n = np.shape(data)
	distances = np.mat(np.zeros((1, m)))
	for i in range(m):
		distances[0, i] = eulerDistance(in_x, data[i])
	sorted_dist_index = distances.argsort() # 排序，结果为索引
	# print(sorted_dist_index, distances)
	class_count = {}
	for i in range(k):
		tmp_label = labels[sorted_dist_index[0, i]] # 排序后数据对应的标签
		class_count[tmp_label] = class_count.get(tmp_label, 0) + 1
	sorted_class_count = sorted(class_count.items(), key=lambda x:x[1], reverse=True)
	return sorted_class_count[0][0]



if __name__ == '__main__':
	# 简单测试
	data = np.mat([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	res = classify([0, 0], data, labels, 3)
	print(res) # B