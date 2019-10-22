'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

# 2018-11-10
# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number


# https://leetcode.com/problems/find-the-duplicate-number/discuss/72912/Python-solution-with-detailed-explanation
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0

        # 找到循环起点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 找到重复元素
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


nums = [3,1,3,4,2]
test = Solution()
res = test.findDuplicate(nums)
print(res)