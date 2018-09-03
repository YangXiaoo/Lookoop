'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2
'''

# 2018-9-3
# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution1:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = 1
        while index1 < index2:
            if numbers[index2] + numbers[index1] == target:
                break
            else:
                if numbers[index2] + numbers[index1] < target:
                    index1 += 1
                    index2 += 1
                else:
                    index1 -= 1
        return [index1 + 1, index2 + 1] 

class Solution2:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff not in dic:
                dic[numbers[i]] = i
            else:
                return [dic[diff] + 1, i + 1]

        return []

numbers = [1,2,3,4,7,11,15]
target = 9
test = Solution1()
r = test.twoSum(numbers, target)
print(r)