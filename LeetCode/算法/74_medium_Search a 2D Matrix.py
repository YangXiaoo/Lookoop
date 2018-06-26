"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

# 2018-6-26
# Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0: return False
        col = len(matrix[0])
        left = 0
        right = col-1
        bl = 0
        br = row-1
        k = (bl+br)//2
        # print(left,right,bl,br)
        while left <= right and bl <= br:
            mid = (right+left)//2
            k = (bl+br)//2
            
            if matrix[k][mid] == target:
                return True
            if matrix[k][left] <= target and matrix[k][right] >= target:
                if target < matrix[k][mid]:
                    right = mid
                else:
                    left = mid + 1

            if matrix[k][left] > target:
                br = k - 1
            if matrix[k][right] < target:
                bl = k + 1
                
            # print(k,left,right,mid,bl,br)

        return False




# test
matrix = [[1]]   
target = 5
test = Solution()
res = test.searchMatrix(matrix,target)
print(res)