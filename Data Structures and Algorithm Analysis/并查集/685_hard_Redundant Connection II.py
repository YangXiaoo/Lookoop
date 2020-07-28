# coding:utf-8
"""
685. Redundant Connection II
Hard

769

210

Add to List

Share
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        canA = [-1, -1]
        canB = [-1, -1]
        fa = [0 for i in range(len(edges)+1)]

        for edge in edges:
        	if fa[edge[1]] == 0:
        		fa[edge[1]] = edge[0]
        	else:
        		canA[0] = fa[edge[1]]
        		canA[1] = edge[1]
        		canB[0] = fa[edge[0]]
        		canB[1] = edge[1]

        		edge[1] = 0

        # print(canA, canB)
        fa = [i for i in range(len(edges)+1)]

        for edge in edges:
        	if edge[1] == 0: continue

        	child, father = edge[1], edge[0]
        	if self.find(fa, father) == child:
        		if canA[0] == -1: return edge
        		return canA

        	fa[child] = father

        return canB
        

    def find(self, fa, x):
    	while x != fa[x]:
    		fa[x] = fa[fa[x]]
    		x = fa[x]
    	return x

edgesCollections =  [
		[[1,2], [2,3], [3,4], [4,1], [1,5]],
		[[1,2], [1,3], [2,3]]
	]

test = Solution()

for edges in edgesCollections:
	ret = test.findRedundantDirectedConnection(edges)
	print(ret)