"""

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

# 2018-6-27
# Combination
class Solution1:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k: return []
        res = self.dfs(n,[],[],k,1)
        return res
    def dfs(self,n,res,tmp,k,s):
        if len(tmp) == k:
            res.append(tmp[:])
            return
        else:
            for i in range(s,n+1):
                tmp.append(i)
                self.dfs(n,res,tmp,k,i+1)
                tmp.pop()
        return res

from itertools import combinations

class Solution2:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))
        
n = 4
k = 2
test = Solution()
res = test.combine(n,k)
print(res)