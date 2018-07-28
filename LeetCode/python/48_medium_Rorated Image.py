"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
# 2018-6-21
# Rorated Image
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        :example
        """
        L = len(matrix) - 1
        for s in range((L+1)//2): # Number of squares to rotate. E.g. A 4x4 matrix has 2 squares to rotate
            for i in range(s,L-s,1): # Loop on rotating 4 points at a time to get a 90-degree rotation
                # print(matrix[i][L-s], matrix[s][i])
                # the colum of point 2 in a i loop will not change
                # the row of point 1 in a i loop will not change
                matrix[s][i], matrix[i][L-s] = matrix[i][L-s], matrix[s][i] # Swapping corresponding 1 & 2

                # the colum of point 4 in a i loop will not change
                # the row of point 3 in a i loop will not change
                # print(matrix[L-i][s], matrix[L-s][L-i])
                matrix[L-s][L-i], matrix[L-i][s] = matrix[L-i][s], matrix[L-s][L-i] # Swapping corresponding 3 & 4
                # print(matrix[L-s][L-i], matrix[s][i])
                matrix[s][i], matrix[L-s][L-i] = matrix[L-s][L-i], matrix[s][i] # Swapping corresponding 4 & 1
                # Combination of these 3 swaps is equivalent to 90 degree rotation for 4 points
                # Will repeate this for Length - 1 on each square 

        return matrix

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

test = Solution()
r = test.rotate(matrix)
print(r)
