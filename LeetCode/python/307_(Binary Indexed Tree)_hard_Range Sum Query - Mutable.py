'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

# 2018-9-2
# 307. Range Sum Query - Mutable
# Binary Indexed Tree

# 关键在于 k -= (k & -k) 和 k += (k & -k), 前者用于update后者用于sum
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.lens = len(nums)
        self.BIT = [0] * (self.lens + 1)
        # map(update, range(self.lens), nums)
        for i in range(self.lens):
            k = i + 1 
            while k <= self.lens:
                self.BIT[k] += nums[i]
                k += (k & -k)

        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.lens:
            self.BIT[i] += diff
            i += (i & -i)
        # print(self.BIT)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        j += 1
        while j > 0:
            res += self.BIT[j]
            j -= (j & -j)
            
        while i > 0:
            res -= self.BIT[i]
            i -= (i & -i)

        return res
        


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
obj.update(1, 2)
obj.update(1, 44)
obj.update(2, 44)

r1 = obj.sumRange(0, 2)
print(r1,obj.nums)