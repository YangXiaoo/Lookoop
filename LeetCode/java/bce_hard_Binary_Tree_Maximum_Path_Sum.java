/**
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
*/

// 2018-7-18
// 124. Binary Tree Maximum Path Sum
//Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bce_hard_Binary_Tree_Maximum_Path_Sum {
  int max = 0;
    public int maxPathSum(TreeNode root) {
        if (root != null) max = root.val;

        dfs(root);

        return max;
    }

    public int dfs(TreeNode root) {
      if (root == null) return 0;

      int left = dfs(root.left);
      int right = dfs(root.right);

      // ??
      if (left < 0) left = 0;
      if (roght < 0) right = 0;

      int sum = root.val + left + right;
      max = Math.max(max, sum);

      return root.val + Math.max(left, right);
    }
}
