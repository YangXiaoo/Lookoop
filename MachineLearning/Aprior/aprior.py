# coding:UTF-8
# 2018-10-31
# Aprior
# 机器学习实战

import numpy as np 


def loadData():
	"""
	加载测试数据
	"""
	return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createDic(data):
	"""
	列表生成集合
	"""
	data_set = []
	for k in data:
		for v in k:
			if [v] not in data_set:
				data_set.append([v])
	data_set.sort()
	return map(frozenset, data_set)


def scanData(data, data_set, min_support):
	"""
	data:训练集[[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
	data_set:训练集的集合[[1], [2], [3], [4], [5]]
	min_support: 最小支持度
	"""
	dic = {}
	for d in data:
		print(d)
		for can in data_set:
			print(can)
			if can.issubset(d):
				if not dic.get(can): 
					dic[can] = 1
				else:
					dic[can] += 1
		print(can)
	# 计算每个数据的支持度，过滤
	items_count = float(len(data))
	ret, support_data = [], {}
	print(dic)
	for key in dic:
		support = dic[key] / items_count
		if support >= min_support:
			ret.insert(0, key)
		support_data[key] = support
	print(ret, support_data)
	return ret, support_data


def apriorGen(data, k):
	"""
	组合生成新的数据
	data：数据
	k:k>=2
	"""
	ret = []
	len_data = len(data)
	for i in range(len_data):
		for j in range(i + 1, len_data):
			l_1 = data[i][:k - 2].sort()
			l_2 = data[j][:k - 2].sort()
			if l_1 == l_2:
				ret.append(data[i] | data[j]) # 合并
	print(ret)
	return ret 


def aprior(data, min_support=0.5):
	"""
	构建频繁项列表
	算法：
	当集合中的个数大于0时：
		构建一个k个项组成的候选项集合李彪
		检查数据以确认每个项集都是频繁的
		保留频繁项集并构建k+1项组成的候选项集列表
	"""
	data_set = createDic(data)
	new_data = []
	for i in data:
		if i not in new_data:
			new_data.append(i)
	data = new_data
	print(data)
	sub_data, support_data = scanData(data, data_set, min_support)
	ret = [sub_data] # 存储频繁项集合
	k = 2
	while len(ret[k - 2]) > 0:
		new_data_set = apriorGen(ret[k - 2], k)
		data_new, support_new = scanData(data, new_data_set, min_support)
		support_data.update(support_new)
		ret.append(data_new)
		k += 1
	print(ret, support_data)
	return ret, support_data


def generateRules(lists, support_data, min_conf=0.7):
	"""
	"""
	ret = [] # 存储关联项
	# 只对两个或以上的元素进行关联
	for i in range(1, len(lists)):
		for items in lists[i]:
			if i > 1:
				# 超过两个元素
				rulesFromConseq(lists, items, support_data, ret, min_conf)
			else:
				# 只有两个元素时直接计算可信度
				calcConf(lists, items, support_data, ret, min_conf)
	return ret 


def calcConf(lists, items, support_data, rules, min_conf):
	"""
	计算可信度
	"""
	ret = []
	for item in items:
		conf = support_data[lists] / support_data[lists - item]
		if conf >= min_conf:
			print(lists - item, '-->', item, 'conf:', conf)
			rules.append((lists - item, item, conf))
			ret.append(item)
	return ret 


def rulesFromConseq(lists, items, support_data, rules, min_conf):
	m = len(items[0]) + 1
	if len(lists) > m:
		data_set = apriorGen(items, m)
		data_new = calcConf(lists, data_set, support_data, rules, min_conf)
		if len(data_new) > 1:
			rulesFromConseq(lists, data_new, support_data, min_conf)


if __name__ == '__main__':
	data = loadData()
	print("data: ", data)
	lists, support_data = aprior(data, min_support=0.5)
	rules = generateRules(lists, support_data, min_conf=0.5)
	print(rules)


