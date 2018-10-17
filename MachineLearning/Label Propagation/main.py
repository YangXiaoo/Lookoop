# coding:UTF-8
# 2018-10-17
# Label Progation

import string

def loadData(file_path):
	"""
	读取数据生成无向树
	"""
	f = open(file_path)
	vector_dict = {}
	edge_dict = {}

	for line in f.readlines():
		lines = line.strip().split("\t")

		for i in range(2):
			if lines[i] not in vector_dict:
				# 将节点放在vector_dict中, 设置社区属性为自己
				vector_dict[lines[i]] = string.atoi(lines[i])
				# 边
				edge = []
				edge.append(lines[1 - i] + ":" + "1")
				edge_dict[lines[i]] = edge
			else:
				edge = edge_dict[lines[i]]
				edge.append(lines[1 - i] + ":" + "1")
				edge_dict[lines[i]] = edge

	f.close()

	return vector_dict, edge_dict

def getMaxCommunityLabel(vector_dict, adjacent):
	"""
	得到相邻节点中标签数最多的标签
	"""
	label_dict = {}
	for node in adjacent:
		node_data = node.strip().split(":")
		node_id = node_data[0]
		node_weight = string.atoi(node_data[1])
		if vector_dict[node_id] not in label_dict:
			label_dict[vector_dict[node_id]] = node_weight
		else:
			label_dict[vector_dict[node_id]] += node_weight

	sort_label = sorted(label_dict.items(), key=lambda d:d[1], reverse=True)

	# print(sort_label)
	return sort_label[0][0]


def Finish(vector_dict, edge_dict):
	"""
	检查是否满足终止条件
	"""
	for node in vector_dict.keys():
		adjacent = edge_dict[node]
		node_label = vector_dict[node] # 与node相连接的节点
		label = getMaxCommunityLabel(vector_dict, adjacent)
		if node_label == label:
			continue
		else:
			return False
	return True


def labelPropagation(vector_dict, edge_dict):
	"""
	标签传播
	"""
	it = 1
	while True:
		if not Finish(vector_dict, edge_dict):
			print("iteration: ", it)
			for node in vector_dict.keys():
				adjacent = edge_dict[node]
				vector_dict[node] = getMaxCommunityLabel(vector_dict, adjacent)
		else:
			break
	return vector_dict


if __name__ == '__main__':
	print("loading data...")
	file_path = "data.txt"
	vector_dict, edge_dict = loadData(file_path)
	print(vector_dict)
	print(edge_dict)
	print("training...")
	vec = labelPropagation(vector_dict, edge_dict)
	print(vec)
