'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

# 2018-9-29
# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/


# m != n 有最后一位AND后为0
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        offset = 0
        while m != n:
            m >>= 1
            n >>= 1
            offset += 1
        return m<<offset
        

m = 0
n = 1        
test = Solution()
print(test.rangeBitwiseAnd(m, n))
        