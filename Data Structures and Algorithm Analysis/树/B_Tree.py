# 2018-8-10
# B-tree
# Reference
# Introduction to Algorithms [P174]
# python http://blog.51cto.com/thuhak/1269059
# https://blog.csdn.net/screaming/article/details/50932166
# C https://blog.csdn.net/xiaohusaier/article/details/76708490
# detail introduction: https://blog.csdn.net/endlu/article/details/51720299
# C++ ** https://blog.csdn.net/Ture010Love/article/details/6720855
# CSDN https://blog.csdn.net/guoziqing506/article/details/64122287
# https://www.cs.usfca.edu/~galles/visualization/BTree.html


class BTreeNode(object):
	def __init__(self, k=None, t):
		self.k = k
		self.childs = []
		self.keys = []
		self.degree = t

class BTree(object):
	def __init__(self):
		self.root = BTreeNode()
		self.isLeaf = False
		self.mind  =  MINDGREE
		self.maxd = MAXDGREE

	def insertKeystoTree(self, keys):
		for k in keys:
			self.insertKeytoTree(k)

	def insertKeytoTree(self, k):

