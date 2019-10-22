/*
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
*/

// 2019-4-28
// 543. Diameter of Binary Tree [easy]
// https://leetcode.com/problems/diameter-of-binary-tree/
import java.util.*;

class TreeNode {
	int val;
	TreeNode left, right;
	TreeNode (int val) { 
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

public class DiameterOfBinaryTree {
	private int ret = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        // 左最长加右最长
        ret = 0;
        helper(root);

        return ret;
    }

    public void helper(TreeNode node) {
    	if (node != null) {
    		int maxleft = maxLength(node.left);
    		int maxRight = maxLength(node.right);
            ret = Math.max(ret, maxleft + maxRight)
    		helper(node.left);
    		helper(node.right);
    	}
    }

    public int maxLength(TreeNode node) {
    	if (node == null) {
    		return 0;
    	}

    	return Math.max(maxLength(node.left), maxLength(node.right)) + 1;
    }

    public void test(String testName, TreeNode root, int expect) {
    	int ret = diameterOfBinaryTree(root);
    	System.out.println(testName + ", expect: " + expect + ", result: " + ret);
    }

    public TreeNode tree1() {
    	TreeNode a = new TreeNode(1);
    	TreeNode b = new TreeNode(2);
    	TreeNode c = new TreeNode(3);
    	TreeNode d = new TreeNode(4);
    	TreeNode e = new TreeNode(5);
    	a.left = b;
    	a.right = c;
    	b.left = d;
    	b.right = e;

    	return a;
    }

    public static void main(String[] args) {
    	DiameterOfBinaryTree test = new DiameterOfBinaryTree();
    	TreeNode root1 = test.tree1();
    	test.test("test-1", root1, 3);
    }
}