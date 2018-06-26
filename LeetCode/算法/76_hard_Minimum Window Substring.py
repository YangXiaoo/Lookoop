"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

import collections

# 2018-6-26
# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        print(need,missing)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0 # missing = missing -1 if need[c] > 0 else missing 
            print(j,c,missing,need,i,j,I,J)
            need[c] -= 1 # 添加c并使得 c : -1
            if not missing: # missing <= 0 
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
                #print(need)
        print(j,c,missing,need,i,j,I,J)
        return s[I:J]
# test
S = "ADOBECODEBANC"
T = "ABC"

test = Solution()
res = test.minWindow(S,T)
print(res)