/* 
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# 用动态规划解决解题问题时所使用的字典类似于memoization
class Solution():
    def stair(self,n,dic):
        if n < 1: return 0
        if n == 1: return 1
        if n == 2: return 2
        if n in dic:
            return dic[n]
        else:
            value = self.stair(n-1,dic) + self.stair(n-2,dic)
            dic[n] = value
            return value

===================================================================
*/
// 2018-8-29
// In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again
// 329. Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
class Solution {
    vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int res = 1;
        int row = matrix.size();
        if (row == 0) return 0;
        int col = matrix[0].size();
        vector<vector<int>> visit(row, vector<int>(col, 0));
        // 遍历每个点
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                int tmp = dfs(matrix, visit, row, col, i, j);
                res = max(tmp, res);
            }
        }
        return res;
    } // end ~ longestIncreasingPath

    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& visit, int row, int col, int i, int j)
    {
        // 若点(i, j)已经别访问过则直接返回结果
        // 利用visit来缓存结果
        if (visit[i][j] > 0) return visit[i][j];
        int tmpRes = 1;
        for (auto dir : directions)
        {
            // 向下一个点移动、
            int x = i + dir[0], y = j + dir[1];
            if (x < 0 || x >= row || y < 0 || y >= col || matrix[i][j] >= matrix[x][y])
                continue;
            tmpRes = max(tmpRes, dfs(matrix, visit, row, col, x, y)+1);
        }
        // 若点(i,j)有可行路径则上面for循环会使tmpRes的值大于1，否则不经历循环，并且该点的值依然为其本身
        visit[i][j] = tmpRes;
        return tmpRes;
    }
};