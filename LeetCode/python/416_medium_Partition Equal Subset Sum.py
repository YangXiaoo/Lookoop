'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

# 2019-3-15
# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/


# import collections
# d = collections.deque()
# import heapq


# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90607/My-Simple-C%2B%2B-DP-Code-with-Comments
class Solution:
    def canPartition(self, nums):
        _sum = sum(nums)
        possible = {0}
        for n in nums:
            possible.update({(v + n) for v in possible})

        return (_sum / 2)  in possible


# bool canPartition(vector<int>& nums) {
#     int sum = accumulate(nums.begin(), nums.end(), 0), target = sum >> 1;
#     if (sum & 1) return false;
#     vector<int> dp(target + 1, 0);
#     dp[0] = 1;
#     for(auto num : nums) 
#         for(int i = target; i >= num; i--)
#             dp[i] = dp[i] || dp[i - num];
#     return dp[target];
# }


nums = [[1, 5, 11, 5],
        [1, 2, 3, 5]]

test = Solution()
for n in nums:
    ret = test.canPartition(n)
    print(ret)