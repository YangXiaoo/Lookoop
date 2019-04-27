/*
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
*/

// 2019-4-27
// 538. Convert BST to Greater Tree [easy]
// https://leetcode.com/problems/convert-bst-to-greater-tree/

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


public class ConvertBSTToGreaterTree {
	private int pre = 0;
    public TreeNode convertBST(TreeNode root) {
    	pre = 0;
        helper(root);

        return root;
    }

    public void helper(TreeNode node) {
    	if (node == null) return;
    	helper(node.right);
    	node.val += pre;
    	pre = node.val;
    	helper(node.left);
    }

    // 基于迭代
    public TreeNode convertBST2(TreeNode root) {
    	int preVal = 0;
    	Stack<TreeNode> stack = new Stack<>();
    	TreeNode cur = root;
    	while ((cur != null) || (!stack.isEmpty())) {
    		while (cur != null) {
    			stack.push(cur);
    			cur = cur.right;
    		}

    		cur = stack.pop();
    		cur.val += preVal;
    		preVal = cur.val;
    		cur = cur.left;
    	}

    	return root;
    }

    // 剑指offer-54题
	public TreeNode binaryTree() {
		TreeNode root = new TreeNode(5);
		TreeNode b = new TreeNode(3);
		TreeNode c = new TreeNode(7);
		TreeNode d = new TreeNode(2);
		TreeNode e = new TreeNode(4);
		TreeNode f = new TreeNode(6);
		TreeNode g = new TreeNode(8);
		root.left = b;
		root.right = c;
		b.left = d;
		b.right = e;
		c.left = f;
		c.right = g;

		return root;
	}

	public void traverse(TreeNode root, List<Integer> ret) {
		if (root != null) {
			traverse(root.left, ret);
			ret.add(root.val);
			traverse(root.right, ret);
		}
	}
	public void test(String testName, TreeNode root) {
		TreeNode ret = convertBST2(root);
		List<Integer> tmp = new ArrayList<>();
		traverse(ret, tmp);
		System.out.println(testName + ", result: " + tmp.toString());
	}

	public static void main(String[] args) {
		ConvertBSTToGreaterTree test = new ConvertBSTToGreaterTree();
		TreeNode root1 = test.binaryTree();
		test.test("test-1", root1);
	}
}

// test-1, result: [35, 33, 30, 26, 21, 15, 8]