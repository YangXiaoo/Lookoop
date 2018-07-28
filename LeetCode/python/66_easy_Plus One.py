"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
# 2018-6-23
# Plus One
# just same as 1+1=1, but it is array
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lens = len(digits)
        b = 1
        digits.insert(0,0)
        while lens >= 0:
            e = digits[lens] + b
            digits[lens] = e%10
            b = e//10
            if b == 0:
                break
            # print(b,e)
            lens -= 1
        if digits[0] == 0:
            return digits[1:]
        return digits

# test
digits = [1,2,3,4]
test = Solution()
res = test.plusOne(digits)
print(res)
