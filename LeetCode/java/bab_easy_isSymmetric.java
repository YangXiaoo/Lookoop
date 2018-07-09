/**
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
*/

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

// 2018-7-9
// 使用递归 
// 101 isSymmetric
class bab_easy_isSymmetric {
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