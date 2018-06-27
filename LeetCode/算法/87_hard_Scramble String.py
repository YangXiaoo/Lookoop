"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""

# 2018-6-27
# Scramble String
# https://www.cnblogs.com/grandyang/p/4318500.html
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False 
        if s1 == s2: return True 
        t1,t2 = s1,s2
        if sorted(t1) != sorted(t2): return False

        for i in range(1,len(s1)):
        	s11 = s1[:i]
        	s12 = s1[i:]
        	s21 = s2[:i]
        	s22 = s2[i:]
        	if self.isScramble(s11,s21) and self.isScramble(s12,s22): return True
        	s21 = s2[:len(s2)-len(s11)]
        	s22 = s2[len(s2)-len(s11):]
        	if self.isScramble(s11,s22) and self.isScramble(s12,s21): return True

        return False
        



# test 
s1 = "abcde"
s2 = "caebd"
test = Solution()
res = test.isScramble(s1,s2)
print(res)