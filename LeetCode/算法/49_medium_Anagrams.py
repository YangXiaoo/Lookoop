"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
# 2018-6-21
# Anagrams
# TLE
class Solution1:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp = []
        res = []
        sub = []
        check = []
        curr = ''
        i = 0
        while i < len(strs):
            ar = sorted(strs[i])
            sub.append(strs[i])
            tmp.append(ar)
            if ar not in check:
                check.append(ar)
            else:
                strs.pop(i)
                sub = []
                tmp = []
                continue
            j = i + 1
            for n in range(j,len(strs)):
                curr = sorted(sorted(strs[n]))
                if curr in tmp:
                    sub.append(strs[n])
            # print(tmp,sub,check)
            res.append(sub)
            sub = []
            tmp = []
        return res

class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for s in strs:
            sorted_key = ''.join(sorted(s))
            if sorted_key in dic:
                dic[sorted_key].append(s)
            else:
                dic[sorted_key] = [s]
        return list(dic.values())

# test
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution2()
r = test.groupAnagrams(s)
print(r)