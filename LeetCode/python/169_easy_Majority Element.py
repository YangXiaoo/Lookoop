'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

# 2018-9-8
# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1

        m = 0
        r = nums[0]
        for i in h:
            if h[i] > m:
                m = h[i]
                r = i
        return r

class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为 元素长度大于⌊ n/2 ⌋, 所以直接取len(nums) // 2位置就可以
        nums.sort()
        return nums[len(nums) // 2]

nums = [2,2,1,1,1,2,2]
test = Solution()
r = test.majorityElement(nums)
print(r)
        