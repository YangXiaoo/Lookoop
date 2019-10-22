/**
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/

// 2018-7-18
// 121. Best Time to Buy and Sell Stock

class bcb_easy_Best_Time_to_Buy_and_Sell_Stock {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) return 0;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                int profit = prices[j] - prices[i];
                if (profit > maxProfit) maxProfit = profit;
            }
        }

        return maxProfit;
    }
}
// Solution2
class Solution {
    public int maxProfit(int[] prices) {
         if(prices==null||prices.length==0){
            return 0;
        }
        
         int min = prices[0];
        int result = 0;
        
       for(int i=0;i<prices.length;i++) {
           if(prices[i] < min ){
             min =prices[i];
           }else if(prices[i] - min > result){
             result = prices[i] - min ;
           }
      }
        return result;
    }
  }