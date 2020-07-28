# coding:utf-8

"""
题目背景
某个局域网内有n(n<=100)台计算机，由于搭建局域网时工作人员的疏忽，现在局域网内的连接形成了回路，我们知道如果局域网形成回路那么数据将不停的在回路内传输，造成网络卡的现象。因为连接计算机的网线本身不同，所以有一些连线不是很畅通，我们用f(i,j)表示i,j之间连接的畅通程度，f(i,j)值越小表示i,j之间连接越通畅，f(i,j)为0表示i,j之间无网线连接。

题目描述
需要解决回路问题，我们将除去一些连线，使得网络中没有回路，并且被除去网线的Σf(i,j)最大，请求出这个最大值。

输入格式
第一行两个正整数n k

接下来的k行每行三个正整数i j m表示i,j两台计算机之间有网线联通，通畅程度为m。

输出格式
一个正整数，Σf(i,j)的最大值

输入输出样例
输入 #1 复制
5 5
1 2 8
1 3 1
1 5 3
2 4 5
3 4 2
输出 #1 复制
8
说明/提示
f(i,j)<=1000
"""

class Node():
	def __init__(self, u, v, w):
		self.u = u
		self.v = v 
		self.w = w

def getW(node):
	return node.w 

class Solution():
	def solver(self, n, k, edges):
		self.init(n)
		nodeNums = []
		total = 0
		for (u, v, w) in edges:
			node = Node(u, v, w)
			nodeNums.append(node)
			total += w

		# print(total)
		nodeNums.sort(key=getW)
		curLength = 0
		for node in nodeNums:
			# print(node.u, node.v, node.w)
			x, y = self.find(node.u), self.find(node.v)
			if x == y:	# 有相同的父节点即组成环
				continue
			self.merge(x, y)
			curLength += node.w 

		return total - curLength

	def init(self, n):
		self.fa = [i for i in range(n+1)]

	def find(self, x):
		if self.fa[x] == x:
			return x
		else:
			return self.find(self.fa[x])

	def merge(self, x, y):
		self.fa[x] = self.fa[y]


n, k = 5, 5
edges = [
	[1,2,8],
	[1,3,1],
	[1,5,3],
	[2,4,5],
	[3,4,2]
]

test = Solution()
ret = test.solver(n, k, edges)
print(ret)