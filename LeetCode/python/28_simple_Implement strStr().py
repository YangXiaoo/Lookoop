'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

# 2018-6-19
#  Implement strStr()
# 超过内存限制
# KMP，自动机等可以实现
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        i = 0
        index = -1
        while i < len(haystack):
            j = 0
            while j < len(needle) and i+j < len(haystack):
                if haystack[i+j] == needle[j]:
                    j += 1
                    index = i
                else:
                    index = -1
                    break
                if j == len(needle):
                    return index
                else:
                    index = -1
            i += 1
        return index    

# test
haystack = "lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll"
needle = "lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll"
test = Solution()
res = test.strStr(haystack,needle)
print(res)