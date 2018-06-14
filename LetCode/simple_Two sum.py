# 2018-6-12
# Two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        leng = len(nums)
        i = 0
        while i < leng - 1:
            j = i + 1
            while j < leng:
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
                j += 1
            i += 1
        return -1
nums = [3,2,4]
target = 6
s = Solution()
r = s.twoSum(nums,target)
print(r)