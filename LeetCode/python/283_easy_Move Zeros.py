'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# 2018-11-9
# 283. Move Zeros
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        len_nums, left, i, first = len(nums), 0, 0, True
        while i < len_nums:
            if nums[i] == 0:
                left = [left, i][first == True]
                first = False
            else:
                if not first:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            i += 1

nums = [1,1]
test = Solution()
test.moveZeroes(nums)
print(nums)
