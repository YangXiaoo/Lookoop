/**
102 Binary Tree level Order Traverse 
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
*/

// 102
// 2018-7-9
// bac_medium_Binary_Tree_level_Order_Traverse 

// Definition for a binary tree node.
// 类似于BFS
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bac_medium_Binary_Tree_level_Order_Traverse {
    public List<List<Integer>> levelOrder(TreeNode root) {
    	// 最终结果
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        // 存放每一层节点
        Queue<TreeNode> treenode = new LinkedList<>();

        if (root == null) {
        	return res;
        } else {
        	List<Integer> tmp = new ArrayList<>();
        	tmp.add(root.val);
        	treenode.offer(root);
        	res.add(tmp);
        }

        while (!treenode.isEmpty()) {
        	// 遍历这一层所有节点
        	int i = treenode.size();
        	List<Integer> tmpRes = new ArrayList<>();

        	while (i > 0) {
        		TreeNode node = treenode.poll();
        		if (node.left != null) {
        			tmpRes.add(node.left.val);
        			treenode.offer(node.left);
        		}
        		if (node.right != null) {
        			tmpRes.add(node.right.val);
        			treenode.offer(node.right);
        		}

        		i--;
        	}

        	if (!tmpRes.isEmpty()) res.add(tmpRes);
        }

        return res;
    }
}