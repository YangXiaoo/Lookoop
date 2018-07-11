'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

0 1 2 4 5 6 7
7 0 1 2 4 5 6
6 7 0 1 2 4 5
5 6 7 0 1 2 4
4 5 6 7 0 1 2
4 5 6 7 0 1 2
2 4 5 6 7 0 1
1 2 4 5 6 7 0
如果中间数小于最右边的数则右边段是有序的
若中间数大于最右边数则左边段是有序的
'''

# 2018-6-19
# Search in Roated Array
# binary search
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        right = len(nums) - 1
        left = 0
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1

nums = [1,3,1,1,1]
target = 3
test = Solution()
res = test.search(nums,target)
print(res)