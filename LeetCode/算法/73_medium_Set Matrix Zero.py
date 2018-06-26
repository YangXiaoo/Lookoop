"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# 2018-6-26
# Set Matirx Zero
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        col = len(matrix[0])
        row = len(matrix)

        for r in range(row):
        	if matrix[r][0] == 0: col0 = 0
        	for c in range(1,col):
        		if matrix[r][c] == 0:
        			matrix[r][0] = 0
        			matrix[0][c] = 0

        for r in range(row-1,-1,-1):
        	for c in range(col-1,0,-1):
        		if matrix[r][0] == 0 or matrix[0][c] == 0:
        			matrix[r][c] = 0
        	if col0 == 0:
        		matrix[r][0] = 0

        return matrix
 

#test
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
test = Solution()
res = test.setZeroes(matrix)
print(res)