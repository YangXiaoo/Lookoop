# coding:utf-8
# 并查集

"""
分为合并和查询两部分，管理一系列不相交的集合

背景：
给出某个亲戚关系图，求任意给出的两个人是否具有亲戚关系
规定：如果x和y是亲戚，y和z是亲戚，那么x和z是亲戚。
输入：三个整数n,m,p表示n个人，m个亲戚关系, 询问p对亲戚关系
"""

fa = []
rank = [] # 按秩合并

def init(n):
	"""初始化关系"""
	global fa, rank
	fa = [i for i in range(n+1)]
	rank = [1 for _ in range(n+1)]

def find(x):
	"""找到x的父元素"""
	if x == fa[x]:
		return x
	else:
		fa[x] = find(fa[x])
		return fa[x]

def merge(i, j):
	"""合并"""
	x, y = find(i), find(j)
	if rank[x] <= rank[y]:
		fa[x] = y
	else:
		fa[y] = x

	if rank[x] == rank[y] and x != y:
		rank[y] += 1

def main():
	global fa, rank
	n = 7
	rela = [[1,2], [3,4], [2, 3], [2, 7], [4, 7], [5, 6]]
	query = [[1,3], [2, 4], [3, 6], [1, 5]]

	init(n)
	for (x, y) in rela:
		merge(x, y)

	for (x, y) in query:
		if find(x) == find(y):
			print("x: {}, y: {} is relative".format(x, y))
		else:
			print("x: {}, y: {} is not relative".format(x, y))

if __name__ == '__main__':
	main()


