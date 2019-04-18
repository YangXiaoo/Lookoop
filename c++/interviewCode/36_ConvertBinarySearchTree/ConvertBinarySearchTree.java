// 2019-4-18
// 将二叉搜索树转化为排序的双向链表

import java.util.*;

class TreeNode {
	int val;
	TreeNode left, right;
	public TreeNode(int val) { this.val = val; }
}


public class ConvertBinarySearchTree {
	public TreeNode convert(TreeNode root) {
		if (root == null) return root;


		TreeNode preNode = null;
		helper(root, preNode);

		// 获得链表头节点
		TreeNode head = root;	// 链表头结点
		while (head != null && head.left != null) {
			head = head.left;
		}

		return head;
	}

	public void helper(TreeNode root, TreeNode preNode) {
		if (root == null) return;

		// TreeNode preNode = preLastNode;
		TreeNode pCurrent = root;
		if (pCurrent.left != null) {
			helper(pCurrent.left, preNode);
		}

		pCurrent.left = preNode;
		if (preNode != null) {
			preNode.right = pCurrent;
		}

		preNode = pCurrent;

		if (pCurrent.right != null)
			helper(pCurrent.right, preNode);
	}

	public void test(String testName, TreeNode root) {
		List<Integer> listVal = new ArrayList<>();
		TreeNode head = convert(root);

		while (head != null) {
			listVal.add(head.val);
			head = head.right;
		}

		System.out.println(testName + ", linklist: " + listVal.toString());
	}
	public TreeNode tree1() {
		TreeNode root = new TreeNode(10);
		TreeNode a = new TreeNode(6);
		TreeNode b = new TreeNode(14);
		TreeNode c = new TreeNode(4);
		TreeNode d = new TreeNode(8);
		TreeNode e = new TreeNode(12);
		TreeNode f = new TreeNode(16);
		root.left = a;
		root.right = b;
		a.left = c;
		a.right = d;
		b.left = e;
		b.right = f;

		return root;
	}

	public static void main(String[] args) {
		ConvertBinarySearchTree test = new ConvertBinarySearchTree();
		TreeNode root = test.tree1();
		test.test("test1", root);
	}
}