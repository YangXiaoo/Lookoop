'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

# 2018-9-18
# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        tmp = []
        for i in nums:
            tmp.append(str(i))
        # tmp = sorted(tmp)
        def swap(i, j):
            t = tmp[i]
            tmp[i] = tmp[j]
            tmp[j] = t
        lens = len(nums) - 1
        i = 0
        while i < lens :
            j = 0
            while j < lens - i:
                if int(tmp[j] + tmp[j + 1]) > int(tmp[j + 1] + tmp[j]):
                    swap(j, j + 1)
                j += 1
            i += 1

        print(tmp)
        tmp = tmp[::-1]
        return str(int("".join(tmp)))