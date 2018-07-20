/**
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
*/

// 2018-7-20
// 129. Sum Root to Leaf Numbers
// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bcj_medium_Sum_Root_to_Leaf_Numbers {
    private int result = 0; // 记录总的结果
    private int num = 0; // 记根到叶子的数字

    public int sumNumbers(TreeNode root) {
        sum(root);
        return result;
    }

    private void sum(TreeNode root) {
        if (root != null) {
            num = num*10 + root.val;

            // 已经到了根结点了
            if (root.left == null && root.right == null) {
                result += num;
            }
            sum(root.left);
            sum(root.right);
            // 返回上一层num要还原
            num /= 10;
        }
    }
}
