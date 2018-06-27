"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# 2018-6-27
# Subsets
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.dfs(nums,[],[],0,0)
        return res
    def dfs(self,nums,res,tmp,k,iters):
        res.append(tmp[:])
        if k == len(nums):
            return
        else:
            for i in range(iters,len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                self.dfs(nums,res,tmp,k+1,i)
                tmp.pop()
        return res

nums = [1,2,3]
test = Solution()
res = test.subsets(nums)
print(res)