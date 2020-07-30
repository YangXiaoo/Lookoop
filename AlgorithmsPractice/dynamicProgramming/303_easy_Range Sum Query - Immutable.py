# coding:utf-8

"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

# 2020-7-30
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sumRecord = []
        self.initSum()
        
    def initSum(self):
        self.sumRecord = [0 for _ in range(len(self.nums))]
        for i in range(len(self.nums)):
            self.sumRecord[i] = self.nums[i]
            if i > 0:
                self.sumRecord[i] += self.sumRecord[i-1]
                
        self.sumRecord.append(0)
                

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRecord[j] - self.sumRecord[i-1]
        
nums = [-2, 0, 3, -5, 2, -1]
query = [
	[0,2],	# 1
	[2,5],	# -1
	[0,5]	# -3
]

test = NumArray(nums)
for q in query:
	ret = test.sumRange(q[0], q[1])
	print(ret)