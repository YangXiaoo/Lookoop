'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''
# 2018-6-19
# Search Insert Position
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
        	if nums[i] == target:
        		return i
        	if nums[i] > target:
        		return i
        	i += 1
        return i
        
nums = [1,3,4,5,6]
target = 4
test = Solution()
res = test.searchInsert(nums,target)
print(res)