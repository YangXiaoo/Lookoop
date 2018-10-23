'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
'''

# 2018-10-23
# 223. Rectangle Area
# https://leetcode.com/problems/rectangle-area/

# https://leetcode.com/problems/rectangle-area/discuss/62139/Python-concise-solution.
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_1 = abs(C - A) * abs(D - B)
        area_2 = abs(G - E) * abs(H - F)
        w = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)
        if w <=0 or h <= 0:
        	return area_1 + area_2
        else:
        	return area_1 + area_2 - w * h