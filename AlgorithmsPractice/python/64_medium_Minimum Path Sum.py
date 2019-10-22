"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

# 2018-6-23
# Minimum Path Sum
# record first line and first row's sum inorder to use DP
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
test = Solution()
res = test.minPathSum(grid)
print(res)