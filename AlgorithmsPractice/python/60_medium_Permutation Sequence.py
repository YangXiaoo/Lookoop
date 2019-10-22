"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

# 2018-6-22
# Permutation Sequence
# Use backtracing but LTE
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = self.dfs(n,[],[],1)
        r = ''
        for c in res[k-1]:
        	r += str(c)
        return r

    def dfs(self,n,res,tmp,pos):
    	if len(tmp) == n:
    		res.append(tmp[:])
    	else:
    		for k in range(1,n+1):
    			if k in tmp:
    				continue
    			tmp.append(k)
    			self.dfs(n,res,tmp,k)
    			tmp.pop()
    	return res


n = 9
k = 24
test = Solution()
res = test.getPermutation(n,k)
print(res)