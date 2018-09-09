'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

# 2018-9-7
# 171. Excel Sheet Column Number

# https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1] 
        r = 1
        res = 0
        for c in s:
            res += (ord(c) - 64) * r
            r *= 26
        return res
        

s = "AB"
test = Solution()
r = test.titleToNumber(s)
print(r)