'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
# 2018-6-16
# Reverse Integer
import sys

# 利用字符串转换
class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strs = str(x)
        res = ""
        pre = ""
        for i in strs:
            if i == "0":
                continue
            elif i == "-":
                pre = i
            else:
                res = i + res
        res = pre+res
        r = int(res)
        if r > 2**31 or r < -2**31:
            return 0 
        return r

# 利用余数
class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True  
        if negative:
            x = -x  
        r = 0  
        while  x > 0 : 
            r = r * 10 + x % 10  
            x /= 10    
        if negative:
            r = -r  
        if r > 2**31 or r < -2**31:
            return 0 
        return r  

# test
x = -3320
test = Solution1()
re = test.reverse(x)
print(re)