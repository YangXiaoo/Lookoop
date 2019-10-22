'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

# 2018-11-6
# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66139/6-9-lines-C%2B%2BPython-Solutions-with-Explanations
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m, n, r, c = len(matrix), len(matrix[0]), 0, len(matrix[0]) - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True 
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False

matrix = [[]]
target = 0
test = Solution()
res = test.searchMatrix(matrix, target)
print(res)