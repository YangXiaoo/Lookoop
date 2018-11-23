'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

# 2018-11-23
# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicts = {}
        for i in nums:
            dicts[i] = dicts.get(i, 0) + 1
        print(dicts)
        sort = sorted(dicts.items(),key = lambda x:x[1],reverse = True)
        res = []
        for i in range(k):
            res.append(sort[i][0])
        return res

nums = [1]
k = 1
test = Solution()
res = test.topKFrequent(nums, k)
print(res)


        