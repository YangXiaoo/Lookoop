"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

# 2020-9-24
class Solution:
    def partitionLabels(self, S):
        charMap = {}
        for i, c in enumerate(S):
            charMap[c] = i 

        print(charMap.items())
        preIndex, lastIndex = 0, 0
        ret = []
        for i, c in enumerate(S):
            lastIndex = max(lastIndex, charMap[c])
            if i == lastIndex:
                ret.append(lastIndex - preIndex + 1)
                preIndex = lastIndex + 1

        return ret 

S = "ababcbacadefegdehijhklij"
test = Solution()
ret = test.partitionLabels(S)
print(ret)