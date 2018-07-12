/**
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
no require to sort the tree
*/

// 2018-7-12
// 114. Flatten Binary Tree to Linked List

// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
// 遍历根节点左子树的右子树到空节点r1，将根节点接到r1上，然后将根节点的左子树接到根节点的右子树上,根节点左子树为null。递归完成,迭代终止条件为root.null == null，
class bbe_easy_Flatten_Binary_Tree_to_Linked_List {
    public void flatten(TreeNode root) {
        if (root == null) return;
        if (root.left != null) {
            TreeNode cur = root.left;
            while (cur.right != null) {
                cur = cur.right;
            }

            cur.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        flatten(root.right);
    }
}