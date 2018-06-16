'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


# 2018-6-16
# Integer to Roman
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r = []
        res = ''
        x = 1
        while num > 0:
            r.append((num % 10)*x)
            num = num // 10
            x *= 10
        lens = len(r)-1
        for i in range(lens,-1,-1):
            if r[i]//1000 > 0: res += "M"*(r[i]//1000)
            if r[i]//100 > 0 and r[i]//100 < 10:
                j = r[i]//100
                if j<4: res += "C"*(j)
                elif j == 4: res += "CD"
                elif j == 5: res += "D"
                elif j > 5 and j < 9: res += "D" + "C"*(j-5)
                else: res += "CM"
            if r[i]//10 > 0 and r[i]//10 < 10:
                t = r[i]//10
                if t<4: res += "X"*(t)
                elif t == 4: res += "XL"
                elif t == 5: res += "L"
                elif t > 5 and t < 9: res += "L" +"X"*(t-5)
                else: res += "XC" 
            if r[i]//1 > 0 and r[i]//1 < 10:
                n = r[i]//1
                if n<4: res += "I"*(n)
                elif n == 4: res += "IV"
                elif n == 5: res += "V"
                elif n > 5 and n < 9: res += "V" +"I"*(n-5)
                else: res += "IX" 
        return res                           

# test
num = 1994
test = Solution()
res = test.intToRoman(num)
print(res)