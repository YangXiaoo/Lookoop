"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,9]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# 2018-6-21
# Insert Intervals
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        index = 0
        flag = 0
        res,first,second,tmp = [],[],[],[]
        while i < len(intervals):
            # print("newInterval:",i,newInterval.start,newInterval.end)
            if newInterval.end < intervals[i].start or newInterval.start > intervals[i].end: 
                res.append(intervals[i])
                i += 1
                continue
            first.append(intervals[i].start)
            first.append(intervals[i].end)
            second.append(newInterval.start)
            second.append(newInterval.end)
            for f in first:
                tmp.append(f)
            for s in second:
                tmp.append(s)
            tmp.sort()
            if tmp[1] == tmp[2]:
                newInterval = Interval(tmp[0],tmp[-1]) 
                tmp,first,second = [],[],[]
                if flag == 0:
                    index = i
                    flag = 1
            elif tmp[0:2] != first:
                newInterval = Interval(tmp[0],tmp[-1]) 
                tmp,first,second = [],[],[]
                if flag == 0:
                    flag = 1
                    index = i
            i += 1

        # return res
        # print(index,newInterval,res)
        if len(intervals) == len(res):
            res.append(newInterval)
            return sorted(res, key=lambda i: i.start)
        else:
            res.insert(index,newInterval)
            return sorted(res, key=lambda i: i.start)


            


nums = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,9]
newInterval = Interval(newInterval[0],newInterval[1])
intervals = []
for i in nums:
    add = Interval(i[0],i[1])
    intervals.append(add)

test = Solution()
res = test.insert(intervals,newInterval)
for r in res:
    print(r.start,r.end)