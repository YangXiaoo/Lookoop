"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

Example 4:
Input:[1,1],[1,null,1]
Output: false
"""
# 2018-6-30
# Same Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# error for example 4
class Solution1:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        l1 = self.recursive(p,[])
        l2 = self.recursive(q,[])

        return l1 == l2

    def recursive(self,root,lists):
        if root == None:
            lists.append("nul")
            return 
        self.recursive(root.left,lists)
        lists.append(root.val)
        self.recursive(root.right,lists)

        return lists


# https://leetcode.com/problems/same-tree/discuss/32687/Five-line-Java-solution-with-recursion
class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True 
        if p == None or q == None:
            return False 

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


"""
# java
public boolean isSameTree(TreeNode p, TreeNode q) {
    if(p == null && q == null) return true;
    if(p == null || q == null) return false;
    if(p.val == q.val)
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    return false;
}
"""