'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''
# 2018-6-20
# Sudoku Solver
# DFS
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        unfilled = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    unfilled.append((i, j))
        found = [False]
        # print(unfilled)
        self.dfs(board, unfilled, 0, found)
        return
        
        
        
    def dfs(self, board, unfilled, i, found):
        if i == len(unfilled): # 如果填满则返回结果
            found[0] = True
            return
        s, t = unfilled[i]
        for k in range(1, 10, 1):
            board[s][t] = str(k)
            if self.isValidAdd(board):
                self.dfs(board, unfilled, i + 1, found)
            if found[0] == False:
                board[s][t] = '.'
            else:
                break
        return
        
        
    def isValidAdd(self, board):
        dic_row = [{},{},{},{},{},{},{},{},{}]
        dic_col = [{},{},{},{},{},{},{},{},{}]
        dic_box = [{},{},{},{},{},{},{},{},{}]
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3*(i//3)+(j//3)][num] = 1
                else:
                    return False
        #print(dic_row)
        #print(dic_col)
        #print(dic_box)

        return True      

        
        
class Solution2:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        unfilled = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    unfilled.append((i, j))
        found = [False]
        self.dfs(board, unfilled, 0, found)
        return

    def dfs(self, board, unfilled, i, found):
        # print(board)
        if i == len(unfilled): # 如果填满则返回结果
            found[0] = True
            return
        s, t = unfilled[i]
        for k in range(1, 10, 1):
            board[s][t] = str(k)
            if self.isValidAdd(board, s, t):
            #if self.isValidSudoku(board):
                self.dfs(board, unfilled, i + 1, found)
            if found[0] == False:
                board[s][t] = '.'
            else:
                break
        return
        
        
    def isValidAdd(self, board, s, t):
        dic = {}
        for i in range(1, 10, 1):
            dic[str(i)] = False 
        for j in range(9):
            if board[s][j] != '.':
                if dic[board[s][j]] == False:
                    dic[board[s][j]] = True
                else:
                    return False
        for i in range(1, 10, 1):
            dic[str(i)] = False     
        for i in range(9):
            if board[i][t] != '.':
                if dic[board[i][t]] == False:
                    dic[board[i][t]] = True
                else:
                    return False
        for i in range(1, 10, 1):
            dic[str(i)] = False     
        k = s // 3
        l = t // 3
        for i in range(3):
            for j in range(3):
                # st = set([])
                if board[3 * k + i][3 * l + j] != '.':
                    if dic[board[3 * k + i][3 * l + j]] == False:
                        dic[board[3 * k + i][3 * l + j]] = True
                    else:
                        return False
        return True  

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".",".","."],
  ["8",".",".",".","6",".",".",".","."],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
test= Solution2()
test.solveSudoku(board)
print(board)