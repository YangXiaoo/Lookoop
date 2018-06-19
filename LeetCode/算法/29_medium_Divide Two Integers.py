'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient(商) after dividing(被除数) dividend by divisor(除数).

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.
'''

# 2018-6-19
# Divide Two Integers
# 暴力解法
class Solution1:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor>0:
            ne_sor = False
        else:
            ne_sor = True
        if dividend>0:
            ne_end = False
        else:
            ne_end = True
        quotient = 0
        div = divisor = abs(divisor)
        dividend = abs(dividend)
        while div <= dividend:
            quotient += 1
            div += divisor
        if (ne_sor and ne_end) or (not ne_sor and not ne_end):
            return quotient
        else:
            return -quotient

# 通过移位，1,2,4...倍数
class Solution2:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            k = 0
            tmp = divisor
            # print(tmp,dividend,"----")
            while dividend >= tmp:
                dividend -= tmp
                quotient += 1 << k # quotient = quotient + (1 << k)
                tmp <<= 1
                k += 1
                # print(k,quotient,dividend,tmp)
        quotient  = sign * quotient
        if quotient > MAX_INT:
            quotient = MAX_INT
        return quotient

dividend = -16
divisor = -2
test = Solution2()
res = test.divide(dividend,divisor)
print(res)

