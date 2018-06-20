'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''
# 2018-6-20
# Count and Say
# it can also use loop to resolve
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.subHandle(1,n,'1')

    def subHandle(self,s,n,r):
        if s >= n:
            return r
        i = 0
        r += '#'
        tmp = ''
        c = 1
        while i < len(r) - 1:
            if r[i] == r[i+1]:
                c += 1
            else:
                tmp += str(c) + r[i]
                c = 1
            i += 1
        # print(s,n,r,tmp)
        r = tmp
        return self.subHandle(s+1,n,r)

n = 20
test = Solution()
res = test.countAndSay(n)
print(res)
