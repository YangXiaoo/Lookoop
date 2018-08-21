# 2018-8-21
# 拓扑排序
# 算法导论 P335

# 数据结构与算法分析 P219

class Vertex(object):
	def __init__(self, name=None, degree=None, p=[], c=[]):
		self.name = name
		self.degree = degree # 入度
		self.p = None # 前驱
		self.c = None
		self.sortNum = None


def topSort(G):
	"""
	使用BFS实现拓扑排序。
	每次找到入度为0的节点放入列队，遍历与入度为0的点相邻的节点，并将度数减少1，如果度数变为0则放入列队。直到列队为空。
	"""
	Q = [] # 列队存储每个节点
	counter = 0
	sort = {}

	for i in G:
		if i.degree == 0:
			Q.append(i)

	while len(Q) != 0:
		vertex = Q.pop()
		sort[vertex] = counter
		counter += 1

		if vertex.c == None:
			continue

		for j in vertex.c :
			j.degree -= 1
			if j.degree == 0:
				Q.append(j)

	if len(sort) != len(G):
		print("Graph has a cycle!")
		return None

	return sort


def test():
	# 数据结构与算法分析 P218 图9-4
	# 实例图
	v1 = Vertex(name="v1",degree=0)
	v2 = Vertex(name="v2",degree=1)
	v3 = Vertex(name="v3",degree=2)
	v4 = Vertex(name="v4",degree=3)
	v5 = Vertex(name="v5",degree=1)
	v6 = Vertex(name="v6",degree=3)
	v7 = Vertex(name="v7",degree=2)

	v1.c = [v2,v3,v4]
	v2.p = [v1]
	v2.c = [v4,v5]
	v3.p = [v1,v4]
	v3.c = [v6]
	v4.p = [v1,v2,v5]
	v4.c = [v3,v6,v7]
	v5.p = [v2]
	v5.c = [v4,v7]
	v6.p = [v3,v4,v7]
	v7.p = [v4,v5]
	v7.c = [v6]
	G = [v1,v2,v3,v4,v5,v6,v7]

	test = topSort(G)

	for i in test:
		print(i.name)

if __name__ == "__main__":
	test()


"""
v1
v2
v5
v4
v7
v3
v6

符合  数据结构与算法分析 P219 图9-6 结果
"""