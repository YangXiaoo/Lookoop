'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

# 2018-11-18
# 322. Coin Change
# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # # not greedy algorithms
        # coins.sort()
        # index, res = len(coins) - 1, 0
        # while index >= 0:
        #     cur = coins[index]
        #     if cur <= amount:
        #         tmp_number = amount // cur
        #         res += tmp_number
        #         amount = amount % cur
        #     index -= 1
        # print(amount)
        # if amount != 0:
        #     return -1
        # return res

        # use dp
        # don not understand
        # ...


        # use bfs
        # if amount == 0:
        #     return 0
        # value1 = [0]
        # value2 = []
        # nc =  0
        # visited = [False]*(amount+1)
        # visited[0] = True
        # while value1:
        #     nc += 1
        #     for v in value1:
        #         for coin in coins:
        #             newval = v + coin
        #             if newval == amount:
        #                 return nc
        #             elif newval > amount:
        #                 continue
        #             elif not visited[newval]:
        #                 visited[newval] = True
        #                 value2.append(newval)
        #     value1, value2 = value2, []
        # return -1



        if amount == 0: return 0
        queue = [0]
        count = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while len(queue) != 0:
            tmp = []
            count += 1
            for v in queue:
                for c in coins:
                    new_val = c + v 
                    if new_val == amount:
                        return count
                    elif new_val > amount:
                        continue
                    elif not visited[new_val]:
                        visited[new_val] = True
                        tmp.append(new_val)
            queue = tmp 
        return -1






coins = [186,419,83,408]

amount = 6249    
test = Solution()
res = test.coinChange(coins, amount)
print(res)