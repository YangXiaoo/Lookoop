"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
# 2018-6-23
# Add Binary
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = '0'
        i = 0
        lena = len(a)
        lenb = len(b)
        while i < max(lena, lenb) or carry == '1':
        	aa = a[-1 - i] if i < lena else '0'
        	bb = b[-1 - i] if i < lenb else '0'

        	sums = int(aa) + int(bb) + int(carry)
        	res = str(sums%2) + res
        	carry = '1' if sums//2 > 0 else '0'

        	i += 1
        return res


# test
a = "1010"
b = "1011"
test = Solution()
res = test.addBinary(a,b)
print(res)