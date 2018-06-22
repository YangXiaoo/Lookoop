"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

Input: "a  "
Output: 1
"""

# 2018-6-22
# Length of Last Word
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip(' ').split(' ')[-1])

s = "a  "
test = Solution()
res = test.lengthOfLastWord(s)
print(res)
s = s.rstrip(' ')
print(s,"-",s.split(' '))