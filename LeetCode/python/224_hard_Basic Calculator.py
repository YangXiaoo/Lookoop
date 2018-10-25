'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

# 2018-10-25
# 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, num, sign, res = [], 0, 1, 0
        for i in s:
            if i == " ":
                continue
            if i.isdigit():
                num = 10*num + int(i)
            elif i in ["-", '+']:
                res += sign * num
                num = 0
                sign = [-1, 1][i == '+']
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif i == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
            # print(stack, num, sign, res, i)

        return res + sign * num


s = "(1+(4-5+2)-3)+(6+8)"
test = Solution()
res = test.calculate(s)
print(res)
        