'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

# 2018-10-7
# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/description/

# 30 / 37 test cases passed.
class Solution:
    # def __init__(self):
    #     self.root = {}
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        index, root = 0, {}
        for c in words:
            node = root
            for i in c:
                node = node.setdefault(i,  {})
            node['#'] = index
            index += 1
        print(root)

        row, col, res = len(board), len(board[0]), []
        for r in range(row):
            for c in range(col):
                if board[r][c] in root:
                    visited = [[False for _ in range(col)] for _ in range(row)]
                    queue = []
                    queue.append((r,c))
                    visited[r][c] = True
                    cur_trie = root[board[r][c]]
                    while len(queue) != 0:
                        m, n = queue.pop()
                        if m + 1 < row and not visited[m + 1][n] and board[m + 1][n] in cur_trie:
                            cur_trie = cur_trie[board[m + 1][n]]
                            queue.append((m + 1, n))
                            visited[m + 1][n] = True

                        if m - 1 >= 0 and not visited[m - 1][n] and board[m - 1][n] in cur_trie:
                            cur_trie = cur_trie[board[m - 1][n]]
                            queue.append((m - 1, n))
                            visited[m - 1][n] = True

                        if n + 1 < col and not visited[m][n + 1] and board[m][n + 1] in cur_trie:
                            cur_trie = cur_trie[board[m][n + 1]]
                            queue.append((m, n + 1))
                            visited[m][n + 1] = True

                        if n - 1 >= 0 and not visited[m][n - 1] and board[m][n - 1] in cur_trie:
                            cur_trie = cur_trie[board[m][n - 1]]
                            queue.append((m, n - 1))
                            visited[m][n - 1] = True

                    if '#' in cur_trie:
                        cur_char = words[cur_trie['#']]
                        if cur_char not in res:
                            res.append(cur_char)

        return res

# dfs
class Solution2:
    def __init__(self):
        self.res = []
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        index, root = 0, {}
        for c in words:
            node = root
            for i in c:
                node = node.setdefault(i,  {})
            node['#'] = index
            index += 1
        print(root)

        row, col, res = len(board), len(board[0]), []
        
        for i in range(row):
            for j in range(col):
                visited = [[False for _ in range(col)] for _ in range(row)]
                cur_trie = root[board[i][j]]
                self.dfs(res, board, visited, cur_trie, i, j, row, col, words)

        return self.res

    def dfs(self, res, board, visited, cur_trie, r, c, row, col, words):
        # print(cur_trie)
        if '#' in cur_trie:
            cur_char = words[cur_trie['#']]
            if cur_char not in self.res:
                self.res.append(cur_char)
            return 
        print(board[r][c] not in cur_trie)
        if r < 0 or r >= row or c < 0 or c >= col or visited[r][c]:
            return 

        print("hsand")
        visited[r][c] = True
        #cur_trie = cur_trie[board[r][c]]
        self.dfs(self, res, board, visited, cur_trie[board[r][c]], r + 1, c, row, col, words)
        self.dfs(self, res, board, visited, cur_trie[board[r][c]], r - 1, c, row, col, words)
        self.dfs(self, res, board, visited, cur_trie[board[r][c]], r, c + 1, row, col, words)
        self.dfs(self, res, board, visited, cur_trie[board[r][c]], r, c - 1, row, col, words)
        # visited[r][c] = False



# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
board = [["a","b"],["c","d"]]
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
# error ['acb', 'bd', 'ca', 'db']
test = Solution2()
res = test.findWords(board, words)
print(res)