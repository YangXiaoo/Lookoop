/**
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
*/

// 2018-7-25
// 145. Binary Tree Postorder Traversal
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class 145_hard_Binary_Tree_Postorder_Traversal {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>(); // Queue<TreeNode> stack = new LinkedList<>(); 不能实现，必须用Stack
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                res.add(0, cur.val);
                stack.push(cur);
                cur = cur.right;
            }

            cur = stack.pop();
            cur = cur.left;
        }

        return res;      
    }
}
/**
# Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 右中左,然后倒序
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cur = root
        while cur != None or len(stack) != 0:
            while cur!=None:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left

        return res[::-1]       
*/
    public List<Integer> preorderTraversal2(TreeNode root) {
        if (root == null) {
            return list;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode tempNode = null;
        while (!stack.isEmpty()) {
            tempNode = stack.pop();
            list.add(tempNode.val);
            if (tempNode.right != null) {
                stack.push(tempNode.right);
            }
            if (tempNode.left != null) {
                stack.push(tempNode.left);
            }
        }
        return list;
    }
}