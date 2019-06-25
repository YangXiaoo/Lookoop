# coding:utf-8
# 复习记录

#######################################
# 15-二进制中1的个数
def countBit01(n):
	"""左移，防止负数右移时出错"""
	count = 0
	flag = 1
	for i in range(32):
		if n & flag:
			count += 1
		flag <<= 1

	return count

def countBit02(n):
	"""n & (n - 1)
	1100 & 1011 -> 1000 少一个1
	"""
	count = 0
	while n:
		count += 1
		n = n & (n -1)

	return count

def test_countBit():
	nums = [1, 2, 22, 33, 9, 32]
	for n in nums:
		ret1 = countBit01(n)
		ret2 = countBit02(n)

		print("ret1: {}, ret2: {}".format(ret1, ret2))

#######################################
# 16-数值的整数次方
def power(base, exponent):
	"""考虑0情况，并考虑exponent正负号"""
	pass

#######################################
# 31-栈的压入弹出顺序
def isPopOrder(push, pop):
	record = []
	index = 0
	pushIndex = 0
	ret = True
	while index < len(pop):
		while len(record) == 0 or record[-1] != pop[index]:
			record.append(push[pushIndex])
			pushIndex += 1

		# print(record)
		if record[-1] != pop[index]:
			ret = False
			break

		record.pop()
		index += 1

	return ret

def test_isPopOrder():
	push = [1,2,3,4,5]
	pop = [4,5,3,2,1]

	ret = isPopOrder(push, pop)
	print("ret: {}".format(ret))

#######################################
# 49-丑数
def uglyNumber(n):
	"""求从小到大顺序排列的第n个丑数
	以空间换时间，时间复杂度O(n)
	"""
	ugly2, ugly3, ugly5 = 0, 0, 0
	uglyNums = [0 for _ in range(n)]
	uglyNums[0] = 1	# 第一个丑数
	for i in range(n)[1:]:
		nextUgly = min(uglyNums[ugly2]*2, uglyNums[ugly3]*3, uglyNums[ugly5]*5)
		# print(nextUgly)
		uglyNums[i] = nextUgly
		while uglyNums[ugly2]*2 <= nextUgly:
			ugly2 += 1
		while uglyNums[ugly3]*3 <= nextUgly:
			ugly3 += 1		
		while uglyNums[ugly5]*5 <= nextUgly:
			ugly5 += 1
	# print("-"*30)
	return uglyNums[-1]

def test_uglyNumber():
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
	for n in nums:
		ret = uglyNumber(n)
		print("ret: {}".format(ret))

#######################################
# 55-03-二叉树的最小深度[leetcode-111]
def minDepthOfBT(root):
	pass 

# 55-02-平衡二叉树
def balanceBT(root):
	if not root:
		return True

	if abs(depth(root.left)-depth(root.right)) > 1:
		return False

	return balanceBT(root.left) and balanceBT(root.right)

def depth(root):
	if not root:
		return 0

	return max(depth(root.left), depth(root.right)) + 1

#######################################
# 60-n个骰子的点数
def probability(n):
	def _helper(n, pro):
		"""计算每一种可能"""
		for i in range(1, maxValue + 1):
			countPro(n, n, i, pro)

	def countPro(orig, cur, sums, pro):
		"""计算概率
		@param orig 基数
		@param cur 当前骰子数
		@param sums 骰子和
		@param pro 概率
		"""
		if cur == 1:
			pro[sums - orig] += 1
		else:
			for i in range(1, maxValue + 1):
				countPro(orig, cur - 1, i + sums, pro)

	maxValue = 6
	pro = [0 for _ in range(maxValue * 6 - 6 + 1)]
	_helper(n, pro)

	total = maxValue**n 
	for i in range(len(pro)):
		pro[i] /= total

	return pro

def test_probability():
	n = 6
	ret = probability(n)
	print("ret: {} \nverify sum(pro): {}".format(ret, sum(ret)))

#######################################
# 62-圆圈中最后剩下的数字
def lastNumber(n, m):
	"""每次从n个数中删除第m个数字"""
	nums = [i for i in range(n)]
	preIndex = 0
	while len(nums) > 1:
		curIndex = preIndex
		curLength = len(nums)
		for i in range(m-1):
			curIndex += 1
			if curIndex > curLength - 1:
				curIndex = curIndex - curLength

		print("cur nums: {}, delete num: {}, delete index: {}, preIndex: {}".format(nums, nums[curIndex], curIndex, preIndex))
		nums.pop(curIndex)
		preIndex  = curIndex

	return nums[0]

def test_lastNumber():
	n, m = 5, 2
	ret = lastNumber(n, m)
	print("ret: {}".format(ret))

#######################################
# 64-求1+2+...+n
"""不使用乘除法以及for,while,if, else, switch,case,条件判断"""
"""java	
	
	//方法一：利用库函数+位运算
	public int sumN01(int n) {
		int sum = (int)(Math.pow(n, 2)+n) >> 1;

		return sum;
	}

	//方法二：利用 && 运算符实现短路结束递归条件
	public int sumN02(int n) {
		int sums = n;
		boolean dummy = (n > 0) && (sums = sums + sumN02(n-1) > 0);

		return sums;
	}
"""
########################################
# 65-不用加减乘除做加法
def add(num1, num2):
	while True:
		sums = num1 ^ num2
		carry = (num1 & num2) << 1
		print("sums: {}, carry: {}, bin(num1): {}, bin(num2): {}".format(sums, carry, bin(num1), bin(num2)))
		num1 = sums
		num2 = carry

		if num2 == 0:
			break
	return num1

def test_add():
	num1, num2 = 98, 99
	ret = add(num1, num2)
	print("ret: {}".format(ret))

if __name__ == '__main__':
	test_add()
