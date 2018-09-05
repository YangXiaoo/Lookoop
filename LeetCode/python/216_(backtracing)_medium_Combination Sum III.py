'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

# 2018-9-5
# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/discuss/60636/Concise-python-solution-using-DFS

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(k, n, [], 1)

        return self.res

    def dfs(self, k, n, tmp, p):
        sums = sum(tmp)
        if len(tmp) == k and sums == n:
            if tmp not in self.res:
                self.res.append(tmp[:])

        for i in range(p, 10):
            tmp.append(i)
            self.dfs(k, n, tmp, i + 1)
            tmp.pop()




k = 3
n = 9
test = Solution()
r = test.combinationSum3(k, n)
print(r)