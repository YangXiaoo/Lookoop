'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
# 2018-6-20
# Combination Sum II
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = self.dfs(candidates,target,[],[],0,[])
        r = []
        for i in res:
            if i not in r:
                r.append(i)
        return r

    def dfs(self,candidates,target,res,tmp,pos,dic):
        # print(res,tmp,dic)
        sums = sum(tmp)
        if target == sums:
            res.append(tmp[:])
        else:
            for i in range(pos,len(candidates)):
                if sums + candidates[i]> target:
                    break
                tmp.append(candidates[i])
                self.dfs(candidates,target,res,tmp,i+1,dic) # i + 1:下一个迭代从下一位开始
                tmp.pop()
        return res


candidates = [10,1,2,7,1,6,5]
target = 8
test = Solution()
res = test.combinationSum2(candidates,target)
print(res)