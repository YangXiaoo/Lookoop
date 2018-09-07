'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

# 2018-9-7
# 168. Excel Sheet Column Title

# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        radix = 65
        res = ""
        if n <= 26:
            return chr(radix + n)
        while n:
            res = chr((n - 1) % 26 + radix) + res
            n = (n - 1) // 26
        return res

n = 52
test = Solution()
r = test.convertToTitle(n)
print(r)