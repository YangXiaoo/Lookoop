/**
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
*/

// 2018-7-23
// 133. Clone Graph
// 读不懂题
// Definition for undirected graph.
class UndirectedGraphNode {
    int label;
    List<UndirectedGraphNode> neighbors;
    UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
};
public class 133_medium_Clone_Graph {
Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
 
public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
    if (node == null)
        return null;
    if (map.containsKey(node))
        return map.get(node);
    UndirectedGraphNode newHead = new UndirectedGraphNode(node.label);
    map.put(node, newHead);
    for (UndirectedGraphNode aNeighbor : node.neighbors)
        newHead.neighbors.add(cloneGraph(aNeighbor));
    return newHead;
}

public class Solution2 {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node==null)
            return null;
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        HashMap<UndirectedGraphNode,UndirectedGraphNode> maps = new HashMap<>();
        Queue<UndirectedGraphNode> queue = new LinkedList<>();

        maps.put(node,newNode);
        queue.offer(node);

        while (!queue.isEmpty()){
            UndirectedGraphNode top = queue.poll();
            List<UndirectedGraphNode> neighbors = top.neighbors;

            for(UndirectedGraphNode neighbour:neighbors){
                if(!maps.containsKey(neighbour)){
                    UndirectedGraphNode newTmpNode = new UndirectedGraphNode(neighbour.label);
                    maps.put(neighbour,newTmpNode);
                    queue.offer(neighbour);
                }
                maps.get(top).neighbors.add(maps.get(neighbour));
            }
        }
        return newNode;
    }
}