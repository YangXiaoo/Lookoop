# coding:utf-8
import math
feature = 8.866080156402736
print(10 * math.sin(5 * feature) + 7 * math.cos(4 * feature))

nums1 = [1,2,3,4]
nums2 = [5,6,7,8]
nums1[2:], nums2[2:] = nums2[2:], nums1[2:]
print(nums1, nums2)