/**
 * Definition for a binary tree node.
 */
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    // 构造器
    TreeNode(int x) { 
        val = x;
    }
}

// 101
// 2018-7-9
// 使用递归 
// isSymmetric
// https://blog.csdn.net/crazy1235/article/details/51541984
class 101_easy_isSymmetric {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
        	return true;
        }

        return checkNodes(root.left, root.right);
    }

    public boolean checkNodes(TreeNode node1, TreeNode node2) {
    	if (node1 == null && node2 == null) {
    		return true;
    	}

    	if (node1 == null || node2 == null) {
    		return false;
    	}

    	if (node1.val != node2.val) {
    		return false;
    	} else {
    		return checkNodes(node1.right, node2.left) && checkNodes(node1.left, node2.right);
    	}
    }
}