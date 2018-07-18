/**
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/

// 2018-7-18
// 122. Best Time to Buy and Sell Stock III
/**
根据题目要求，最多进行两次买卖股票，而且手中不能有2只股票，就是不能连续两次买入操作。

所以，两次交易必须是分布在2各区间内，也就是动作为：买入卖出，买入卖出。

进而，我们可以划分为2个区间[0,i]和[i,len-1]，i可以取0~len-1。

那么两次买卖的最大利润为：在两个区间的最大利益和的最大利润。

一次划分的最大利益为：Profit[i] = MaxProfit(区间[0,i]) + MaxProfit(区间[i,len-1]);

最终的最大利润为：MaxProfit(Profit[0], Profit[1], Profit[2], ... , Profit[len-1])。
*/
class bcd_hard_Best_Time_to_Buy_and_Sell_Stock_III {
  public int maxProfit(int[] prices) {  
        if(prices == null || prices.length <= 1){  
            return 0;  
        }  
        int len = prices.length;  
        int maxProfit = 0;  
        int min = prices[0];  
        int[] arrayA = new int[len];  
        
        for(int i=1;i<prices.length;i++){
            min=Math.min(min,prices[i]); // if (min > prices[i]) min = prices[i];
            arrayA[i]=Math.max(arrayA[i-1],prices[i]-min);
        }
        
        int max = prices[len-1];  
        int arrayB[] = new int[len];  
        for(int i = len-2; i >= 0; i--){
            max = Math.max(prices[i],max);
            arrayB[i] = Math.max(max-prices[i],arrayB[i+1]);
        }  
        
        for(int i = 0; i < len; i++){  
            maxProfit = Math.max(maxProfit,arrayA[i] + arrayB[i]);
        }  
        
        return maxProfit;  
    }
}
