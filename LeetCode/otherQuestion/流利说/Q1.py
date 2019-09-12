# coding:utf-8
"""
第一行 n 用户需要送礼物
第二行 甲地有a个礼物，乙地有b个礼物
接下来的n行表示甲与乙送礼物给用户i的花费
求最少花费

输入：
3
1 2
13 19
4 9
10 20

输出：
38

"""
import sys

def solver(n, a, b, cost):
	minCost = 0
	for c in cost:
		minCost += sum(c)

	que = [[a, b, n]] # [甲地剩余货物，乙地剩余货物，还需要送n个用户]
	while len(que) != 0:
		curSize = len(que)
		tmp = []
		for i in range(curSize):
			cur = que.pop()
			for 