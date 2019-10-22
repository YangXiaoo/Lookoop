'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

# 2018-9-28
# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

# 连通区域

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        island = 0
        for rr in range(row):
            for cc in range(col):
                # BFS
                queue = []
                if visited[rr][cc] or grid[rr][cc] == "0":
                    continue
                else:
                    queue.append([rr, cc])
                    island += 1
                    visited[rr][cc] = True
                    while len(queue) != 0:
                        r, c = queue.pop()
                        if r - 1 >= 0 and not visited[r - 1][c] and grid[r - 1][c] == "1":
                            queue.append([r - 1, c])
                            visited[r - 1][c] = True

                        if r + 1 < row and not visited[r + 1][c] and grid[r + 1][c] == "1":
                            queue.append([r + 1, c])
                            visited[r + 1][c] = True

                        if c - 1 >= 0 and not visited[r][c - 1] and grid[r][c - 1] == "1":
                            queue.append([r, c - 1])
                            visited[r][c - 1] = True

                        if c + 1 < col and not visited[r][c + 1] and grid[r][c + 1] == "1":
                            queue.append([r, c + 1])
                            visited[r][c + 1] = True

        return island

class Solution2(object):
    def isLand(self, row, col, grid):
        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.isLand(row-1, col, grid) if row > 0 else None
            self.isLand(row+1, col, grid) if row < len(grid)-1 else None
            self.isLand(row, col-1, grid) if col > 0 else None
            self.isLand(row, col+1, grid) if col < len(grid[0])-1 else None
            return True
        return False
                
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isLand(i, j, grid):
                    count += 1                    
        return count

grid = [["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]

test = Solution()
res = test.numIslands(grid)
print(res)