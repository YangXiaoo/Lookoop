# 2018-10-20
# Personl Rank
# python 机器学习算法
import numpy as np

def loadData(file_path):
	'''
	导入用户商品数据
	'''
	f = open(file_path)
	data = []
	for line in f.readlines():
		lines = line.strip().split("\t")
		tmp = []
		for x in lines:
			if x != "-":
				tmp.append(1) # 打过分记为1
			else:
				tmp.append(0) # 未打分记为0
		data.append(tmp)
	f.close()
	return np.mat(data)


def generateDict(data):
	"""
	将用户-商品转换为二部图表示
	"""
	m, n = np.shape(data)
	data_dict = {}

	# 用户-商品
	for i in range(m):
		tmp = {}
		for j in range(n):
			if data[i, j] != 0:
				tmp["D_" + str(j)] = data[i, j]
		data_dict["U_" + str(i)] = tmp

	# 商品-用户
	for j in range(n):
		tmp = {}
		for i in range(m):
			if data[i, j] != 0:
				tmp["U_" + str(i)] = data[i, j]
		data_dict["D_" + str(j)] = tmp

	return data_dict


def PersonalRank(data_dict, alpha, user, max_iter):
	"""
	使用Personal Rank 算法
	a. 初始化rank
	b. 在图上游走，每次选择rank不为0的节点开始，沿着边往前的概率为alhpa,停在当前节点的概率为1-alpha
	c. 从第一个rank不为0的节点开始计算转移概率
	d. 判断是否停止否则转为b
	"""
	# a. 初始化
	rank = {}
	for x in data_dict.keys():
		rank[x] = 0
	rank[user] = 1

	# 进行迭代
	it = 0
	while it < max_iter:
		tmp = {}
		for x in data_dict:
			tmp[x] = 0

		for i,v in data_dict.items():
			for j in v.keys():
				if j not in tmp:
					tmp[j] = 0

				tmp[j] += alpha * rank[i] / (1.0 * len(v))
				if j == user:
					tmp[j] += (1 - alpha)

		check = []
		for k in tmp.keys():
			check.append(tmp[k] - rank[k])
		if sum(check) <= 0.0001:
			break

		rank = tmp
		if it % 10 == 0:
			print("iteration: ", it)

		it += 1
	return rank



def recommend(data_dict, rank, user):
	"""
	为用户推荐没有打过分数的商品
	"""
	items_dict = {}
	scored = []
	for x in data_dict[user].keys():
		scored.append(x)

	for k in rank.keys():
		if k.startswith("D_"):
			if k not in scored:
				items_dict[k] = rank[k]

	result = sorted(items_dict.items(), key=lambda d: d[1], reverse=True)

	return result


if __name__ == "__main__":
	# 1、导入用户商品矩阵
	print("loading data...")
	dataMat = loadData("data.txt")
	# 2、将用户商品矩阵转换成邻接表的存储
	print("generating dicts...")
	data_dict = generateDict(dataMat)
	# 3、利用PersonalRank计算
	print("training...")
	rank = PersonalRank(data_dict, 0.85, "U_0", 500)
	# 4、根据rank结果进行商品推荐
	print("recommend")
	result = recommend(data_dict, rank, "U_0")
	print( result)

