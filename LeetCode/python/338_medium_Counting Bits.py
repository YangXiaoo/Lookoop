'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

# 2018-11-19
# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/


# https://www.cnblogs.com/liujinhong/p/6115831.html
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * num
        for i in range(num):
            if i % 2 == 1:
                # 奇数时增加1
                res[i] = res[i>>1] + 1
            else:
                # 偶数时1的个数等于上一个奇数的1的个数
                res[i] = res[i>>1]
        return res

num = 5
test = Solution()
res = test.countBits(num)
print(res)