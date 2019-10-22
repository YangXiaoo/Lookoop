/* 
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.`
*/

// 2018-8-27
// 310. Minimum Height Trees
#include <stdio.h>
class Solution {
public:
	struct Node
	{
		unordered_set<int> neighbor;
		bool isleaf()const{return neighbor.size() == 1;}
	};
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        std::vector<int> buffer1;
        std::vector<int> buffer2;
        std::vector<int>* pb1 = &buffer1;
        std::vector<int>* pb2 = &buffer2;

        if (n == 1)
        {
        	buffer1.push_back(0);
        	return buffer1;
        }

        if (n == 2)
        {
        	buffer1.push_back(0);
        	buffer1.push_back(1);
        	return buffer1;
        }

        // 构造图
        vector<Node> nodes(n);
        for (auto p : edges)
        {
        	nodes[p.first].neighbor.insert(p.second);
        	nodes[p.second].neighbor.insert(p.first);
        }

        // 找到叶子,将叶子装入pb1所指向的数组buffer1中
        for (int i = 0; i < n; ++i)
        {
        	if (nodes[i].isleaf())
        		pb1->push_back(i);
        }

        // 去除叶子
        while (true)
        {
        	for (int i : *pb1)
        	{
        		for (auto n : nodes[i].neighbor)
        		{
        			nodes[n].neighbor.erase(i);
        			if (nodes[n].isleaf())
        				pb2->push_back(n);
        		}
        	}

        	if (pb2->empty())
        	{
        		return *pb1;
        	}

        	pb1->clear();
        	swap(pb1, pb2);
        }
    }
};

/*The basic idea is "keep deleting leaves layer-by-layer, until reach the root."

Specifically, first find all the leaves, then remove them. After removing, some nodes will become new leaves. So we can continue remove them. Eventually, there is only 1 or 2 nodes left. If there is only one node left, it is the root. If there are 2 nodes, either of them could be a possible root.

Time Complexity: Since each node will be removed at most once, the complexity is O(n).

Thanks for pointing out any mistakes.

Updates:
More precisely, if the number of nodes is V, and the number of edges is E. The space complexity is O(V+2E), for storing the whole tree. The time complexity is O(E), because we gradually remove all the neighboring information. As some friends pointing out, for a tree, if V=n, then E=n-1. Thus both time complexity and space complexity become O(n).*/