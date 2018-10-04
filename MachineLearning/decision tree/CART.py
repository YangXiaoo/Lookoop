# coding:UTF-8
# 2018-10-4 - 2018-10-5
# 决策树(CART)
# python 机器学习算法
# https://blog.csdn.net/gamer_gyt/article/details/51372309

class node(object):
	def __init__(self, fea = -1, value = None, results = None, right = None):
		self.fea = fea
		self.value = value
		self.results = results
		self.right = right
		self.left = left


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



def lableUniqueCount(data):
	"""
	统计数据集中不同标签的个数
	"""
	uniq = {}
	for i in data:
		label = i[-1]
		if label not in uniq:
			uniq[label] = 0
		uniq[label] += 1
	return uniq


def calcGiniIndex(data):
	total_sample = len(data)
	if len(data) == 0:
		return 0
	lable_counts = lableUniqueCount(data)

	gini = 0
	for label in lable_counts:
		gini += lable_counts[label]**2
	gini = 1 - float(gini) / (total_sample**2)

	return gini


def buildTree(data):
	if len(data) == 0:
		return node()

	# 1. 获得当前的基尼指数
	current_gini = calcGiniIndex(data)

	# 2. 划分
	best_gini, best_criteria, best_set = 0.0, None, None

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
			new_gini = float(len(set_1) * calcGiniIndex(set_1) + len(set_2) * calcGiniIndex(set_2)) / len(data)

			# 计算gini指数的增量
			gain = current_gini - new_gini

			# 判断新划分是否比旧划分好
			if gain > best_gini and len(set_1) > 0 and len(set_2) > 0:
				best_gini = gain
				best_criteria = (fea, value)
				best_set = (set_1, set_2)


	# 3. 判断是否结束
	if best_gini > 0:
		right = buildTree(best_set[0])
		left = buildTree(best_set[1])
		return node(fea=best_criteria[0], value=best_criteria[1], right=right, left=left)
	else:
		return node(results=lableUniqueCount(data))

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