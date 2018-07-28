"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# 2018-6-27
# Word Serch
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,word,i,j,{},0):
                    return True 
        return False 

    def dfs(self,board,word,i,j,visited,pos):
        if pos == len(word):
            return True 
        
        # 结束搜索条件
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or visited.get((i,j)) or word[pos] != board[i][j]:
            return False

        visited[(i,j)] = True
        res = self.dfs(board,word,i+1,j,visited,pos+1) or self.dfs(board,word,i,j+1,visited,pos+1) or self.dfs(board,word,i-1,j,visited,pos+1) or self.dfs(board,word,i,j-1,visited,pos+1)
        visited[(i,j)] = False

        return res

        

# test
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "A"
test = Solution()
res = test.exist(board,word)
print(res)