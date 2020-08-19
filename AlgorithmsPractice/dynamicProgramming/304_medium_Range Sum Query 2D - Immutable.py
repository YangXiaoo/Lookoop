# coding:utf-8

"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

# 2020-7-31
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sumRecord = []
        self.initSum(matrix)

    def initSum(self, matrix):
        import copy
        self.sumRecord = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        lineRecord = copy.deepcopy(self.sumRecord)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                lineRecord[r][c] = matrix[r][c]
                if c > 0:
                    lineRecord[r][c] += lineRecord[r][c-1]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.sumRecord[r][c] = lineRecord[r][c]
                if r > 0:
                    self.sumRecord[r][c] += self.sumRecord[r-1][c]


        # print(self.sumRecord)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        subUp, subLeft, addLeftUp = 0, 0, 0
        if row1 > 0:
            subUp = self.sumRecord[row1-1][col2]
        if col1 > 0:
            subLeft = self.sumRecord[row2][col1-1]

        if row1 > 0 and col1 > 0:
            addLeftUp = self.sumRecord[row1-1][col1-1]

        return self.sumRecord[row2][col2] - subLeft - subUp + addLeftUp
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

query = [
    [2, 1, 4, 3],   # 8
    [1, 1, 2, 2],   # 11
    [1, 2, 2, 4]    # 12
]

test = NumMatrix(matrix)

for q in query:
    ret = test.sumRegion(*q)
    print(ret)