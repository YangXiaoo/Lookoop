# coding:utf-8

"""
Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
 

Constraints:

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
intervals[i] != intervals[j] for all i != j
"""

# 2020-8-19
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x:x[0])
        
        i = 0
        while i < len(intervals)-1:
            if intervals[i][0] <= intervals[i+1][0] and intervals[i+1][1] <= intervals[i][1]:
                # 后一个在前一个范围内
                del intervals[i+1]
            elif intervals[i+1][0] <= intervals[i][0] and intervals[i][1] <= intervals[i+1][1]:
                # 前一个在后一个范围内
                del intervals[i]
            else:
                i += 1
        
        return len(intervals)
        