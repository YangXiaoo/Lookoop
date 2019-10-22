'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
# 2018-6-20
# Trapping rain water
# https://www.cnblogs.com/zuoyuan/p/3781453.html
'''
解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为height[i]之前的最高的bar值，然后从后面开始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], rightmax)-height[i]就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # print(height)
        leftmosthigh = [0 for i in range(len(height))]
        # print(leftmosthigh)
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmosthigh[i] = leftmax
        # print(leftmosthigh)
        sum = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(rightmax, leftmosthigh[i]) > height[i]:
                sum += min(rightmax, leftmosthigh[i]) - height[i]
            print(i,rightmax,leftmosthigh[i],height[i],sum)
        return sum
        
# test
h = [0,1,0,2,1,0,1,3,2,1,2,1]
test = Solution()
res = test.trap(h)
print(res)