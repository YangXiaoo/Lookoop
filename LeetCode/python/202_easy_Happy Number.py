'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

# 2018-9-30
# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isHappy = True
        maps = []
        while True:
            if n in maps:
                isHappy = False
                break
            maps.append(n)
            if n == 1:
                break
            r = 0
            while n // 10 != 0:
                r += (n % 10) ** 2
                n = n // 10
            r += n ** 2
            n = r

        return isHappy
n = 19
test = Solution()
res = test.isHappy(n)
print(res)
# print(list(str(n)))
# print(4//10)