/*
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
*/

// 2019-4-28
// 617. Merge Two Binary Trees [easy]
// https://leetcode.com/problems/merge-two-binary-trees/
import java.util.*;

public class MergeTwoBinaryTrees {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        TreeNode ret =  helper(t1, t2);
        return ret;
    }

    public TreeNode helper(TreeNode t1, TreeNode t2) {
        if ((t1 != null) && (t2 != null)) {
        	TreeNode node = new TreeNode(t1.val + t2.val);
        	node.left = helper(t1.left, t2.left);
        	node.right = helper(t1.right, t2.right);
            return node;
        }else if ((t1 == null) && (t2 != null)) {
        	TreeNode node = new TreeNode(t2.val);
        	node.left = helper(t1, t2.left);
        	node.right = helper(t1, t2.right);
            return node;
        }else if ((t1 != null) && (t2 == null)) {
        	TreeNode node = new TreeNode(t1.val);
        	node.left = helper(t1.left, t2);
        	node.right = helper(t1.right, t2);
            return node;
        } else {
        	return null;
        }
    }

	public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
		if (t1 == null) {
			return t2;
		} else if (t2 == null) {
			return t1;
		} else {
			TreeNode root = new TreeNode(t1.val + t2.val);
			root.left = mergeTrees(t1.left, t2.left);
			root.right = mergeTrees(t1.right, t2.right);
			return root;
		}
	}
}