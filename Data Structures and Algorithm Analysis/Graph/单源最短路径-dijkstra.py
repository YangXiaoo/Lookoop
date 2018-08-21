# 2018-8-21
# 单源最短路径
# Dijkstra算法

# 算法导论 P383
# 数据结构与算法分析 P224

class graphNode(object):
	def __init__(self):
		self.known = False
		self.dist = INF
		self.p = None
		self.adj = []

def dijkstra(G):
	"""
	每次取出最小dist并且属性known为False的节点v，对v的邻节点进行松弛操作， 直到G中的known属性为False的节点为0。
	"""
	while len(G) != 0:
		v = smallestUnknownDist(G)
		v.known = True
		for w in v.adj:
			if w.known == False:
				relax(w, v)

def relax(w, v):
	"""
	松弛操作
	"""
	if v.dist + dist(w, v) < w.dist:
		w.dist = v.dist + dist(w, v)
		w.p = v 

def dist(w, v):
	"""
	返回 w 到 v 之间的距离
	"""
	pass



def smallestUnknownDist(G):
	"""
	返回图G中unknown且dist最小的节点
	"""
	pass