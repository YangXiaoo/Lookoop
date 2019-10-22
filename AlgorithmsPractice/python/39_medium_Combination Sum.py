'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
# 2018-6-20
# Combination Sum
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        # print(candidates)
        return self.dfs(candidates,target,[],[],0)
        
        
        
    def dfs(self,candidates,target,tmp,res,pos):
        #print(sums,tmp,res,pos)
        sums = sum(tmp)
        if sums == target:
            res.append(tmp[:])
            # print(res)
        else:
            for p in range(pos,len(candidates)):
                if sums + candidates[p] > target:
                    break
                tmp.append(candidates[p])
                self.dfs(candidates,target,tmp,res,p)
                tmp.pop()
        return res       


class Solution2(object):
    def _combination_sum(self, xs, q, subset, res, i):
        partial = sum(subset)
        if partial == q:
            res.append(subset[:])
        else:
            for j in range(i, len(xs)):
                if partial+xs[j] > q:
                    break
                subset.append(xs[j])
                self._combination_sum(xs, q, subset, res, j)
                subset.pop()
        return res

    def combinationSum(self, xs, q):
        xs.sort()
        return self._combination_sum(xs, q, [], [], 0)



candidates = [8,7,4,3]
target = 11
test = Solution()
res = test.combinationSum(candidates,target)
print(res)