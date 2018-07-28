'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.


实现 atoi，将字符串转为整数。

在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来(正负号后面必须为数字才能转换)，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。
说明：

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。

输入: "3.14159" 
输出： 3

输入："   +0 123"
输出：0

输入："2147483648"
输出："2147483647"

输入：" ++1"
输出："0"
'''

# 2018-6-16
# String to Integer

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        s = str.strip()
        if len(s) == 0:
            return 0
        res = 0
        re = ''
        negative = False
        if s[0] == "-":
            negative = True
            t = self.toInt(s[1])
            if not t:
                return 0
            s = s.lstrip("-")
        elif s[0] == "+":
            t = self.toInt(s[1])
            if not t:
                return 0
            s = s.lstrip("+")
        lens = len(s)
        print(s)
        if lens == 0:
            return 0
        try:
            int(s[0])
            for i in range(lens):
                try:
                    int(s[i])
                    re += s[i]
                except:
                    if negative:
                        re = "-" + re
                    re = self.Limit(re)
                    return int(re) 
        except:
            return 0
        maxl = 0
        start = 0
        for i in range(lens):
            if i - maxl >= 1:
                try:
                    int(s[i-maxl-1: i+1])
                    start = i - maxl - 1 
                    maxl += 2
                except:
                    continue
            if i - maxl >= 0 :
                try:
                    int(s[i-maxl: i+1])
                    start = i - maxl
                    maxl += 1
                except:
                    continue
        res = int(s[start:start+maxl])
        if negative:
            res = -res
        res = self.Limit(res)
        return res

    def toInt(self ,char):
        try:
            int(char)
        except:
            return False  

    def Limit(self, res):
        if res > 2**31 - 1:
            return  (2**31 -1)
        elif res < -2**31:
            return  (-2**31)
        else:
            return res


# test 
s = " ++1"
test = Solution()
res = test.myAtoi(s)
print (res)