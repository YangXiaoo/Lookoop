"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10


[3,5,5,2,5,5,6,6,4,4,1,1,2,5,5,6,6,4,1,3] => 24
"""


# 2018-6-27
# Largest Rectangle in Histogram
# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
class Solution1:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
                print(i,stack,ans,h,w)
            stack.append(i)
        heights.pop()
        return ans



# TLE
class Solution2:
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
        print(tmp,s)
        if s == len(heights):
            return 
        i = s
        c = 1
        max_area = 0
        while i < len(heights):
            new_area = min(heights[s:i+1]) * c
            print(min(heights[s:i+1]))
            if new_area > max_area:
                max_area = new_area

            i += 1
            c += 1
        tmp.append(max_area)
        self.subhandle(heights,s+1,tmp)

# test
h = [9046155,17522430,44186957,40374643,77652689,89027934,97586333,68834337,62979669,1783127,29339118,83907628]
test = Solution2()
res = test.largestRectangleArea(h)
print(res)
"""
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)


We have discussed a Divide and Conquer based O(nLogn) solution for this problem. In this post, O(n) time solution is discussed. Like the previous post, width of all bars is assumed to be 1 for simplicity. For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle. If we calculate such area for every bar ‘x’ and find the maximum of all areas, our task is done. How to calculate area with ‘x’ as smallest bar? We need to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index of first smaller bar on right of ‘x’. Let us call these indexes as ‘left index’ and ‘right index’ respectively.
We traverse all bars from left to right, maintain a stack of bars. Every bar is pushed to stack once. A bar is popped from stack when a bar of smaller height is seen. When a bar is popped, we calculate the area with the popped bar as smallest bar. How do we get left and right indexes of the popped bar – the current index tells us the ‘right index’ and index of previous item in stack is the ‘left index’. Following is the complete algorithm.



1) Create an empty stack.

2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
……a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
……b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).

3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.
"""