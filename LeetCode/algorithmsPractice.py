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


if __name__ == '__main__':
	test_isPopOrder()
