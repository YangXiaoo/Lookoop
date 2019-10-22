/*
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
*/

// 2019-4-26
// 437. Path Sum III(113, 114)
// https://leetcode.com/problems/path-sum-iii/

import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class TreeNode {
	int val;
	TreeNode left, right;
	public TreeNode(int val) { this.val = val; }
	public TreeNode() {}
}

class Tree {
	private int count;
	public TreeNode deSerialize(List<String> serialList) {
		TreeNode root = null;
		count = 0;
		root = deSerializeHelper(root, serialList);
		return root;
	}

	public TreeNode deSerializeHelper(TreeNode node, List<String> serialList) {
		if (serialList.size() == count) {
			return null;
		}
		String val = serialList.get(count);
		count++;
		if (val == "null") {
			return null;
		} 
		node = new TreeNode(Integer.parseInt(val));
		node.left = deSerializeHelper(node, serialList);
		node.right = deSerializeHelper(node, serialList);

		return node;
	}
}

class PathSum {
	private List<List<Integer>> path = new ArrayList<List<Integer>>();
	private int sum = 0;

    public int pathSum(TreeNode root, int sum) {
    	path = new ArrayList<List<Integer>>();
    	this.sum = sum;
        pathSumHelper(root);
        // System.out.println(path.toString());
        return path.size();
    }

    public void pathSumHelper(TreeNode node) {
    	if (node != null) {
    		List<Integer> tmp = new ArrayList<>();
    		dfs(node, tmp);
			pathSumHelper(node.left);
			pathSumHelper(node.right);
    	}
    }

    public void dfs(TreeNode node, List<Integer> tmp) {
    	if (node != null) {
    		tmp.add(node.val);
    		if (nodeSum(tmp) == sum) {
    			path.add(new ArrayList(tmp));
    		}

			dfs(node.left, tmp);
			dfs(node.right, tmp);	

    		if (tmp.size() > 1)
    			tmp.remove(tmp.size() - 1);
    	}
    }

    private int nodeSum(List<Integer> nodeList) {
    	int curSum = 0;
    	for (Integer node : nodeList) {
    		curSum += node;
    	}

    	return curSum;
    }

    public void test(String testName, TreeNode root, 
    			     int sum, int expect) {

    	int ret = pathSum(root, sum);

    	System.out.println(testName + ", ret: " + ret + ", expect: " + expect);
    }

    public TreeNode tree2() {
    	TreeNode a = new TreeNode(1);
    	TreeNode b = new TreeNode(-2);
    	TreeNode c = new TreeNode(-3);
    	TreeNode d = new TreeNode(1);
    	TreeNode e = new TreeNode(3);
    	TreeNode f = new TreeNode(-2);
    	TreeNode g = new TreeNode(-1);
    	a.left = b;
    	a.right = c;
    	b.left = d;
    	b.right = e;
    	d.left = g;
    	c.left = f;

    	return a;
    }

    public static void main(String[] args) {
    	Tree tree = new Tree();
    	String[] nodeList = {"10", "5", "3", "3", "null", "null","-2","null","null","2","null","1","null","null","-3","null","11","null","null"};

    	PathSum test = new PathSum();
    	TreeNode root = tree.deSerialize(Arrays.asList(nodeList));

    	test.test("test-1", root, 8, 3);



    	TreeNode root2 = test.tree2();
    	test.test("test-2", root2, -1, 4);
    }
}