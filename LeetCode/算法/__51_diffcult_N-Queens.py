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
class Solution1:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, index):
        # print(nums,index)
        if index == len(nums):
            self.save_result(nums)
            return
        for i in range(len(nums)):
            nums[index] = i
            # print(nums)
            if self.is_valid(nums, index):
                self.dfs(nums, index+1)

    def is_valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[i] - nums[n]) == n - i:
                return False
        return True

    def save_result(self, nums):
        print(nums)
        board, row, n = [], [], len(nums)
        for q_pos in nums:
            for i in range(n):
                if i != q_pos:
                    row.append('.')
                else:
                    row.append('Q')
            board.append(''.join(row))
            row[:] = []
        self.res.append(board[:])


# state 存放每行皇后所在列
class Solution2:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        state = [-1]*n
        self.helper(state,0) # 从第一行开始   
        return self.res

    def helper(self,state,row):
        if row == len(state):
            self.save(state)
        for col in range(n):
            if self.isValid(state,row,col):
                state[row] = col
                self.helper(state,row+1)
                state[row] -= 1

    def isValid(self,state,row,col):
        # print(row,col)
        for i in range(row):
            # 判断列不出现重复，对角线不出现重复
            if state[i] == col or abs(row - i) == abs(col - state[i]): # 关键
                return False
        return True

    def save(self,state):
        # print(state)
        board, row, n = [], [], len(state)
        for q_pos in state:
            for i in range(n):
                if i != q_pos:
                    row.append('.')
                else:
                    row.append('Q')
            board.append(''.join(row))
            row[:] = []
        self.res.append(board[:])

# test
n = 4
test = Solution2()
r = test.solveNQueens(n)
print(r)