'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

# 2018-11-4
# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret, pre = [], 1
        for i in nums:
        	ret.append(pre)
        	pre = pre * i 
        pre = 1
        print(ret)
        for i in range(len(nums) - 1, -1, -1):
        	ret[i] = ret[i] * pre 
        	pre = pre * nums[i]
        return ret



nums = [1,2,3,4]
test = Solution()
res = test.productExceptSelf(nums)
print(res)
        

        