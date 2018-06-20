'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''

# 2018-6-20
# First Missing Positive
# Error solution
class Solution1:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        nums.sort()
        if len(nums) == 0 or  ( len(nums) == 1 and (nums[0] > 1 or nums[0]<1)) or nums[-1] < 1 or nums[0]>1:
            return 1
        flag = 0
        flag1 = 0
        # print(nums)
        while i < len(nums):
            if nums[i-1] > 0 and flag1 == 0 and nums[i]-nums[i-1]>1:
                if nums[i-1] - 0 > 1 and nums[i-1] >2:
                    return 1
                else:
                    flag1 = 1
            if nums[i] > 0 and flag == 0 and nums[i]-nums[i-1]>1:
                if nums[i] - 0 > 1 and nums[i-1] > 2:
                    if nums[i-1] == 1:
                        return 2
                    else:
                        return 1
                else:
                    flag = 1
            if nums[i] > 0 and nums[i-1]>0:
                if nums[i] - nums[i-1] > 1:
                    return nums[i-1] + 1
            i += 1
        return nums[-1] + 1
class Solution2:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        if len(nums) < 1:
            return ans
        # find max
        max_len = max(nums)
        new_nums = [0]*len(nums)
        print(new_nums)
        for num in nums:
            if  0 < num < len(nums):
                new_nums[num-1] = num
        nums = new_nums
        print(new_nums)
        for num in nums:
            if num == ans:
                ans += 1
        return ans 






nums = [[1,2,0],[-1,10],[2,10],[],[3,4,-1,1],[7,8,9,11,12],[2,1],[2,2],[0,1,1,2,10],[-10,-3,-20,1],[-2,-1,0,1]]
# [-1,100]
test = Solution2()
for nums in nums:
    res = test.firstMissingPositive(nums)
    print(res)