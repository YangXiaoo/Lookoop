'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

# 2018-10-2
# 204. Count Primes
# https://leetcode.com/problems/count-primes/description/

# TLE 17/20
class Solution1(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n):
            is_prime = True
            if i % 2 == 0 and i != 2:
                continue
            j = i - 1
            if i == 1: is_prime = False
            while j > 1:
                if i % j == 0:
                    is_prime = False
                    break
                j -= 1
            if is_prime:
                res += 1

        return res

# TLE 19/20
class Solution2(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n):
            is_prime = True
            j = 3
            if i % 2 == 0 and i != 2:
                continue
            while j * j <= i:
                if i % j == 0:
                    is_prime = False
                    j += 2
                    break
                j += 2
            if is_prime: res += 1
        return res
        res = 0
        # for i in range(1, n, 2):
        #     is_prime = True
        #     j = 3
        #     if i % 2 == 0 and (i != 2 or i < 2):
        #         continue
        #     while j * j <= i:
        #         if i % j == 0:
        #             is_prime = False
        #             j += 2
        #             break
        #         j += 2
        #     if is_prime: res += 1
        # return res


# AC
class Solution3(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = [0 for _ in range(n)]
        c = 0
        i = 2
        while i < n:
            if visited[i] == 0:
                c += 1
                for j in range(i, n, i):
                    visited[j] = 1
            i += 1
        return c

n = 150000
# n = 10 , res =  2, 3, 5, 7.
test = Solution3()
res = test.countPrimes(n)
print(res)