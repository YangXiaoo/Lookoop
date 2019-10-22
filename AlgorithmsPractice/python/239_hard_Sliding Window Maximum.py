'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''

# 2018-11-4
# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not k: return []
        queue, res = collections.deque(), []
        for i, v in enumerate(nums):
            # print(queue)
            # 档queue不为空且最后一位索引在nums中的值比当前遍历值小则去掉最后一位
            while queue and nums[queue[-1]] <= v:
                queue.pop()
            queue.append(i)

            # 窗口移出queue记录的位置
            if queue[0] == i - k:
                queue.popleft()

            res.append(nums[queue[0]])
        return res[k - 1:]

nums = [1,3,-1,-3,5,3,6,7]
k = 3
test = Solution()
res = test.maxSlidingWindow(nums, k)
print(res)