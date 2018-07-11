"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

# 2018-6-21
# Pow(x.n)
class Solution1:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0: 
            x = 1/x
            n = abs(n)
        
        if n == 0: return 1
        if n == 1: return x
        # print(n)
        ret = self.myPow(x, n//2)
        print(ret)
        
        return ret*ret if n%2 == 0 else ret*ret*x


# LTE
class Solution2:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0: 
            x = 1/x
            n = abs(n)
        
        if n == 0: return 1
        if n == 1: return x

        i = 1
        m = x
        while i < n:
            x = x * m
            i += 1
        return x        
# test
x = 2.0000
n = 10
test = Solution1()
r = test.myPow(x,n)
print(r)