"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

# 2018-6-21
# Pernutation II
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dfs(nums,[],[],0,[])

    def dfs(self,nums,res,tmp,pos,dic):
        if len(tmp) == len(nums) and tmp not in res:
            res.append(tmp[:])
        else:
            for k in range(0,len(nums)):
                if k in dic:
                    continue
                dic.append(k)
                tmp.append(nums[k])
                self.dfs(nums,res,tmp,k,dic)
                tmp.pop()
                dic.pop()
        return res        

nums = [1,1,2]
test = Solution()
res = test.permuteUnique(nums)
print(res)