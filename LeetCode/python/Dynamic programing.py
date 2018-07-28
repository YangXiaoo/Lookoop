# Dynamic programing
# 2018-6-22
"""
动态规划
实例：台阶
三个重要概念：最优子结构，边界，状态转移公式
F(N) = F(N-1) + F(N-2)
"""

class Solution1():
	def stair(self,n):
		if n < 1: return 0
		if n == 1: return 1
		if n == 2: return 2
		return self.stair(n-1) + self.stair(n-2)

class Solution2():
	def stair(self,n,dic):
		if n < 1: return 0
		if n == 1: return 1
		if n == 2: return 2
		if n in dic:
			return dic[n]
		else:
			value = self.stair(n-1,dic) + self.stair(n-2,dic)
			dic[n] = value
			return value

class Solution3():
	def stair(self,n):
		if n < 1: return 0
		if n == 1: return 1
		if n == 2: return 2
		a = 1
		b = 2
		tmp = 0
		for i in range(3,n+1):
			tmp = a + b
			a = b
			b = tmp
		return tmp

test1 = Solution1()
r1 = test1.stair(10)
test2 = Solution2()
r2 = test2.stair(10,{})
test3 = Solution3()
r3 = test3.stair(10)
print(r1,r2,r3)
