'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''

# 2018-6-16
# Palindrome number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        lens = len(x)
        if x[0:lens] == x[0:lens][::-1]:
        	return True
        else:
        	return False

# test
x = -121
test = Solution()
res = test.isPalindrome(x)
if res:
	print("Yes")
else:
	print("Not palindrome!")