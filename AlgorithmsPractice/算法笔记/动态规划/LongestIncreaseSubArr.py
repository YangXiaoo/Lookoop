# coding:utf-8
# 最长上升子序列问题
# 动态规划问题
# LeetCode-300

# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

def subArr(nums):
	"""最长上升子序列问题
	@param nums 输入序列
	"""
	dp = [0 for _ in nums]

	for i in range(len(nums)):
		dp[i] = 1	# 自身也构成一个子序列
		for j in range(i):
			if nums[i] > nums[j]:
				dp[i] = max(dp[i], dp[j] + 1)
	print(dp)

	return max(dp)

def test():
	nums = [10,9,2,5,3,7,101,18]

	ret = subArr(nums)

	print(ret)

if __name__ == '__main__':
	test()
