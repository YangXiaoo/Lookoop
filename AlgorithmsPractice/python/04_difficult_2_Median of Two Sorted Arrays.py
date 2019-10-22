# 2018-6-15
# 递归二分查找
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
            return (nums2[l2//2 - 1] + nums2[l2//2])/2

        if l2 == 0:
            if l1%2 != 0:
                return nums1[l1/2]
            return (nums1[l1//2 - 1] + nums1[l1//2])/2

        return self.binarySearch(nums1,0,len(nums1),nums2,0,len(nums2))

    def binarySearch(self,nums1,lower1,upper1,nums2,lower2,upper2):
    	pass
    	# 暂未解决
