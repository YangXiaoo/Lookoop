'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

# 2018-9-21
# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/


"""
参考博客: https://blog.csdn.net/smile_watermelon/article/details/47445981


维护两个数组，local[][]和global[][]，其中
global[i][j]表示到第i天时完成j次交易的最大收益，
local[i][j]表示到第i天时完成j次交易并且最后一次交易发生在第i天时的最大收益。

global的推导公式如下：

global[i][j] = max(local[i][j], global[i-1][j]); # 最后一日不做交易或最后一日完成第j次交易
即，到第i天完成j次交易的最大收益，要么是第j次交易发生在第i天时的最大收益，要么是到第i-1天完成j次交易时的最大收益。

local的推导公式如下：

local[i][j] = max(global[i-1][j-1]+max(diff,0), local[i-1][j]+diff); # 倒数第二次完成第j次交易，或倒数第二日不做任何交易
需要看两个量，第一个是全局global到i-1天进行j-1次交易，然后加上今天的交易，如果今天是赚钱的话（也就是前面只要j-1次交易，最后一次交易取当前天）；第二个量则是取local第i-1天j次交易，然后加上今天的差值（这里因为local[i-1][j]比如包含第i-1天卖出的交易，所以现在变成第i天卖出，并不会增加交易次数，而且这里无论diff是不是大于0都一定要加上，因为否则就不满足local[i][j]必须在最后一天卖出的条件了）。
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        lens = len(prices)
        if lens < 2 or k < 1: return 0
        if k >= (lens // 2):
            res = 0
            for i in range(lens-1):
                if prices[i + 1] > prices[i]:
                    res += prices[i + 1] - prices[i]
        k += 1
        glob = [[0 for _ in range(k)] for _ in range(lens)]
        local = [[0 for _ in range(k)] for _ in range(lens)]

        for i in range(1, lens, 1):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k, 1):
                print(i, j)
                local[i][j] = max(glob[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
                glob[i][j] = max(local[i][j], glob[i - 1][j])

        return glob[-1][-1]


prices = [3,2,6,5,0,3]
k = 2
test = Solution()
res = test.maxProfit(k, prices)
print(res)