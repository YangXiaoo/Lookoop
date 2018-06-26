"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

# 2018-6-25
# Edit Distance
# https://blog.csdn.net/chichoxian/article/details/53944188
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        sm = word1
        sn = word2
        m,n = len(sm)+1,len(sn)+1

        # create a matrix (m*n)

        matrix = [[0]*n for i in range(m)]

        matrix[0][0]=0
        for i in range(1,m):
            matrix[i][0] = matrix[i-1][0] + 1

        for j in range(1,n):
            matrix[0][j] = matrix[0][j-1]+1


        for i in range(m):
            print (matrix[i])


        print ("********************")

        cost = 0

        for i in range(1,m):
            for j in range(1,n):
                if sm[i-1]==sn[j-1]:
                    cost = 0
                else:
                    cost = 1

                matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+cost)


        for i in range(m):
            print (matrix[i])

        return matrix[m-1][n-1]


word1 = "intention"
word2 = "execution"
test = Solution()
res = test.minDistance(word1,word2)
print(res)