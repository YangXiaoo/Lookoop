"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

# 2018-6-21
# N-Queens II
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
n = 4
test = Solution1()
r = test.solveNQueens(n)
print(r)