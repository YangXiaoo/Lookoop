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

def majorityElement(nums):
    """超过三分之一的数,最多不超过两个数"""
    if len(nums) <= 2:
        return nums[0]
    num1, num2 = -1, -1
    count1, count2 = 0, 0
    for i in range(len(nums)):
        curNum = nums[i]
        if curNum == num1:
            count1 += 1
        elif curNum == num2:
            count2 += 1
        elif count1 == 0:
            num1 = curNum
            count1 = 1
        elif count2 == 0:
            num2 = curNum
            count2 = 1
        else:
            count1 -= 1
            count2 -= 2

    count1, count2 = 0, 0
    for n in nums:
        if n == num1:
            count1 += 1
        elif n == num2:
            count2 += 1
    print("num1: {}, count1: {}; num2: {}, count2: {}".format(num1, count1, num2, count2))
    numLens = len(nums)
    ret = []
    if count1 > numLens//3:
        ret.append(num1)
    if count2 > numLens//3:
        ret.append(num2)
    
    return ret

def test_majorityElement():
    nums = [1,1,1,3,3,2,2,2]
    ret = majorityElement(nums)
    print(ret)

# test_majorityElement()



nums = [1]
test = Solution()
res = test.majorityElement(nums)
print(res)