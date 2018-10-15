# coding:UTF-8
# 2018-10-15
# k-means++
# python 机器学习算法

import numpy as np 
from random import random

def loadData(file_path):
    '''导入数据
    input:  file_path(string):文件的存储位置
    output: data(mat):数据
    '''
    f = open(file_path)
    data = []
    for line in f.readlines():
        row = []  # 记录每一行
        lines = line.strip().split("\t")
        for x in lines:
            row.append(float(x)) # 将文本中的特征转换成浮点数
        data.append(row)
    f.close()
    return np.mat(data)


def distance(vecA, vecB):
	"""
	计算两点的欧式距离
	"""
	dist = (vecA - vecB) * (vecA - vecB).T 
	return dist[0, 0]


def nearest(point, cluster_centers):
	"""
	计算point 与 closter_centers之间的最小距离
	"""
	min_dist = np.inf 
	m = np.shape(cluster_centers)[0]

	for i in range(m):
		d = distance(point, cluster_centers[i, :])
		if d < min_dist:
			min_dist = d
	return min_dist


def getCentriods(point, k):
	"""
	初始化聚类中心
	"""
	m, n = np.shape(point)
	cluster_centers = np.mat(np.zeros((k, n)))

	# 随机选择一个样本点作为第一个聚类
	index = np.random.randint(0, m)
	cluster_centers[0, :] = np.copy(point[index, :])

	# 初始化一个距离的序列
	d = [0.0 for _ in range(m)]

	for i in range(1, k):
		sum_all = 0
		for j in range(m):
			# 对每一个样本找到最近的聚类中心
			d[j] = nearest(point[j, :], cluster_centers[0:i, :])
			# 将所有的最短距离相加
			sum_all += d[j]
		sum_all *= random()

		# 获得距离最远的样本点作为聚类中心点
		for j, di in enumerate(d):
			sum_all -= di 
			if sum_all > 0:
				continue
			cluster_centers[i] = np.copy(point[j, :])
			break
	return cluster_centers





def kmeans(data, k, centriods):
	m, n = np.shape(data)
	sub_cent = np.mat(np.zeros((m, 2)))
	change = True
	while change:
		change = False

		# 计算每个样本到聚类中心的距离
		for i in range(m):
			min_dist = np.inf 
			min_index = 0
			for j in range(k):
				dist = distance(data[i, :], centriods[j, :])
				if dist < min_dist:
					min_dist = dist
					min_index = j 

			if sub_cent[i, 0] != min_index:
				change = True
				sub_cent[i, :] = np.mat([min_index, min_dist])

		# 重新计算中心
		for j in range(k):
			sum_all = np.mat(np.zeros((1, n)))
			r = 0
			for i in range(m):
				if sub_cent[i, 0] == j:
					sum_all += data[i, :]
					r += 1
			for c in range(n):
				try:
					centriods[j, c] = sum_all[0, c] / r 
				except:
					print("r is zero")
	return centriods, sub_cent

if __name__ == "__main__":
    k = 4  # 聚类中心的个数
    file_path = "data.txt"
    # 1、导入数据
    print("loading data...")
    data = loadData(file_path)
    # 2、随机初始化k个聚类中心  
    print("initialize centroids...")
    centroids = getCentriods(data, k)
    # 3、聚类计算  
    print("training...")
    subCenter, centroids = kmeans(data, k, centroids)  
    # result
    print("centroids: ", subCenter)
