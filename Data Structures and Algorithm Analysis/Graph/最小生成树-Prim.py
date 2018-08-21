# 2018-8-21
# 最小上生成树
# Prim算法

# 算法导论 P368
# 数据结构与算法分析 P237

def prim(G, w, r):
	"""
	从根节点开始，如果相邻节点使得路程减少则链接起来
	"""
	for u in G.v:
		u.key = INF
		u.p = None
	r.key = 0
	Q = G.V
	while len(Q) != None:
		u = extractMin(Q)
		for v in u.adj:
			if v in Q and w(u, v) < v.key:
				v.p = u
				v.key = w(u,v)