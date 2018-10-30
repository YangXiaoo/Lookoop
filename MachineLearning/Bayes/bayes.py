# coding:UTF-8
# 2018-10-29
# naive bayes
# 机器学习实战

import numpy as np 

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    # 1 is abusive, 0 not
    return postingList,classVec


def createVocabList(data):
	"""
	创建数据集合
	"""
	voc = set([])
	for v in data:
		voc = voc | set(v) # | 并集操作
	return list(voc)


def setOfWords2Vec(voc_list, inputs_set):
	"""
	创建词汇属于abusive的标签
	"""
	vec = [0] * len(voc_list) # [0 for _ in range(len(voc_list))]
	for w in inputs_set:
		if w in voc_list:
			vec[voc_list.index(w)] = 1
		else:
			pass
	return vec 


def trainNB(train_data, train_labels):
	"""
	利用贝叶斯得到各个词汇是abusive的概率
	"""
	# print(train_data, train_labels)
	m, n = len(train_data), len(train_data[0])
	p_abusive = sum(train_labels) / float(m) # abusive概率
	p_is_abusive = np.ones(n)
	p_not_abusive = np.ones(n)
	p_is_denom = 2.0 # abusive分母
	p_not_denom = 2.0 # not abusive 分母
	for i in range(m):
		# print(train_labels[i])
		if train_labels[i] == 1:
			p_is_abusive += train_data[i]
			p_is_denom += sum(train_data)
		else:
			p_not_abusive += train_data[i]
			p_not_denom += sum(train_data)
	p_is_vec = np.log(p_is_abusive/p_is_denom)
	p_not_vec = np.log(p_not_abusive/p_not_denom)

	return p_not_vec, p_is_vec, p_abusive


def classifyNB(in_vec, p_not_abusive, p_is_abusive, p_class):
	"""
	根据概率大小分类
	"""
	p1 = np.sum(in_vec * p_is_abusive) + np.log(p_class)
	p0 = np.sum(in_vec * p_not_abusive) + np.log(1 - p_class)
	if p1 > p0:
		return 1 # abusive
	else:
		return 0


def testingNB(train_data, train_labels, test_data):
	"""
	train_data: 训练数据
	train_labels: 训练标签
	test_data: 测试数据
	"""
	my_voc_list = createVocabList(train_data)
	train_mat = []
	for v in train_data:
		train_mat.append(setOfWords2Vec(my_voc_list, v))
	# print(train_mat)
	p_0, p_1, p_a = trainNB(np.array(train_mat), np.array(train_labels))

	this_doc = np.array(setOfWords2Vec(my_voc_list, test_data))
	this_class = classifyNB(this_doc, p_0, p_1, p_a)
	print(test_data, " classified as :", this_class)



if __name__ == '__main__':
	# 简单测试
	train_data, train_labels = loadDataSet()
	test_data_1 = ['love', 'my', 'dalmation']
	test_data_2 = ['stupid','garbage']
	testingNB(train_data, train_labels, test_data_1)
	testingNB(train_data, train_labels, test_data_2)


