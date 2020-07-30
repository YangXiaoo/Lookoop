# coding:utf-8

"""
354. Russian Doll Envelopes
Hard

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

# 2020-7-30
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0: return 0
        sortedEnvelopes = sorted(envelopes)
        # print(sortedEnvelopes)
        dp = [0 for _ in range(len(envelopes))]
        
        for i in range(0, len(envelopes)):
            dp[i] = 1
            for j in range(i):
                # print(i,j)
                if sortedEnvelopes[j][0] < sortedEnvelopes[i][0] and sortedEnvelopes[j][1] < sortedEnvelopes[i][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    # print("dp: {}".format(dp))
        # print(dp)
        return max(dp)

envelopesNums = [
	[[5,4],[6,4],[6,7],[2,3]],
]

answers = [
	3,
]

test = Solution()
for (en, ans) in zip(envelopesNums, answers):
	ret = test.maxEnvelopes(en)
	print("{}, my answer is {}, true answer is {}".format(en, ret, ans))