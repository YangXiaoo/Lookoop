"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

#2018-6-22
# Sprial Matrix II
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        row_start,row_end,col_start,col_end = 0,n-1,0,n-1
        num = 1
        while row_start <= row_end and col_start <= col_end:
        	for i in range(col_start,col_end+1):
        		matrix[row_start][i] = num
        		num += 1
        	row_start += 1

        	for j in range(row_start,row_end+1):
        		matrix[j][col_end] = num
        		num += 1
        	col_end -= 1

        	for m in range(col_end,col_start-1,-1):
        		matrix[row_end][m] = num
        		num += 1
        	row_end -= 1

        	for k in range(row_end,row_start-1,-1):
        		matrix[k][col_start] = num
        		num += 1
        	col_start += 1

        return matrix

n = 4
test = Solution()
res = test.generateMatrix(n)
print(res)
