"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

Input: [[1,4],[0,4]]
Output: [[0,4]]

Input:
[[1,4],[0,0]]
Expected:
[[0,0],[1,4]]

Input:
[[2,3],[4,5],[6,7],[8,9],[1,10]]
Expected:
[[1,10]]
"""

# 2018-6-21
# Merge Interval
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        print("[{}, {}]".format(self.start, self.end))


# List should be sorted befor handle
class Solution1:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 1 or len(intervals) == 0:
            return intervals
        i = 1
        res,first,second,tmp = [],[],[],[]
        intervals = sorted(intervals, key=lambda i: i.start)
        while i < len(intervals):
            first.append(intervals[i-1].start)
            first.append(intervals[i-1].end)
            second.append(intervals[i].start)
            second.append(intervals[i].end)
            for f in first:
                tmp.append(f)
            for s in second:
                tmp.append(s)
            tmp.sort()
            # print(tmp,first,second)
            if tmp[1] == tmp[2]:
                add = Interval(tmp[0],tmp[-1])
                intervals[i] = add
                intervals.pop(i-1)   
                tmp,first,second = [],[],[]
            elif tmp[0:2] != first and tmp[0:2] != second:
                add = Interval(tmp[0],tmp[-1])
                intervals[i] = add
                intervals.pop(i-1)   
                tmp,first,second = [],[],[]             
            else:
                i += 1
                tmp,first,second = [],[],[]
        return intervals


class Solution2:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        r = sorted(intervals, key=lambda i: i.start)
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return r

class Solution:
    def merge(self, intervals):

        # sort
        intervals.sort(key=lambda item: item[0])

        i = 0
        # no neeed to check the last array
        while (i + 1) < len(intervals):

            curr_a = intervals[i]
            next_a = intervals[i+1]

            # check for overlap
            if curr_a[1] >= next_a[0]:

                # merge
                # we use max coz of such a case: [[1,4],[2,3]]
                # make the last element of the first array be the furthest(largest value)
                intervals[i][1] = max(curr_a[1], next_a[1])

                # delete the second array
                intervals.pop(i+1)

            else:
                i += 1

        return intervals

nums = [[1,3],[2,6],[8,10],[15,18]]
intervals = nums
# for i in nums:
#     add = Interval(i[0],i[1])
#     intervals.append(add)

test = Solution()
res = test.merge(intervals)
print(res)
        