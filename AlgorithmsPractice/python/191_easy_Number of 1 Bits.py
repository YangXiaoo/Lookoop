 '''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
'''

# 2018-9-25
# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 2:
            if n % 2 == 1:
                res += 1
            n //= 2

        if n > 0:
            return res+1
        else:
            return res

n = 4
test = Solution()
print(test.hammingWeight(n))


        