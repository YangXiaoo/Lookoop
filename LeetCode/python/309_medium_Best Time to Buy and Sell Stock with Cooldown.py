'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

# 2018-11-14
# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


# 状态机：https://www.cnblogs.com/jdneo/p/5228004.html
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75940/5-lines-Python-O(n)-time-O(1)-space
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free = 0
        have = cool = float('-inf')
        for p in prices:
            print(free, have, cool)
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)


        # free is the maximum profit I can have while being free to buy.
        # have is the maximum profit I can have while having stock.
        # cool is the maximum profit I can have while cooling down.

"""        Let me just expand what StefanPochmann explained a little bit:
            free -- is the maximum profit I can have while being free to buy. I am free to buy in the current iteration either because I was free to buy in the previous iteration and did nothing in the current iteration, or I was cooling down in the previous iteration and did nothing in the current iteration.
            have -- is the maximum profit I can have while having stock, i.e., I've bought a stock and haven't sold it yet. This happens when I was already holding stock but did not sell in this iteration, or I was free to buy stock last iteration and bought the stock in the current iteration.
            cool -- is the maximum profit I can have while cooling down. This only happens if I was holding a stock in the previous iteration and sold it in the current iteration."""


prices = [1,2,3,0,2]
test = Solution()
res = test.maxProfit(prices)
print(res)


