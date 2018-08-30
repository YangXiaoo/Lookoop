/* 
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50


===================================================================
*/
// 2018-8-30
// 892. Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/description/


class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int n = grid.size(), res = 0;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // 重叠的立方体面积 area = v * 4 + 2
                if (grid[i][j]) res += grid[i][j] * 4 + 2;

                // 网格中相邻立方重叠面积为 min(v1, v2) * 2. v1,v2为两个相邻网格重叠立方体个数
                // 第一行时只能j - 1
                // 第一列时只能i - 1
                if (i) res -= min(grid[i][j], grid[i - 1][j]) * 2;
                if (j) res -= min(grid[i][j], grid[i][j - 1]) * 2;
            }
        }

        return res;
    }
};