/*
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
*/

// 2019-5-21
// 230. Kth Smallest Element in a BST [medium]
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class KthSmallestElementInBST {
    private int k = 0;
    public int kthSmallest(TreeNode root, int k) {
        this.k = k;
        TreeNode ret = traverse(root);
        
        return ret.val;
    }
    
    public TreeNode traverse(TreeNode root) {
        TreeNode expect = null;
        if (root.left != null) {
            expect = traverse(root.left);
        }
        
        if (expect == null) {
            if (k == 1) {
                expect = root;
            }
            
            --k;
        }
        if ((expect == null) && (root.right != null)) {
            expect = traverse(root.right);
        }
        
        return expect;
    }
}