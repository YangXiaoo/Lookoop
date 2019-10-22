/**
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
*/

// 2018-7-11
// 113. Path Sum II

// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bbd_medium_Path_Sum {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> tmp = new ArrayList<Integer>();

        if (root == null) return res;
        dfs(res,tmp,root,sum);
        return res;
    }

    public void dfs(List<List<Integer>> res, List<Integer> tmp, TreeNode root, int sum) {
        if (root == null)
            return;
        if (root.left == null && root.right == null) {
            tmp.add(root.val);
            if (isEqual(tmp, sum)) {
                res.add(new ArrayList(tmp)); 
                // res.add(tmp); 结果为[[],[]]
                // res.append(tmp[:]) 与python类似
            }
            tmp.remove(tmp.size()-1);
            return;
        } else {
            tmp.add(root.val);
            dfs(res, tmp, root.left, sum);
            dfs(res, tmp, root.right, sum);
            tmp.remove(tmp.size()-1);
        }
    }

    public boolean isEqual(List<Integer> tmp, int sum) {
        int total = 0;
        for (int i = 0; i < tmp.size(); i++) {
            total += tmp.get(i);
        }

        return sum == total;
    }
}