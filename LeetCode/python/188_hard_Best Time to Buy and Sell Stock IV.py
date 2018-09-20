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

# 2018-9-20
# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """



    # public int maxProfit(int k, int[] prices) {
    #     int len = prices.length;
    #     if (k >= len / 2) return quickSolve(prices);
        
    #     int[][] t = new int[k + 1][len];
    #     for (int i = 1; i <= k; i++) {
    #         int tmpMax =  -prices[0];
    #         for (int j = 1; j < len; j++) {
    #             t[i][j] = Math.max(t[i][j - 1], prices[j] + tmpMax);
    #             tmpMax =  Math.max(tmpMax, t[i - 1][j - 1] - prices[j]);
    #         }
    #     }
    #     return t[k][len - 1];
    # }
    

    # private int quickSolve(int[] prices) {
    #     int len = prices.length, profit = 0;
    #     for (int i = 1; i < len; i++)
    #         // as long as there is a price gap, we gain a profit.
    #         if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
    #     return profit;
    # }
        