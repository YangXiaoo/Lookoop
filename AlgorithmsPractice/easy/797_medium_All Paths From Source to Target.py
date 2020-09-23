"""
Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
 

Constraints:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

# 2020-9-21
class Solution(object):

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(nextNode, tmpRet):
            nonlocal graph, ret, N 
            if nextNode == N - 1:
                ret.append(tmpRet[:])
                return 
            for node in graph[nextNode]:
                tmpRet.append(node)
                helper(node, tmpRet)
                tmpRet.pop()

        ret = []
        N = len(graph)
        for node in graph[0]:
            helper(node, [0, node])

        return ret 


graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
test = Solution()
ret = test.allPathsSourceTarget(graph)
print(ret)
