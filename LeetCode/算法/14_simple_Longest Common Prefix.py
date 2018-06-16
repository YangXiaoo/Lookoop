'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''
# 2018-6-16
# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lens = len(strs)
        if lens == 0:
            return ""
        elif lens == 1:
            return strs[0]
        p = 0
        min_lens = len(strs[p])
        for i in range(1,lens):
            if len(strs[i]) < len(strs[p]):
                min_lens = strs[i]
                p = i
        end = 1
        while end < len(strs[p]) + 1:
            for j in range(0,lens):
                if j == p:
                    continue
                elif strs[j][:end] == strs[p][:end]:
                    continue
                else:
                    if end == 1:
                        return ""
                    else:
                        return strs[p][:end-1]
            end += 1
        if end == 1:
            return strs[p]
        else:
            return  str(strs[p][:end])


# test
strs = [["cc","a"],["dog","racecar","car"],["flower","flow","flight"],["",""]]
test = Solution()
for t in strs:
    res = test.longestCommonPrefix(t)
    print(res)