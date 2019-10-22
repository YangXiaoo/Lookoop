"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
# 2018-6-21
# Pernutation
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dfs(nums,[],[],0)

    def dfs(self,nums,res,tmp,pos):
        if len(tmp) == len(nums):
            res.append(tmp[:])
        else:
            for k in range(len(nums)):
                if nums[k] in tmp:
                    continue
                tmp.append(nums[k])
                self.dfs(nums,res,tmp,k+1)
                tmp.pop()
        return res


nums = [1,2,3]
test = Solution()
res = test.permute(nums)
print(res)