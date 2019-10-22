/**
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
*/


// 104
// 2018-7-9
// bae_easy_Maximum_Depth_of_Binary_Tree

// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bae_easy_Maximum_Depth_of_Binary_Tree {
    public int maxDepth(TreeNode root) {
        // 存储每一层的节点
        Queue<TreeNode> treenode = new LinkedList<>();
        int depth = 0;
        if (root == null) {
            return 0;
        } else {
            treenode.offer(root);
        }

        while (!treenode.isEmpty()) {
            depth++;
            int i = treenode.size();

            while (i > 0) {
                TreeNode node = treenode.poll();
                if (node.left != null) {
                    treenode.offer(node.left);
                }

                if (node.right != null) {
                    treenode.offer(node.right);
                }

                i--;
            }

        }

        return depth;
    }
}

class Solution2 {
    public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        return Math.max(maxDepth(root.left),maxDepth(root.right))+1;
        
    }
}