"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

# 2018-6-21
# 55.Jump game(medium)
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = 1 
        for i in range(len(nums)):
            if counter < 1: # can't reach the next position
                return False
            counter = max(counter-1,nums[i])
        return True
      

# test
nums = [[2,3,1,1,4,2],[3,2,1,0,4]]
test = Solution()
for nums in nums:
    res = test.canJump(nums)
    print(nums,"--is",res)
