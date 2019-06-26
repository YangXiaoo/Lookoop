# coding:utf-8
# 2019-6-26

"""
一个一维数轴上有不同的线段，求重复最长的两个线段

例如
a：1~3
b: 2~7
c：2~8
最长重复是b和c
"""
# 只测试了例子
class Node:
	def __init__(self, start, end):
		self.start = start
		self.end = end

def maxLengthLines(lists):
	sorted(lists, key=lambda node:node.start)	# 排序
	dp = [0 for _ in lists]
	
	maxEndIndex = 0	# 定义前一个最大尾结点线段所在索引
	ret = [0, 1]	# 声明返回结果
	preMax = max(dp)	# flag
	# print("preMax: {}, maxEndIndex: {}".format(preMax, maxEndIndex))

	for i in range(len(lists))[1:]:
		curNode = lists[i]

		# 找出当前节点之前最大尾节点所在索引与数值
		if lists[maxEndIndex].end < lists[i-1].end:
			maxEndIndex = i - 1
		maxEnd = lists[maxEndIndex].end

		if curNode.start >= maxEnd:	# 当前节点与之前节点无关
			dp[i] = dp[i-1]			# dp[i] = dp[i-1]
		else:						# 当前节点与之前索引为maxEndIndex的线段有关
			curLength = 0
			if maxEnd > curNode.end:
				curLength = curNode.end - curNode.start
			else:
				curLength = maxEnd - curNode.start
			dp[i] = max(dp[i-1], curLength)

		# 最大值判断
		if dp[i] > preMax:
			preMax = dp[i]
			ret = [maxEndIndex, i]

	return ret 

def test_maxLengthLines():
	lines = [[1, 3], [2, 7], [2, 8]]
	lists = []
	for line in lines:
		lists.append(Node(line[0], line[1]))
	ret = maxLengthLines(lists)
	print(ret)

if __name__ == '__main__':
	test_maxLengthLines()


