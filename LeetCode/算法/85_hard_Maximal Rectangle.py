"""

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

# 2018-6-27
# Maximal Rectangel
# Build on the last question

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = -1
        height = [0]*len(matrix[0])
        area = []
        print(height)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    height[j] = 0
                else:
                    height[j] += 1

            f = last()
            # print(height)
            res =  f.largestRectangleArea(height)
            area.append(res)

        return max(area)
        



class last:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        init = min(heights) * len(heights)
        tmp = []
        tmp.append(init)
        self.subhandle(heights,0,tmp)

        return max(tmp)


    def subhandle(self,heights,s,tmp):
        # print(tmp,s)
        if s == len(heights):
            return 
        i = s
        c = 1
        max_area = 0
        while i < len(heights):
            new_area = min(heights[s:i+1]) * c
            # print(min(heights[s:i+1]))
            if new_area > max_area:
                max_area = new_area

            i += 1
            c += 1
        tmp.append(max_area)
        self.subhandle(heights,s+1,tmp)


# test
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
test = Solution()
res = test.maximalRectangle(matrix)
print(res)