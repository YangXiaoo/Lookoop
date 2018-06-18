'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

# 2018-6-17
# Generate Parenthese
# https://blog.csdn.net/zl87758539/article/details/51643837
# DFS
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.generateParenthesisIter('',n, n)
        return self.res

    def generateParenthesisIter(self, mstr, r, l,i="f"):
        print(mstr,r,l,i)
        if r ==0 and l==0:
            self.res.append(mstr)
        if l>0:
            self.generateParenthesisIter(mstr+'(',r,l-1,i="s")
        if r>0 and r>l:
            self.generateParenthesisIter(mstr+')',r-1,l,i="t")
        print(mstr,r,l,i)

# test
n = 3
test = Solution()
res = test.generateParenthesis(n)
print(res)