# coding:utf-8

"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 

Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""

# 2020-8-19
# graph
class Solution(object):
    def __init__(self):
        self.fa = []

    def initFa(self, n):
        self.fa = [i for i in range(n+1)]

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        lenM = len(M)
        self.initFa(lenM)

        row, colEnd, colStart = lenM, lenM, 0
        circleRecord = 0
        for r in range(row):
            for c in range(colStart, colEnd):
                if M[r][c] == 1:
                    people_1, people_2 = r + 1, c + 1
                    self.fa[self.find(people_1)] = self.find(people_2)
            colStart += 1

        for x in range(1, lenM+1):
            if x != self.fa[x]:
                circleRecord += 1
            
        # print(circleRecord)
        return lenM - circleRecord

    def find(self, x):
        if x == self.fa[x]:
            return x
        else:
            return self.find(self.fa[x])

    def merge(self, x, y):
        pass

nums = [[1,1,0],
        [1,1,0],
        [0,0,1]]

test = Solution()
ret = test.findCircleNum(nums)
print(ret)