'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

# 2018-10-19
# 221. maximal-square
# https://leetcode.com/problems/maximal-square/
"""
# https://blog.csdn.net/u012501459/article/details/46553139
如果matrix[i][j]为1，那么A[i][j]=min(A[i-1][j-1],A[i-1][j],A[i][j-1])+1；如果matrix[i][j]为0，那么A[i][j]为0。
    int maximalSquare(vector<vector<char>>& matrix) {
        int height=matrix.size();
        if(height==0)
            return 0;
        int width=matrix[0].size();
        vector<vector<int>>  vec(height,vector<int>(width,0));
        int result=0;
        for(int i=0;i<height;i++)
        {
            for(int j=0;j<width;j++)
            {
                if(matrix[i][j]=='1')
                {
                    vec[i][j]=1;
                    if(i>0&&j>0)
                        vec[i][j]+=min(min(vec[i-1][j],vec[i][j-1]),vec[i-1][j-1]);
                }
                result=max(result,vec[i][j]);
            }
        }
        return result*result;
        
    }

"""

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        max_size = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_size = max(dp[i][j], max_size)

        return max_size**2


# https://leetcode.com/problems/maximal-square/discuss/174700/DP-Python-code-O(n)-space
class Solution2:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        dp = [0] * (len(matrix[0])+1)
        res = prev = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                prev, dp[j+1] = dp[j+1], min(dp[j], dp[j+1], prev)+1 if matrix[i][j] == '1' else 0
                res = max(res, dp[j+1])
        return res * res

m = [['1' ,'0' ,'1' ,'0' ,'0'],
['1' ,'0' ,'1', '1', '1'],
['1', '1' ,'1' ,'1' ,'1'],
['1', '0' ,'0' ,'1', '0']]
test = Solution()
res = test.maximalSquare(m)
print(res)