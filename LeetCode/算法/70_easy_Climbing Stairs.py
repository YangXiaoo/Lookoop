"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
# 2018-6-24
# Climbing Stairs
class Solution1():
	def climbStairs(self,n):
		if n < 1: return 0
		if n == 1: return 1
		if n == 2: return 2
		return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution2():
	def climbStairs(self,n,dic):
		if n < 1: return 0
		if n == 1: return 1
		if n == 2: return 2
		if n in dic:
			return dic[n]
		else:
			value = self.climbStairs(n-1,dic) + self.climbStairs(n-2,dic)
			dic[n] = value
			return value

class Solution3():
	def climbStairs(self,n):
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

# test
n = 10
test = Solution1()
res = test.climbStairs(n)
print(res)