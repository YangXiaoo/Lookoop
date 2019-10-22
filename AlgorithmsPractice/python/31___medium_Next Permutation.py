'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

1　　2　　7　　4　　3　　1
下一个排列为：
1　　3　　1　　2　　4　　7
如果从末尾往前看，数字逐渐变大，到了2时才减小的，
然后我们再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可
'''
# 2018-6-19
# Next Permutation
class Solution1:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1. get the start index of non-increasing sequence from tail
        # 2. swap
        # 3. sort the non-increasing
        if not nums: return nums
        l = len(nums)
        i = l - 2 
        j = l - 1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i] # 直接交换两个数
        nums[i+1:] = sorted(nums[i+1:])
# test
nums = [1,2,5,6,4]
test = Solution1()
test.nextPermutation(nums)
print(nums)