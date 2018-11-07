'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

# 2018-11-6
# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/

# Time Limit Exceeded/ 112
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        nums = []
        for i in range(1, n):
            if i * i <= n:
                nums.append(i**2)
            else:
                break
        # print(nums)
        res = []
        self.dp(nums, n, [], 0, res)
        # print(res)
        return min(res)

    def dp(self, nums, n, tmp, index, res):
        total = sum(tmp)
        # print(res)
        if total == n:
            len_tmp = len(tmp)
            res.append(len_tmp)
        else:
            for i in range(index, len(nums)):
                if sum(tmp) + nums[i] > n:
                    break
                tmp.append(nums[i])
                self.dp(nums, n, tmp, i, res)
                tmp.pop()


# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
class Solution2:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        nums = []
        for i in range(1, n):
            if i * i <= n:
                nums.append(i**2)
            else:
                break
        check = [n]
        ret = 0
        while check:
            ret += 1
            tmp = set()
            for x in check:
                for y in nums:
                    if x == y:
                        return ret 
                    if x < y:
                        break
                    tmp.add(x - y)
            check = tmp
        return ret



n = 112
test = Solution2()
res = test.numSquares(n)
print(res)