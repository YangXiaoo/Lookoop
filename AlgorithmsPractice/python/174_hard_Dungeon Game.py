'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3  3
-5  -10 1
10  30  -5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.'''

# 2018-9-12
# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/description/


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        col = len(dungeon[0])
        row = len(dungeon)

        dp = [[0 for _ in range(col)] for _ in range(row)]
        print(dp) 

        dp[-1][-1] = 1 # knight is alive
        for i in range(row - 2, -1, -1):
            dp[i][col - 1] = max(1,dp[i + 1][col - 1] - dungeon[i + 1][col -1])
        for j in range(col - 2, -1, -1):
            dp[row - 1][j] = max(1, dp[row - 1][j + 1] - dungeon[row - 1][j + 1])

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = min(max(1, dp[i][j + 1] - dungeon[i][j + 1]), max(1, dp[i + 1][j] - dungeon[i + 1][j]))

        return max(1, dp[0][0] - dungeon[0][0])

test = Solution()
r = test.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
print(r)
        