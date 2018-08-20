# 2018-8-1
# Maximum Subarray
# Introduction to Algorithms P41

# LeetCode 53 Maximum Subarray
# 2018-6-21
# Maximun Subarray
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


# Introduction to Algorithms
class MaxSubarray:
    def FindMaxCrossingSubarray(self, A, low, mid, high):
        leftSum = -32767
        sums = 0
        maxLeft = mid
        for i in range(mid, low, -1):
            sums += A[i]
            if sums > leftSum:
                leftSum = sums
                maxLeft = i

        rightSum = -32767
        sums = 0
        maxRight = mid + 1
        for i in range(mid + 1, high):
            sums += A[i]
            if sums > rightSum:
                rightSum = sums
                maxRight = i

        return maxLeft, maxRight, leftSum + rightSum

    def findMaxmumSubarray(self, A, low, high):
        if high == low:
            return low, high, A[low]
        else:
            mid = (low + high) / 2
            leftLow, leftHigh, leftSum = self.findMaxmumSubarray(A, low, mid)
            rightLow, rightHigh, rightSum = self.findMaxmumSubarray(A, mid + 1,high)
            crossLow, CrossHigh, crossSum = self.FindMaxCrossingSubarray(A, low, mid, high)

            if leftSum >= rightSum and leftSum >= crossSum:
                return leftLow, leftHigh, leftSum
            elif rightSum >= leftSum and rightSum >= crossSum:
                return rightLow, rightHigh, rightSum
            else:
                return crossLow, CrossHigh, crossSum

nums = [-13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
test = MaxSubarray()
res1, res2, res3 = test.findMaxmumSubarray(nums,0,11)
print(res1,res2,res3)