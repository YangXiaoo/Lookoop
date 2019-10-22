'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

# 2018-10-9
# 213. House Robber II
# 动态规划
# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        nums_1 = nums[:-1]
        nums_2 = nums[1:]
        def dp_f(nums):
            lens = len(nums)
            dp = [0 for _ in range(lens)]
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, lens, 1):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return dp[-1]
        return max(dp_f(nums_1), dp_f(nums_2))
        

class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        dp = [0 for _ in range(lens)]
        if lens == 0: return 0
        if lens == 1: return nums[0]
        if lens == 2: return max(nums[0], nums[1])
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, lens, 1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]




nums = [2,3,2]
test = Solution()
res = test.rob(nums)     
print(res)


        