# 2018-8-17 ~ 2018-8-18
# 斐波那锲堆(Fibonacci heap data structure)
# 算法导论 P290
# https://www.cnblogs.com/junyuhuang/p/4463758.html

"""
一个切波那契堆是一系列具有最小堆序(min-heap ordered) 的有跟树的集合。每棵树都遵循最小堆性质
每个节点的关键字大于或等于它的父节点的关键字。

根链表为环形双向链表
每个节点x都包含一个指向它父节点的指针x.p 和一个指向它的某一个孩子指针x.child. 孩子表中每个孩子y均有y.left和y.right。
"""

# 有问题
class Node(object):
	"""
	定义节点
	"""
	# __slots__ = ['key', 'left', 'right', 'p', 'c', 'degree', 'mark']
	def __init__(self, data=None):
		self.key = data
		self.left = None
		self.right = None
		self.p = None
		self.c = None
		self.degree = 1
		self.mark = False
		
MIN_INT = -2147483648 # -32768
class FibHeap(object):
	def __init__(self):
		self.min = None # 指向根链表中关键字最小的那个点
		self.n = 0 # 表示H当前的节点数目

	def swap(self, x, y):
		tmp = x
		x = y
		y = tmp
		return x, y

	def insert(self, x):
		"""
		向堆中插入x, x已经分配
		摊还代价为1
		"""
		if self.min == None:
			x.left = x
			x.right = x
			self.min = x
		else:
			self.addToRootList(x)
			if x.key < self.min.key:
				self.min = x
		self.n += 1


	def addToRootList(self, x):
		"""
		将节点插入堆的根链表中
		"""
		if self.min.left == self.min:
			self.min.left = x
			x.right = self.min
			self.min.right = x
			x.left = self.min
		else:
			r_left = self.min.left
			r_left.right = x
			self.min.left = x
			x.right = self.min
			x.left = self.min

	def extractMin(self):
		"""
		抽取最小节点
		"""
		z = self.min

		if z != None:
			child = z.c # 孩子
			mark = child
			if child != None:
				old = child
				c = 1
				child = child.right
				while old != child:
					c += 1
					if c > self.n:
						print("Something wrong, exceed max iterations: ", c)
						return 
					# print("child values: ", child.key)
					child = child.right
				# print("c = ", c)
				while c != 0:
					addnode = child
					child = child.right
					self.addToRootList(addnode)
					# print(child.key)
					c -= 1
			z_right = z.right
			if z_right == z and mark == None:
				self.min = None
			else:
				self.deleteNode(self.min)
				self.min = z_right
				self.consolidate()
			self.n  -= 1

		return z

	def deleteNode(self, node):
		"""
		删除根链表上的最小节点,已经不考虑只有一个节点的情况
		"""
		left_node = node.left
		right_node = node.right

		# 连接
		left_node.right = right_node
		right_node.left = left_node

	def consolidate(self):
		"""
		调用此函数来减少切波那契堆中树的数目，重复一下操作直到根链表中的每一个根有不同的度数：
			a. 在根链表中找到两个具有相同度的根x, y。不失一般性假定x.key <= y.key
			b. 把y链接到x：从根链表中移除y, 调用link()函数，使得y称为x的孩子, 该过程中x.degree的属性加1， 并清除y上的标记
		"""
		A = [None] * (self.n) #用A来记录根节点对应的度数的轨迹, 若A[i] = y, 则 y.degree == i
		cur = self.min
		old = cur
		d = cur.degree
		A[d] = cur
		cur = cur.right
		while old != cur:
			if cur == None:
				break
			x = cur
			cur = cur.right
			d = x.degree
			# print("consolidate probe_0:",x.key, d, self.n)
			while A[d] != None:
				# print("consolidate probe_A arrary: ", A)
				y = A[d] # 另一个有相同度数的节点
				# print("consolidate probe_1:",y.key, x.key)
				if x.p == None: # 此处应该判断是否在根链表
					self.deleteNode(x)
				flag = 0
				if x.key > y.key:
					# 交换x,y节点
					x,y = y,x
				self.link(x, y)
				A[d] = None # 此度数的节点已经改变，所以置为空
				d += 1 # 加上一个节点后度数加1

			A[d] = x # 跟新节点记录

		self.min = None # 根据A重新生成堆
		n = self.n # insert()函数使用的过程中self.n被改变了
		for i in range(len(A)):
			if A[i] != None:
				# print("degree-------",A[i].degree)
				self.insert(A[i])
		self.n = n
		# print("consolidate probe_2:",self.min.key, A)

	def link(self, x, y):
		"""
		移除根链表上y，然后将y成为x的孩子。 x.degree加1，将y.mark标记为False，
		"""
		# print("link() probe_1: ", x,y, x.key, y.key)
		x_child = x.c 
		if x_child == None:
			x.c = y
			y.left = y
			y.right = y
		elif x_child == x_child.right:
			x_child.right = y
			x_child.left = y
			y.right = x_child
			y.left = x_child
		else:
			x_child_left = x_child.left
			x_child_left.right = y
			y.left = x_child_left
			x_child.left = y
			y.right = x_child
		y.p = x
		x.degree += 1
		y.mark = False
		# print("link() probe_2 x.key ,x.degree: ", x.key, x.degree)

	def decreaseKey(self, x, k):
		"""
		关键字减值
		"""
		if k > x.key:
			print("The value you want to decrease must less than the value of key.")
			return False

		x.key = k
		y = x.p
		if y != None and x.key < y.key:
			self.cut(x, y)
			self.cascadingCut(y)
		if x.key < self.min.key:
			self.min = x

	def cut(self, x, y):
		"""
		将x从y子节点中移除，减少y节点度数， 将x添加到根链表中
		"""
		y.c = None
		x.p = None
		y.degree -= x.degree 
		if x.right != x:
			x_left = x.left
			x_right = x.right
			x_left.right = x_right
			x_right.left = x_left
		x.mark = False
		self.addToRootList(x)

	def cascadingCut(self, y):
		"""
		此时y的孩子已经减少了，所以要改变y.mark标记。
		如果y.mark==True即在y成为其它节点之后已经失去过孩子，则需要将y剪断并添加到根链表中。
		递归调用使得标记符合要求
		"""
		z = y.p
		if z != None:
			if y.mark == False:
				y.mark = True
			else:
				self.cut(y, z)
				self.cascadingCut(z)

	def delete(self, x):
		"""
		删除任一节点，将此节点的值减至最小，成为H.min,然后调用extractMin()删除最小值即可
		"""
		self.decreaseKey(x, MIN_INT)
		self.extractMin()

def test():
	fb = FibHeap()
	for i in range(20):
		fb.insert(Node(i))

	print("最小值：", fb.min.key)
	print("H的n值：", fb.n)
	print()

	node = fb.min
	for i in range(20):
		# print("Each node key:", node.key)
		node = node.right

	for i in range(8):
		mins = fb.extractMin()
		print("移除最小值： ", mins.key)

	print("\n当前最小值：", fb.min.key)

	node = fb.min
	old = node
	print("\n根链表上的结点: ", node.key)
	node = node.right
	while node != old:
		print("根链表上的结点: ", node.key)
		if node.c != None:
			# print("child is: ", node.c.key,node.c.right.key)
			pass
		node = node.right


if __name__ == "__main__":
	"""
	Test!
	"""	
	test()
