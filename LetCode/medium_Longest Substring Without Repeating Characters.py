'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Seen this question in a real interview before?  YesNo

####################################
I also give max substring....

'''

# 2018-6-14
# Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = []
        res = []
        for char in s:
            if char not in chars:
                chars.append(char)
                if len(chars) == len(s):
                    res = chars
                    return len(res),s
            else:
                res.append(chars)
                ins = chars.index(char)
                if ins == len(chars) - 1:
                    chars = []
                    chars.append(char)
                else:
                    for j in range(0, len(chars)):
                        if char == chars[j]:
                            ins = j 
                            break
                    chars = chars[ins+1:]
                    chars.append(char)
        res.append(chars)
        l = len(res)
        m_l = 0
        for i in range(0,l):
           if len(res[i]) > m_l:
                m_l = len(res[i])
                max_res = res[i]
        for m in max_res:
            max_str += m
        return m_l,max_str

strs="pdw4gfffs"
test = Solution()
leng,res = test.lengthOfLongestSubstring(strs)
print("Given \"%s\", the answer is \"%s\", with the length of %s." % (strs,res,leng))
