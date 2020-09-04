"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
# 2020-9-3

class Solution:
    def canPartitionKSubsets(self, nums, k):    # 超时
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def helper(tmpK, curSum, startIndex, visited):
            nonlocal k,nums, target
            # print(tmpK, curSum, startIndex, visited)
            if tmpK == 0: return True
            if target < curSum: return False
            if target == curSum: 
                return helper(tmpK-1, 0, 0, visited)
            
            for i in range(startIndex, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if helper(tmpK, curSum + nums[i], i + 1, visited):
                        return True
                    visited[i] = False
                    
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        visited = [False for _ in nums]
        nums.sort()
        print(nums, target)
        return helper(k, 0, 0, visited)
        
nums = [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2]
k  = 13
test = Solution()
ret = test.canPartitionKSubsets(nums, k)
print(ret)