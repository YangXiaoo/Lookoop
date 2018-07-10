/**
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
*/

// 105
// 2018-7-10
// 思路：先序遍历第一位为根节点，根据根节点在中序遍历的位置找到左子树和右子树，利用递归生成二叉树
// https://www.cnblogs.com/springfor/p/3884034.html
// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class baf_medium_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int preLength = preorder.length;
        int inLength = inorder.length;
        return buildTree(preorder, 0, preLength-1, inorder, 0, inLength-1);
     }
     public TreeNode buildTree(int[] pre, int preStart, int preEnd, int[] in, int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) {
            return null;
        }

        int rootVal = pre[preStart];
        int rootIndex = 0;
        for (int i = preStart; i <= inEnd; i++) {
            if (in[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }

        int lens = rootIndex - inStart;
        TreeNode root = new TreeNode(rootVal);
        root.left = build(pre, preStart+1, preStart+lens, in, inStart, rootIndex-1);
        root.right = build(pre, preStart+1+lens, preEnd, in, rootIndex+1,inEnd);

        return root;
     }
}