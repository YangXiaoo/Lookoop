"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# 2018-6-27
# Subsets II
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums,res,[],0)
        return sorted(res)

    def dfs(self,nums,res,tmp,pos):

        sort = tmp
        sort.sort()
        # print(res,tmp,pos)
        if sort not in res:
            res.append(sort[:])


        for i in range(pos,len(nums)):
            tmp.append(nums[i])
            self.dfs(nums,res,tmp,i+1)
            tmp.pop()



# https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.
class Solution2:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # print(nums)
        res = [[]]
        l = None
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
                print("loop:",i,"--->",res,">>>>>>",res[j],[nums[i]],l)
        return res


# test
nums = [1,3,4,4]
test = Solution2()
res = test.subsetsWithDup(nums)
print(res)
[[], [4], [4, 4], [4, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [1, 1, 4], [1, 1, 4, 4], [1, 4], [1, 1], [1, 4, 4], [1]]
[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
