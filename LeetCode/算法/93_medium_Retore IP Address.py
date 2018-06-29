"""

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

input: "010010"
output: ["0.10.0.10","0.100.1.0"]
最大为255.255.255.255
"""

# 2018-6-29
# Restore IP Address
# DFS
# LTE
class Solution1:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12 or len(s)<4:
            return []
        self.res = []
        self.dfs(s,[],0)
        return self.res

    def dfs(self,s,tmp,index):
        if len(tmp) == 4 and index == len(s) and self.isvalid(tmp):
            self.res.append(".".join(tmp))
        else:
            i = 0
            while i <= 3 and index + i < len(s):
                i += 1
                if self.isvalid(tmp):
                    tmp.append(s[index:index+i])
                    self.dfs(s,tmp,index+i)
                    tmp.pop()


    def isvalid(self,tmp):
        for i in tmp:
            if len(i) > 1:
                if  i[0] == "0":
                    return False
            try:
                if int(i) > 255:
                    return False
            except:
                return False
        return True  

# https://blog.csdn.net/wzy_1988/article/details/23137589
class Solution2:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12 or len(s) < 4:
            return []

        self.res = []
        self.dfs(s,[],0)
        return self.res

    def dfs(self,s,tmp,index):
        if len(tmp) == 4 and index == len(s):
            self.res.append(".".join(tmp))
        else:
            i = 0
            while i <= 3 and index + i < len(s):
                i += 1
                if self.isvalid(s[index:index+i]):
                    tmp.append(s[index:index+i])
                    self.dfs(s,tmp,index+i)
                    tmp.pop()

    def isvalid(self,s):
        if len(s) > 1 and s[0] == "0":
            return False
        return int(s) < 256


# test
s = "25525511135"
test = Solution2()
res = test.restoreIpAddresses(s)
print(res)

