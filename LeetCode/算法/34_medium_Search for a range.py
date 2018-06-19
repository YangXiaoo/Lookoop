'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

# 2018-6-19
# Search for a range
# O(logN)
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        
        # find start in [0,len-1]
        l=0
        r=len(nums)-1
        while r>l:
            m=(l+r)//2
            if target>nums[m]:
                l=m+1
            else:
                r=m
        if nums[l]==target:
            st=l
        else:
            return [-1,-1]
        # find end in [st,len-1]
        l=st
        r=len(nums)-1
        while r>l:
            m=(l+r+1)//2
            if target<nums[m]:
                r=m-1
            else:
                l=m
        return [st,r]

        
# O(N)
class Solution2:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            i = nums.index(target)
            n = nums.count(target)
            return [i, i + n - 1]
        except ValueError:
            return [-1, -1]


nums = [5,7,7,8,8,8,8,10,10,10]
target = 8
test = Solution()
res = test.searchRange(nums,target)
print(res)