/**

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
*/

// 2018-7-10
// 108. Convert Sorted Array to Binary Search Tree

// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bai_easy_Convert_Sorted_Array_to_Binary_Search_Tree {
    public TreeNode sortedArrayToBST(int[] nums) {
        return buildTree(nums, 0, nums.length);
    }

    public TreeNode buildTree(int[] nums, int low, int hight) {
        // 使用递归添加节点
        if (low > hight) {
            return null;
        }

        int mid = (low + hight) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = buildTree(nums, low, mid-1);
        root.right = buildTree(nums, mid+1, hight);

        return root;
    }
}