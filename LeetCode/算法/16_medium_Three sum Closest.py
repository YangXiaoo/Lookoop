'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

[-1,2,1,-4],-1 ===> -1
'''

# 2018-6-17
# Three Sum Closest
class Solution1:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        if len(nums) < 3:
            return res
        elif len(nums) == 3:
            return nums[0]+nums[1]+nums[2]
        nums = sorted(nums)
        print(nums)
        sums = 999
        lens = len(nums)
        i = 0
        while i < len(nums)-2:
            l = i + 1
            r = lens - 1
            while l < r:
                # print(nums[i],nums[l],nums[r],sums)
                if nums[l] + nums[r] < (target-nums[i]):
                    if abs(nums[i] + nums[l] + nums[r] - target) < sums:
                        sums = abs(nums[i] + nums[l] + nums[r] - target)
                        fir = nums[i]
                        sec = nums[l]
                        thrd = nums[r]                        
                    l += 1
                elif nums[l] + nums[r] > (target-nums[i]):
                    if abs(nums[i] + nums[l] + nums[r] - target) < sums:
                        sums = abs(nums[i] + nums[l] + nums[r] - target)
                        fir = nums[i]
                        sec = nums[l]
                        thrd = nums[r] 
                    r -= 1
                else:
                    sums = abs(nums[i] + nums[l] + nums[r] - target)
                    fir = nums[i]
                    sec = nums[l]
                    thrd = nums[r]
                    l += 1
                    r -= 1
                # print(nums[i],nums[l],nums[r],sums)
            i += 1
        # print(fir,sec,thrd)
        res.append(fir)
        res.append(sec)
        res.append(thrd)
        sums = fir + sec + thrd
        return sums





m = [[-1, 2, 1, -4],[0,0,0,0],[0,1,2],[1,1,1,1],[0,0,0],[4,-1,-4,4],[-1,2,1,-4]]
nums = [4,-1,-4,4]
test = Solution1()
# for m in m:
res = test.threeSumClosest(nums,-1)
print ("new____",res)