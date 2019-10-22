'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# 2018-10-13
# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/

# Time Limit Exceeded
class Solution1:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicts = []
        for i in nums:
            if i not in dicts:
                dicts.append(i)
            else:
                return True
        return False
        
class Solution2:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False if len(set(nums)) == len(nums) else True
        # return len(seta(nums)) != len(nums) 