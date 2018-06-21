'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
nums1 = [1, 3]
nums2 = [2]
median: 2

nums1 = [1, 2]
nums2 = [3, 4]

median (2 + 3)/2 = 2.5
'''

# 2018-6-15
# Median of Two Sorted Arrays

# 归并排序
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        result = []

        if l1 == 0:
            if l2%2 != 0:
                return nums2[l2//2]
            return (nums2[l2//2 - 1] + nums2[l2//2])/2.0

        if l2 == 0:
            if l1%2 != 0:
                return nums1[l1//2]
            return (nums1[l1//2 - 1] + nums1[l1//2])/2.0

        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] <= nums2[0]:
                result.append( nums1.pop(0) )
            else:
                result.append( nums2.pop(0) )

        result += nums1
        result += nums2
        print (result)
        tl = len(result)
        if tl%2 != 0:
            return result[tl//2]
        else:
            return (result[(tl//2) - 1] + result[(tl//2)])/2.0


# test
n1 = [1,2]
n2 = [3,4]
test = Solution()
median = test.findMedianSortedArrays(n1,n2)
print(median)