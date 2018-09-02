# 2018-8-7 - 2018-8-9
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
	def __init__(self, X):
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
		self.root = None
		self.nil = None
		"""
		self.root.left = self.nil
		self.root.right = self.nil
		self.root.parent = self.nil
		"""
	def inorder(self):
		"""
		Inorder traversal. 
		"""
		node = self.root
		self.traversal(node)

	def traversal(self, node):
		if node != self.nil:
			self.traversal(node.left)
			print("Inorder traversal--> color:",node.color,", key: ", node.key)
			self.traversal(node.right)


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

	def transplant(self, u, v):
		"""
		Alternate v to u
		"""
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

		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z

		z.parent = y
		z.left = self.nil
		z.right = self.nil
		z.color = RED
		print("Insert node--> key: ", z.key, ", color: ", z.color)
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
		try:
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
						if z == z.parent.left:
							z = z.parent
							self.rightRotate(z)
						z.parent.color = BLACK
						z.parent.parent.color = RED
						self.leftRotate(z.parent.parent)
		except:
			pass

		self.root.color = BLACK


	def delete(self, z):
		"""
		Delete node z, because color x may cause a violation of one of the red-black properties, we call "deleteFix(x)" to restore the red-black properties.
		"""
		y = z
		y_original_color = y.color
		if z.left == self.nil:
			self.transplant(z, z.right)
		elif z.right == self.nil:
			self.transplant(z, z.left)
		else:
			y = self.treeMinimum(z.right)
			y_original_color = y.color
			x = y.right

			if y.parent == z:
				x.p = y
			else:
				self.transplant(y, x)
				y.right = z.right
				y.right.parent = y
				self.transplant(z, y)
				y.left = z.left
				z.left.parent = y
				y.color = z.color
		print("delete--->", "key: ",z.key, "color : ",z.color)

		"""
		If y was red, the red-balck properties still hold when y is remove or move, for the following reasons:
			a. No black-heights in the tree have changed.
			b. No red node have been made adjacent.
			c. Since y could not have been the root if it was red, the root remains black.

		If y was black, three problems may arise, which the call of "deleteFix(x)" will remedy. 
			a. If y had been the root and a red child of y becomes the new root, we have violated property 2.
			b. If both x and x.parent are red, then we have violated property 4.
			c. Moving y within thr tree causes any simple path that previously contained y to have one fewer black node. Thus, property 5 is now violated by any ancestor of y in the tree.
		"""
		if y_original_color == BLACK:
			self.deleteFix(x)


	def deleteFix(self, x):
		"""
		There are four case:
			a. x's sibling w is red.(Will convert case a to case b, c, or d.)
			b. x's sibling w is black, and both of w's children are balck.
			c. x's sibling w is black, w's left child is red, and w's right child is black.(Will cause case d.)
			d. x's sibling w is black, and w's right child is res. 
		"""
		while x != self.root and x.color == BLACK:
			if x == x.parent.left:
				w = x.parent.right
				# case a
				if w.color == RED:
					w.color = BLACK
					x.parent.color = RED
					self.leftRotate(x.parent)
					w = x.parent.right
				# case b
				if w.left.color == BLACK and w.right.color == BLACK:
					w.color = RED
					x = x.parent
				else:
					# case c (convert to case d)
					if w.left.color == RED and w.right.color == BLACK:
						w.color = RED
						w.left.color = BLACK
						self.rightRotate(w)
						w = x.parent.right
					# case d
					w.color = x.parent.color
					x.parent.color = BLACK
					w.right.color = BLACK
					self.leftRotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == RED:
					w.color = BLACK
					x.parent.color = RED
					self.rightRotate(x.parent)
					w = x.parent.left
				if w.left.color == BLACK and w.right.color == BLACK:
					w.color = RED
					x = x.parent
				else:
					if w.right.color == RED and w.left.color == BLACK:
						w.color = RED
						w.right.color = BLACK
						self.leftRotate(w)
						w = w.parent.left
					w.color = x.parent.color
					x.parent.color = BLACK
					w.left.color = BLACK
					self.rightRotate(x.parent)
					x = self.root

			x.color = BLACK

def main():
	"""
	Test!
	"""
	test = RedBlackTree()
	lits = [7,2,5,4,9,1,6,12,8]
	for i in lits:
		node = RedBlackNode(i)
		test.insert(node)
		del node
	test.inorder()
	test.delete(test.root)
	test.inorder()

if __name__ == "__main__":
	main()
