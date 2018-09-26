'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

# 2018-9-26
# 198. House Robber
# 动态规划
# https://leetcode.com/problems/house-robber/description/

# https://www.cnblogs.com/lightwindy/p/8648410.html
# State: dp[i]，表示到第i个房子时能够抢到的最大金额。
# Function: dp[i] = max(num[i] + dp[i - 2], dp[i - 1])
# Initialize: dp[0] = num[0], dp[1] = max(num[0], num[1]) 或者 dp[0] = 0, dp[1] = 0
# Return: dp[n]

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max = 0
        curr_max = 0
        for num in nums:
            prev_max, curr_max = curr_max, max(prev_max + num, curr_max)
        return curr_max

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




nums = [2,7,9,3,1]
test = Solution2()
res = test.rob(nums)     
print(res)


        