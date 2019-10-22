'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more(https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs) about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

# 2018-9-2
# 207. Course Schedule
# topological sort

# https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        vetex = [[] for _ in range(numCourses)]  # adjacency lists
        indegree = [0 for _ in range(numCourses)] # indegree of each node
        queue = [] # store node in which indgree is zero

        for i in range(len(prerequisites)):
            vetex[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] += 1
        # print(vetex, degree)
        count = 0

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            count += 1
            cur = queue.pop()
            # print(queue, cur)
            for i in vetex[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if count == numCourses:
            return True 
        else:
            return False



test = Solution()
numCourses = 2
prerequisites = [[0,1]]
res = test.canFinish(numCourses, prerequisites)
print(res)