'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

# 2018-11-12
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # misunderstanding
        # left = 0
        # max_len = 0
        # pre = nums[0] - 1
        # for i in range(len(nums)):
        #     if nums[i] < pre:
        #         if i - left > max_len:
        #             max_len = i - left
        #         left = i 
        #     pre = nums[i]
        # if i - left > max_len:
        #     max_len = i - left
        # return max_len

        # # 20 / 24 test cases passed.
        # # [10,9,2,5,3,4]
        # max_len = 1
        # len_nums = len(nums)
        # for i in range(len_nums):
        #     tmp_nums = [nums[i]]
        #     for j in range(i, len_nums):
        #         print(nums[j], tmp_nums)
        #         if nums[j] > tmp_nums[-1]:
        #             tmp_nums.append(nums[j])
        #     tmp_len = len(tmp_nums)
        #     if tmp_len > max_len:
        #         max_len = tmp_len
        # return max_len

        # # Time Limited Exceed 
        # # 21 / 24 test cases passed.
        # max_len = 0
        # len_nums = len(nums)
        # for i in range(len_nums):
        #     tmp_nums = [[nums[i]]]
        #     for j in range(i, len_nums):
        #         for k,v in enumerate(tmp_nums):
        #             if nums[j] > v[-1]:
        #                 tmp = v.copy()
        #                 tmp.append(nums[j])
        #                 tmp_nums.append(tmp)
        #     for k in tmp_nums:
        #         tmp_len = len(k)
        #         if tmp_len > max_len:
        #             max_len = tmp_len
        # return max_len

        max_len = 0
        len_nums = len(nums)
        for i in range(len_nums):
            tmp_nums = [nums[i]]
            for j in range(i, len_nums):
                for k,v in enumerate(tmp_nums):
                    if nums[j] > v[-1]:
                        tmp = v.copy()
                        tmp.append(nums[j])
                        tmp_nums.append(tmp)
            tmp_len = len(tmp_nums)
            if tmp_len > max_len:
                max_len = tmp_len
        return max_len
nums = [10,9,2,5,3,4]
test = Solution()
res = test.lengthOfLIS(nums)
print(res)
