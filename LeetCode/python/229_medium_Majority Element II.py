'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

# 2018-11-3
# 229. Majority Element II
# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic, ret = {}, []
        lens = len(nums) // 3
        for i in nums:
            if i not in dic:
                dic[i] = 1
                if dic[i] > lens:
                    if i not in ret:
                        ret.append(i)
            else:
                dic[i] += 1
                if dic[i] > lens:
                    if i not in ret:
                        ret.append(i)
        return ret


nums = [1]
test = Solution()
res = test.majorityElement(nums)
print(res)