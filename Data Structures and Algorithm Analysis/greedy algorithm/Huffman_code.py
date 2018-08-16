# 2018-8-16
# 算法导论 P245

"""
压缩原理：统计词频
编码分为：
	a. 定长编码
		非满二叉树
	b. 变长编码
		满二叉树，比定长编码节约25%空间
"""

class TreeNode(object):
	"""Define a tree"""
	def __init__(self, x=None):
		self.freq = x
		self.left = None
		self.right = None
		
class minQueue(object):
	"""
	最小优先列队，先进先出。
	有待改进。
	"""
	def __init__(self,n=[]):
		self.queue = []

	def popMin(self):
		"""
		弹出最小项
		"""
		# print(self.queue)
		r = self.queue[-1]
		self.queue.pop()
		return r

	def insert(self, x):
		self.queue.append(x)
		self.queue = sorted(self.queue,key=lambda n : n.freq,reverse=True)


def huffman(f):
	"""
	f 为词频字典
	"""
	lens = len(f)
	nums = [f[i] for i in f] # 构造一个数组存储词频以方便操作，最后映射关键字
	nums = sorted(nums,reverse=True)
	print("词频： ", nums)

	# 将每个节点插入最小列队中
	Q = minQueue()
	for i in nums:
		Q.insert(TreeNode(i))

	# 每次抽取最小的两个节点合并成一个节点，然后将合并后的节点插入列队中供下次使用
	for i in range(len(nums)-1):
		z = TreeNode()
		z.left = Q.popMin()
		z.right = Q.popMin()
		if z.right == None:
			Q.insert(z.left)
			break
		z.freq = z.left.freq + z.right.freq
		Q.insert(z)

	tree = Q.popMin()

	# 遍历树得到编码
	r = traversal(tree,nums)

	# 映射还原
	huff = {}
	for i in f:
		huff[i] = r[nums.index(f[i])]
	
	return huff


def traversal(tree,nums):
	"""
	返回每个叶子的编码，返回数组的索引跟nums一一对应
	"""
	stack = [] # 存储每个节点
	code = {} # 存储每个节点的编码
	cur = tree # cur 为当前处理项
	code[tree] = [] # 根节点编码为空
	pre = tree
	res = [0] * len(nums)

	while cur != None or len(stack) != 0:
		while cur != None:
			# print(code,"-----", cur, cur.freq,"---------",pre, pre.freq)
			stack.append(cur)
			dummy = cur
			if cur not in code:
				code[cur] = code[pre].copy()
				code[cur].append(0)
			cur = cur.left
			if cur not in code:
				code[cur] = code[dummy].copy()
				code[cur].append(0)
			pre = dummy

		cur = stack.pop()
		# 遇到叶子的时候生成编码
		if cur.right == None:
			# print("result=======>", code[cur],cur.freq)
			res[nums.index(cur.freq)]=code[cur]
		pre = cur
		cur = cur.right
		if cur not in code:
			code[cur] = code[pre].copy()
			code[cur].append(1)

	# 将数组中的数字转换成字符并连接成字符串
	c = 0
	for i in res:
		tmp = ""
		for j in i:
			tmp += str(j)
		res[c] = tmp
		c += 1

	return res

if __name__ == "__main__":
	f = {'a':45,'b': 13, 'c':12, 'd':16, 'e':9, 'f':5}
	res = huffman(f)
	print(res)
	"""
	输出结果：
	词频：  [45, 16, 13, 12, 9, 5]
	{'a': '0', 'b': '101', 'c': '100', 'd': '111', 'e': '1101', 'f': '1100'}
	[Finished in 0.2s]
	"""
