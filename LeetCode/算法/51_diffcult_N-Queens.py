"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.


Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

# 2018-6-21
# N-Queens
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        lists = []
        i = 0
        while i < n*n:
            if i < n:
                lists.append("Q")
            else:
                lists.append(".")
            i += 1
        print(lists)
        # return self.dfs(lists,n,[],[],pos)

    def dfs(self,n,res,tmp,pos):
        if pos == n:
            res.append(tmp)
        else:
            pass

# test
n = 4
test = Solution()
r = test.solveNQueens(n)