/**
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
*/

// 2018-7-10
// 107. Binary Tree Level Order Traversal II

// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bah_easy_Binary_Tree_Level_Order_Traversal_II {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        // Queue<TreeNode> treenode = new LinkedList<>();  // FIFO
        Deque<TreeNode> treenode = new LinkedList<>();

        if (root == null) {
            return res;
        } else {
            List<Integer> tmpRes = new ArrayList<Integer>();
            tmpRes.add(root.val);
            treenode.offerFirst(root);
            res.add(0, tmpRes);
        }

        while (!treenode.isEmpty()) {
            int i = treenode.size();
            List<Integer> tmpRes = new ArrayList<Integer>();

            while (i >0) {
                TreeNode node = treenode.pollLast();
                if (node.left != null) {
                    tmpRes.add(node.left.val);
                    treenode.offerFirst(node.left);
                }
                if (node.right != null) {
                    tmpRes.add(node.right.val);
                    treenode.offerFirst(node.right);
                }

                i--;
            }

            if (!tmpRes.isEmpty()) res.add(0, tmpRes);
        }
        return res;
    }
}