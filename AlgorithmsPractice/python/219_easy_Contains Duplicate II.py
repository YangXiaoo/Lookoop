'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

# 2018-10-16
# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/

# Time Limit Exceeded
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lens = len(nums)
        for i in range(lens):
            j = i + 1
            while  j < i + k + 1 and j < lens:
                if nums[i] == nums[j]:
                    return True 
                j += 1

        return False 

class Solution2:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dicts = {}
        lens = len(nums)
        for i in range(lens):
            if nums[i] not in dicts:
                dicts[nums[i]] = [i]
            else:
                if i - dicts[nums[i]][-1] <= k:
                    return True 
                dicts[nums[i]].append(i)

        return False 


nums = [2,2]
k = 2
test = Solution2()
res = test.containsNearbyDuplicate(nums, k)
print(res)