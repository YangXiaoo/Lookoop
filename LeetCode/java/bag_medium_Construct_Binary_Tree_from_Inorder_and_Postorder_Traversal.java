/**

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
*/

// 106
// 2018-7-10
// Construct Binary Tree from Inorder and Postorder Traversal
// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bag_medium_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int inLens = inorder.length;
        int posLens = postorder.length;

        return buildTree(inorder, 0, inLens-1, postorder, 0, posLens-1); 
    }

    public TreeNode buildTree(int[] in, int inStart, int inEnd, int[] pos, int poStart, int poEnd) {
        if (inStart > inEnd || poStart > poEnd) {
            return null;
        }

        int rootValue = pos[poEnd];
        int rootIndex = 0;
        for (int i = 0; i <= inEnd; i++) {
            if (in[i] == rootValue) {
                rootIndex = i;
                break;
            }
        }

        int lens = rootIndex - inStart;
        TreeNode root = new TreeNode(rootValue);
        root.left = buildTree(in, inStart, rootIndex-1, pos, poStart, poStart+lens-1); // poStart+lens-1
        root.right = buildTree(in, rootIndex+1, inEnd, pos, poStart+lens, poEnd-1);

        return root;
    }
}