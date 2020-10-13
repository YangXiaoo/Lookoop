"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""
# 2020-10-13

class Solution():
    def maxSubArrayLen(self, nums, k):
        recordMap = {}
        ret = 0
        sumRecord = 0
        for i in range(len(nums)):
            sumRecord += nums[i]
            if sumRecord == k: ret = max(ret, i + 1)
            if (sumRecord - k in recordMap):
                ret = max(ret, i - recordMap[sumRecord - k])
            if sumRecord not in recordMap: recordMap[sumRecord] = i
        # print(recordMap)
        return ret 

nums, k = [-2, -1, 2, 1], 1
test = Solution()
ret = test.maxSubArrayLen(nums, k)
print(ret)