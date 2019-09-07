import java.util.*;
import java.io.*;

// 2019/9/7
// 递增数
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
        	int t = cin.nextInt();
        	String[] ret = new String[t];
        	for (int i = 0; i < t; ++i) {
        		int curNodeCount = cin.nextInt();
        		// System.out.println("curNode count: " + curNodeCount);
        		int[][] nodes = new int[curNodeCount][3];
        		for (int j = 0; j < curNodeCount; ++j) {
        			nodes[j][0] = cin.nextInt();
        			nodes[j][1] = cin.nextInt();
        			nodes[j][2] = cin.nextInt();
        			// System.out.println("cur input first: " + nodes[j][0]);
        		}
        		String curRet = solver(nodes);
        		ret[i] = curRet;
        	}

        	for (String r : ret) {
        		System.out.println(r);
        	}
        }
	}

	public static void printTreeInOder(TreeNode root) {
		if (root != null) {
			printTreeInOder(root.left);
			System.out.println(root.val + " ");
			printTreeInOder(root.right);
		}
	}

	public static String solver(int[][] nodes) {
		// 创建树
		TreeNode[] nodeList = new TreeNode[nodes.length];
		Arrays.fill(nodeList, null);
		int leafCount = initLeaf(nodeList, nodes);
		constructTree(nodes, nodeList);
		int rootIndex = getRoot(nodes);
		TreeNode root = nodeList[rootIndex];
		// System.out.println(root.val);
		// for (TreeNode node : nodeList) {
		// 	System.out.println("node: " + node.val);
		// }
		String ret = checkTree(root);
		// printTreeInOder(root);
		return ret;
	}

	public static int getRoot(int[][] nodes) {
		int ret = 0;
		int[] index = new int[nodes.length];
		Arrays.fill(index, 0);
		for (int i = 0; i < nodes.length; ++i) {
			if (nodes[i][1] != -1) {
				index[nodes[i][1]] = 1;
			}
			if (nodes[i][2] != -1) {
				index[nodes[i][2]] = 1;
			}
		}

		for (int i = 0; i < nodes.length; ++i) {
			if (index[i] != 0) {
				ret = i;
				break;
			}
		}

		return ret;
	}

	// 先创建叶子节点, 并返回叶子节点个数
	public static int initLeaf(TreeNode[] nodeList, int[][] nodes) {
		int retCount = 0;
		for (int i = 0; i < nodes.length; ++i) {
			if (nodes[i][1] == -1 && nodes[i][2] == -1) {	// 叶子节点
				++retCount;	// 叶子节点个数+1
				nodeList[i] = new TreeNode(nodes[i][0], null, null);
			}
		}

		return retCount;
	}

	// 创建树
	public static TreeNode constructTree(int[][] nodes, TreeNode[] nodeList) {
		boolean flag = false;
		TreeNode ret = null;
		while (!check(nodeList)) {	// 循环直至所有节点都生成
			for (int i = 0; i < nodes.length; ++i) {
				// System.out.println(Arrays.toString(nodeList) + ", i: " + i);
				int leftIndex = nodes[i][1], rightIndex = nodes[i][2];
				TreeNode left = null, right = null;
				if ((leftIndex == -1) && (rightIndex == -1)) {
					continue;
				} 
				if (leftIndex != -1) 
					left = nodeList[leftIndex];
				if (rightIndex != -1) 
					right = nodeList[rightIndex];

				if ((left == null) && (right == null)) continue;

				nodeList[i] = new TreeNode(nodes[i][0], left, right);
				// System.out.println("curnode: , index: " + nodeList[i].val + ", " + i);
				if (check(nodeList)) {
					ret = nodeList[i];
					flag = true;
					break;
				}
			}
			if (flag) break;
		}

		return ret;
	}

	public static boolean check(TreeNode[] nodeList) {
		boolean ret = true;
		for (TreeNode node : nodeList) {
			if (node == null) {
				ret = false;
				break;
			}
		}

		return ret;
	}

	// 判断树是否为递增树
	public static String checkTree(TreeNode root) {
		Deque<TreeNode> deq = new LinkedList<>();
		deq.offerFirst(root);
		String ret = "YES";

		// BFS比较每一层节点和与上一层节点和
		while (!deq.isEmpty()) {
			int curSize = deq.size();
			int preSum = computeSum(deq);
			for (int i = 0; i < curSize; ++i) {
				TreeNode curNode = deq.pollLast();
				if (curNode.left != null) {
					deq.offerFirst(curNode.left);
				}

				if (curNode.right != null) {
					deq.offerFirst(curNode.right);
				}
			}

			int nextSum = computeSum(deq);
			if (nextSum <= preSum) {
				ret = "NO";
				break;
			}
		}

		return ret;
	}

	// 计算队列中节点的和
	public static int computeSum(Deque<TreeNode> deq) {
		int ret = 0;
		for (TreeNode node : deq) {
			ret += node.val;
		}

		return ret;
	}
}
/*
2
8
2 -1 -1
1 5 3
4 -1 6
2 -1 -1
3 0 2
2 4 7
7 -1 -1
2 -1 -1
8
21 6 -1
52 4 -1
80 0 3
31 7 -1
21 -1 -1
59 -1 -1
50 5 -1
48 -1 1
*/