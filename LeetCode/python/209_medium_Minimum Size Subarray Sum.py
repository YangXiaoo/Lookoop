'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

# 2018-10-6
# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# TLE 14 / 15 test cases passed.
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = []
        i = 0
        lens = len(nums)
        min_lens = lens
        while i < lens - 1:
            j = i + 1
            tmp_sub = []
            while j < lens + 1:
                # print(i,j,nums[i:j], sum(nums[i:j]))
                if sum(nums[i:j]) > s - 1:
                    tmp_sub = nums[i:j]
                    break
                j += 1
            # print(tmp_sub, len(tmp_sub), min_lens)
            if len(tmp_sub) < min_lens + 1 and len(tmp_sub) != 0:
                min_lens = len(tmp_sub)
                res = tmp_sub
            i += 1
        return len(res)


class Solution2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = []
        lens = len(nums)
        min_lens = lens + 1
        l = 0
        r = 1
        while l < lens:
            while r < lens + 1:
                if sum(nums[l:r]) >= s:
                    tmp_sub = nums[l:r]
                    break
                r += 1
            # print(len(tmp_sub), tmp_sub, min_lens, l, r)
            if len(tmp_sub) < min_lens:
                min_lens = len(tmp_sub)
                res = tmp_sub
            while l < r:
                l += 1
                if sum(nums[l:r]) < s:
                    break
                else:
                    if len(nums[l:r]) < min_lens:
                        min_lens = len(nums[l:r])
                        res = nums[l:r]
            r -= 1
        return len(res)








s = 15
nums = [1,2,3,4,5] # 13 / 15 test cases passed.
# nums = [2,3,1,2,4,3]
test = Solution2()
res = test.minSubArrayLen(s, nums)
print(res)