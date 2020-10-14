"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

# 2020-10-14
# https://www.cnblogs.com/grandyang/p/5185561.html

class Solution():
	def lengthOfLongestSubstringKDistinct(self, s, k):
		charMap, left, ret = {}, 0, 0
		for i in range(len(s)):
			charMap[s[i]] = i 
			while len(charMap.keys()) > k:
				print("charMap[s[left]]: {}".format(charMap[s[left]]))
				if charMap[s[left]] == left:
					charMap.pop(s[left])
				left += 1

			ret = max(ret, i - left + 1)

		return ret 

s = "aa"
k = 1
test = Solution()
ret = test.lengthOfLongestSubstringKDistinct(s, k)
print(ret)
# help(dict)
