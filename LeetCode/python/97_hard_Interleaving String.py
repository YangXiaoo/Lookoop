"""

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""

# 2018-6-29
# Interleaving String
# https://leetcode.com/articles/interleaving-strings/
# https://blog.csdn.net/ljiabin/article/details/44518553
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp = [[True]*(len(s1)+1)]*(len(s2)+1)
        # print(dp)
        for i in range(len(s1)+1):
        	for j in range(len(s2)+1):
        		if i == 0 and j == 0:
        			dp[i][j] = True
        		elif i == 0:
        			dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
        		elif j == 0:
        			dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
        		else:
        			dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or(dp[i-1][j-1] and s2[j-1] == s3[i+j-1])

        # print(dp)
        return dp[-1][-1]


# test
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
test = Solution()
res = test.isInterleave(s1,s2,s3)
print(res)