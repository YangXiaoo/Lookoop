'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

# 2018-10-11
# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Time Limit Exceeded - 30 / 32 test cases passed.
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_len = len(nums) - 1
        if nums_len == 0:
            return nums[0]
        i = 0 
        while i < nums_len:
            j = 0
            while j < nums_len - i:
                if nums[j + 1] < nums[j]:
                    tmp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = tmp
                j += 1
            if i == k - 1:
                break
            i += 1
        return nums[-k]


class Solution2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        min_number = min(nums)
        for i in range(k-1):
            max_number = max(nums)
            nums[nums.index(max_number)] = min_number

        return max(nums)
            

class Solution3:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 使用最小二叉堆


nums = [3,4]
k = 2
test = Solution2()
res = test.findKthLargest(nums, k)
print(res)