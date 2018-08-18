# 2018-8-18
# van Emde Boas树
# 算法导论 P314
# C++ https://blog.csdn.net/coolsunxu/article/details/69487611
# ZKW线段树 http://wyfcyx.logdown.com/posts/201802-summary-data-structures-zkw-segment-tree-details

"""
1. 要存储的关键字值得全域(universe)集合为(0, 1, ..., u-1), u为全域的大小。
2. A[0,..u-1]存储一个值来自全域的动态集合，若值x属于动态集合，则元素A[x]为1，否则为0.
3. 每个内部结点为1当且仅当其子树中任一个叶子结点包含1.
"""

class vEBNode(object):
	def __init__(self):
		self.u = None
		self.min = None
		self.max = None
		self.summary = None
		self.cluster = []


class vEBtree(object):
	def __init__(self):
		self.V = vEBNode()

	def vEBMin(self, V):
		"""
		返回V中最小值
		"""
		return V.min

	def vEBMax(self, V):
		"""
		返回V中最大值
		"""
		return V.max


	





