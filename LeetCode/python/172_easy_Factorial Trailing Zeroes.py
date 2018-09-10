'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

# 2018-9-8
# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n > 0:
            n //= 5
            print(n)
            r += n
        return r

n = 97
test = Solution()
r = test.trailingZeroes(n)
print(r)
print("02".split('0'))