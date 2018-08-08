# 2018-8-7 - 2018-8-
# Red Black Tree

# Reference
# Introduction to Algorithms [P174]
# Data Structures and Algorithm Analysis in C [P351]
# https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
# C https://blog.csdn.net/weewqrer/article/details/51866488
# python https://blog.csdn.net/jacke121/article/details/78178597
# Java https://www.cnblogs.com/KingIceMou/p/6984138.html


"""
1. Each node is either red or black.
2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
3. All leaves (NIL) are black.
4. If a node is red, then both its children are black.
5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
"""

# Global var
BLACK = "black"
RED = "red"

# Define red-black tree
class RedBlackNode(object):
	def __init__(self, X=None):
		self.key = X
		self.color = BLACK
		self.right = None
		self.left = None
		self.parent = None


class RedBlackTree(object):
	def __init__(self):
		"""
		Initialize a red-black tree.
		"""
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

	def Transplant(self, u, v):
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
		y = x.right
		x.right = y.left 
		if y.left != self.nil:
			y.left.parent = x

		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		elif x == x.parent.right:
			x.parent.right = y

		y.left = x
		x.parent = y

	def rightRotate(self, y):
		"""
				y
			   / \
			  x   r
		     / \
			a   b
		Same as leftRotate
		"""
		x = y.left

		y.left = x.right
		if x.right != self.nil:
			x.right.parent = y

		x.parent = y.parent
		if y.parent == self.nil:
			self.root = x
		elif y == y.parent.left:
			y.parent.left = x
		elif y == y.parent.right:
			y.parent.right = x

		x.right = y
		y.parent = x

	def insert(self, z):
		"""
		Insert a new node z, and color z red. 
		Because color z red may cause a violation of one of the red-black properties, we call "insertFix(z)" to restore the red-black properties.
		Insert a node in an n-node red-black tree run O(lgn) time.

		The only properties that might be violated are property 2, which requires the root to be black, and property 4, which says that a red node cannot have a red child. Both possible violations are due to z being colored red. Property 2 is violated if z is the root, and property 4 is violated if z's parent is red.
		"""
		x = self.root
		y = self.nil

		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right

		z.p = y
		if y.parent == self.nil:
			self.root = y
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z

		z.color = RED
		self.insertFix(z)

	def insertFix(self, z):
		"""
		The while loop maintains the following three-part invariant at the start of each iteration of the loop.
			a. Node z is red.
			b. If z.parent is the root, then z.p is black.
			c. If the tree violates any of the red-black properties, then it violates at most one of them, and the violation is of either property 4 or property 2.

		There are three case:
			a. z's uncle y is red.
			b. z's uncle y is black and z is a right child.
			c. z's uncle y is black and z is a left child.
		"""
		while z.parent.color == RED:
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right

				# case a
				if y.color == RED:
					z.parent.color = BLACK 
					y.color = BLACK
					z.parent.parent.color = RED
					z = z.parent.parent
				else:
					# case b
					if z == z.parent.right:
						z = z.parent
						self.leftRotate(z)
					# case c
					z.parent.color = BLACK
					z.parent.parent.color = RED
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left

				# case a
				if y.color == RED:
					z.parent.color = BLACK
					y.color = BLACK
					z.parent.parent.color = RED
					z = z.parent.parent
				else:
					if z == z.parent.right：
						z = z.parent
						self.rightRotate(z)
					z.parent.color = BLACK
					z.parent.parent.color = RED
					self.leftRotate(z.parent.parent)

		self.root.color = BLACK







