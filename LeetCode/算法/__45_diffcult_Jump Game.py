"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

# 2018-6-21
# Jump Game II
# https://www.cnblogs.com/zuoyuan/p/3781953.html
class Solution:
    # @param nums, a list of integers
    # @return an integer
    # def jump(self, nums):
    #     maxint = 1<<31 - 1
    #     dp = [ maxint for i in range(len(nums)) ]
    #     dp[0] = 0
    #     for i in range(1, len(nums)):
    #         for j in range(i):
    #             if nums[j] >= (i - j):
    #                 dp[i] = min(dp[i], dp[j] + 1)
    #     return dp[len(nums) - 1]
    # dp is time limited exceeded!
    
# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "ret", whereas "curr" is the maximum distance
# that can be reached by using "ret+1" steps. Thus,curr = max(i+nums[i]) where 0 <= i <= last.
    def jump(self, nums):    
        ret = 0
        last = 0
        curr = 0
        for i in range(len(nums)):
            if i > last:
                last = curr
                ret += 1
            print(ret,last,i,nums[i])
            curr = max(curr, i+nums[i])
        return ret

nums = [2,3,1,1,4,2]
test = Solution()
res = test.jump(nums)
print(res)