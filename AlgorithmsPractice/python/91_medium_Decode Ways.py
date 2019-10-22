"""

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# 2018-6-27
# Decode Ways
# https://www.jianshu.com/p/5a604070cd11


# Solution1: DFS
class Solution1:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        self.res = 0
        self.dfs(s)
        # print(self.res)
        return self.res

        return res

    def dfs(self,s):
        if len(s) > 0:
            if self.isvalid(s[:1]):
                self.dfs(s[1:])
            else:
                return

        if len(s) > 1:
            if self.isvalid(s[:2]):
                self.dfs(s[2:])
            else:
                return 
        if len(s) == 0:
            self.res += 1

        return self.res

    def isvalid(self,strs):
        if strs[0] == "0":
            return False

        if len(strs) == 1:
            nums = int(strs[0])
        else:
            nums = int(strs[0]) * 10 + int(strs[1])

        return nums<=26 and nums>=1



# Solution2: DP
class Solution2:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """      
        dp = [0]*(len(s)+1)
        # 1 dp[0] = 0 # first item is 0
        # 2 dp[1] = 1 if s[1] is valid else return 0
        # 3 dp[n] = dp[n-1] + dp[n-2]

        # 最后一位不一定有效，所以第三步需要判断两种情况，最后一个有效和最后两位组合有效
        # 此时： dp[n] += dp[n-1] if s[n] is valid 
        #        dp[n] == dp[n-2] if s[n]+s[n-1] is valid

        # 当n只有两位时，若这两位才可以组合则dp[2] = 0, 这时需要做判断 dp[n] += (n-2 == 0)? 1 : dp[n-2]

        if len(s) >= 1:
            if self.isvalid(s[0]):
                dp[1] = 1
            else:
                return 0

        for n in range(1,len(s)):
            if self.isvalid(s[n]):
                dp[n+1] += dp[n]

            if self.isvalid(s[n-1],s[n]):
                dp[n+1] += 1 if n-1 == 0 else dp[n-1]
        # print(dp)
        return dp[len(s)]

    def isvalid(self,s1,s2=""):
        if s2 == "":
            if s1 == "0":
                return False
            nums = int(s1)
            return nums<=26 and nums>=1
        else:
            if s1 == "0":
                return False
            nums = int(s1)*10 + int(s2)
            return nums<=26 and nums>=1


# DP Solution2的简写方法
class Solution3:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        dp = [1] + [0] * l
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(1, l):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if s[i - 1] != '0' and int(s[i - 1:i + 1]) < 27:
                dp[i + 1] += dp[i - 1]
        return dp[-1]
        
# test
s = "226"
test = Solution2()
res = test.numDecodings(s)
print(res)