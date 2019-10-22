'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

# 2018-10-30
# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmp, res = [], []
        if len(nums) == 0:
            return []
        if len(nums) < 2:
            return [str(nums[0])]
        tmp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] - tmp[-1] != 1:
                self.addToAns(res, tmp)
                tmp = []
            tmp.append(nums[i])
        self.addToAns(res, tmp)

        return res   

    def addToAns(self, res, tmp):
        if len(tmp) > 1:
            res.append(str(tmp[0]) + '->' + str(tmp[-1]))
        else:
            res.append(str(tmp[0]))

nums = [0,2,3,4,6,8,9]
test = Solution()
res = test.summaryRanges(nums)
print(res)