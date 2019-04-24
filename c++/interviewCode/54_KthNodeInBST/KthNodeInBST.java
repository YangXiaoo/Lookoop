// 2019-4-23
// 二叉搜索树的第k大节点


class TreeNode {
	int val;
	TreeNode left, right;
	TreeNode (int val) { 
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

public class KthNodeInBST {
	private int k = 0;

	public int kthNode(TreeNode root, int k) {
		this.k = k;
		TreeNode node = kthNodeHelper(root);
		return node.val;
	}

	public TreeNode kthNodeHelper(TreeNode node) {
		TreeNode ret = null;

		if (node.left != null)
			ret = kthNodeHelper(node.left);

		if (ret == null) {
			if (k == 1)
				ret = node;
			k--;
		}

		if ((ret == null) && (node.right != null)) 
			ret = kthNodeHelper(node.right);

		return ret;
	}

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

	public void test(String testName, int k, int expect) {
		TreeNode root = binaryTree();
		int ret = kthNode(root, k);
		System.out.println(testName + ", expect: " + expect + ", result: " + ret);
	}

	public static void main(String[] args) {
		KthNodeInBST test = new KthNodeInBST();
		test.test("test-1", 3, 4);
		test.test("test-2", 4, 5);
		test.test("test-3", 1, 2);
		test.test("test-4", 5, 6);
		test.test("test-5", 6, 7);
	}
}

// test-1, expect: 4, result: 4
// test-2, expect: 5, result: 5
// test-3, expect: 2, result: 2
// test-4, expect: 6, result: 6
// test-5, expect: 7, result: 7