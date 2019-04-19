// 2019-4-18
// 序列化二叉树

import java.util.*;

// 定义树节点
class TreeNode {
	int val;
	TreeNode left, right;
	public TreeNode(int val) { this.val = val; }
	public TreeNode() {}
}

public class SerializeBinaryTree {
	private int count;
	public List<String> serialize(TreeNode root) {
		List<String> serialList = new ArrayList<>();

		serializeHelper(root, serialList);

		return serialList;
	}
	public void serializeHelper(TreeNode root, List<String> serialList) {
			if (root == null) {
				serialList.add("null");
				return;
			}

			String val = String.valueOf(root.val);
			serialList.add(val);

			serializeHelper(root.left, serialList);
			serializeHelper(root.right, serialList);
	}

	public TreeNode deSerialize(List<String> serialList) {

		TreeNode root = new TreeNode();
		count = 0;
		deSerializeHelper(root, serialList);
		return root;
	}

	public void deSerializeHelper(TreeNode root, List<String> serialList) {
		if (serialList.size() == count) {
			return;
		}
		String val = serialList.get(count);
		count++;
		if (val == "null") {
			root = null;
			return;
		} else {
			root.val = Integer.parseInt(val);
		}
		root.left = new TreeNode();
		root.right = new TreeNode();
		deSerializeHelper(root.left, serialList);
		deSerializeHelper(root.right, serialList);
	}

	public void test(String testName, List<String> serialList) {
		TreeNode root = deSerialize(serialList);
		List<String> list = serialize(root);
		System.out.println(testName + "inputs: " + serialList.toString() + ", deSerialize result: " + list.toString());
	}

	public static void main(String[] args) {
		SerializeBinaryTree test = new SerializeBinaryTree();
		String[] list = {"1", "2", "null", "null", "null", "3", "5", "null", "null", "6", "null", "null"};
		List<String> serialList1 = Arrays.asList(list);

		test.test("test1", serialList1);
	}
}