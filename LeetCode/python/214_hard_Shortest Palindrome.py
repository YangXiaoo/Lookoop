'''
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
'''

# 2018-10-10
# 214. Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/description/

# 119 / 120 test cases passed.
# Time Limit Exceeded
class Solution1:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 得到每个点为中心的回文子串
        len_s = len(s)
        if not len_s:
            return ""
        palindrome_single = []
        palindrome_double = []
        for i in range(len_s):
            j = 1
            while i - j >= 0 and i + j < len_s:
                if s[i - j : i + j + 1] == s[i - j : i + j + 1][::-1]:
                    j += 1
                else:
                    break
            d = 1
            while i - d >= 0 and i + d < len_s:
                if s[i - d : i + d + 2] == s[i - d : i + d + 2][::-1]:
                    d += 1
                else:
                    break
            palindrome_single.append(j-1)
            palindrome_double.append(d-1)
        # print(palindrome)
        # print(palindrome_double, palindrome_single)
        mid = len_s // 2

        # 奇数
        mark = 0
        for i in range(mid, -1, -1):
            if palindrome_single[i] == i:
                mark = i 
                break
        single = "".join(s[mark:][::-1]) + "".join(s[mark+1:])

        # 偶数
        mark = 0
        for i in range(mid, -1, -1):
            if palindrome_double[i] == i:
                mark = i 
                break
        double = "".join(s[mark+2:][::-1]) + "".join(s[mark:])
        if len(double) < len(single) and double[:]==double[::-1] and len(double) >= len_s: # len(double) >= len_s for "aaaaa"
            return double
        return single

class Solution2:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if not len_s:
            return ""
        start, max_len = 0, 0
        palindrome = [0 for _ in range(len_s)]
        for i in range(len_s):
            if i - max_len >= 0 and s[i - max_len : i + 1] == s[i - max_len : i + 1][::-1]:
                start = i - max_len
                max_len += 1
                if start == 0:
                    palindrome[i] = max_len
            if i - max_len - 1 >= 0 and s[i - max_len - 1 : i + 1] == s[i - max_len - 1 : i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                if start == 0:
                    palindrome[i] = max_len
        max_index = palindrome.index(max(palindrome))
        return "".join(s[max_index + 1:][::-1]) + "".join(s[:])

class Solution3:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
s = "abbacd"
test = Solution3()
res = test.shortestPalindrome(s)
print(res)