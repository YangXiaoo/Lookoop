'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

# 2018-10-3
# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s , dic_t= {}, {}

        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = i 
        for j in range(len(t)):
            if t[j] not in dic_t:
                dic_t[t[j]] = j
            # 索引位置不同则不可以替换
            if dic_s[s[j]] != dic_t[t[j]]:
                return False 

        return True 

s ="foo"
t = "bst"
test = Solution()
res = test.isIsomorphic(s, t)
print(res)