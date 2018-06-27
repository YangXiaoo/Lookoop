"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

0 1 2 4 5 6 7
7 0 1 2 4 5 6
6 7 0 1 2 4 5
5 6 7 0 1 2 4
4 5 6 7 0 1 2
4 5 6 7 0 1 2
2 4 5 6 7 0 1
1 2 4 5 6 7 0
"""

# 2018-6-27
# Search in Rotated Sorted Array II
# in case 1: nums[left] < nums[middle], handle left part
# in case 2: nums[left] > nums[middle], handle right part
# in case 3: nums[left] = nums[right], left += 1
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        right = len(nums) - 1
        left = 0
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return True
            if nums[left] < nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[left] > nums[middle]:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                left += 1

        return False


# test
nums = [1,1]
target = 2
test = Solution()
res = test.search(nums,target)
print(res)