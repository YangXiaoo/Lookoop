"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

# 2018-6-22
# Unique Path
# daynamic programing
# 状态转移公式：ways[i][j] = ways[i][j-1] + ways[i-1][j]
# recrusion O(m^n)
class Solution1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1: return 1
        return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)


#对于起点到点(i,j)的路径总数：ways[j]= 起点到点(i-1, j) 的路径总数：ways[j] + 起点到点(i, j-1)的路径总数 ways[j-1]，于是我们就得到递推式：ways[j] = ways[j] + ways[j-1]
class Solution2(object):  
    def uniquePaths(self, m, n):  
        """ 
        :type m: int 
        :type n: int 
        :rtype: int 
        """  
        ways = [0]*n  
        ways[0] = 1  
        for i in range(m) :  
            for j in range(1, n) :  
                ways[j] += ways[j-1]  
        return ways[n-1]  


m = 3
n = 2
test = Solution2()
res = test.uniquePaths(m,n)
print(res)