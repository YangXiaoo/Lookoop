# 2018-8-7
# Red Black Tree

# Reference
# Introduction to Algorithms [P174]
# Data Structures and Algorithm Analysis in C [P351]
# https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
# C https://blog.csdn.net/weewqrer/article/details/51866488
# python https://blog.csdn.net/jacke121/article/details/78178597


"""
1. Each node is either red or black.
2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
3. All leaves (NIL) are black.
4. If a node is red, then both its children are black.
5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
"""

# Define red-black tree
class RedBlackNode(object):
	def __init__(self, X=None):
		self.value = X
		self.color = "Black"
		self.right = None
		self.left = None
		self.parent = None


class RedBlackTree(object):
	def __init__(self):
		self.root = RedBlackNode()
		self.nil = None
		self.root.left = self.nil
		self.root.right = self.nil
		self.root.parent = self.nil


	def treeMaximum(self, node):
		"""
		Find maximum leave of the node.
		:rtype: RedBlackNode
		"""
		tmp_node = node
		while tmp_node.right:
			tmp_node = tmp_node.right
		return tmp_node

	def treeMinimum(self, node):
		"""
		Find minimum leave of the node.
		:rtype: RedBlackNode
		"""
		tmp_node = node
		while tmp_node.right:
			tmp_node = tmp_node.right
		return tmp_node

	def redBackTransplant(self, u, v):
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		elif u == u.parent.right:
			u.parent.right = v

		if v:
			v.parent = u.parent

	def leftRotate(self, x):
		"""
				x
			   / \
			  a   y
			     / \
				b   r
		When we do a left rotation on a node x, we assume that its right child y is not T.nill;
		x may be any node in from x to y.It makes y the new root of subtree,with x as y's left child and y's left child as x's right child.
		Both leftRotate and rightRotate run in O(1) time.
		"""
