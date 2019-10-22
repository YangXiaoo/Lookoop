"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

# 2018-6-30
# Validate Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# LTE
class Solution1:
    def __init__(self):
        self.lists = []
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        self.isValidBST(root.left)
        self.lists.append(root.val)
        # print(self.lists)
        if len(self.lists) == 2:
            if self.lists[1] <= self.lists[0]:
                return False
            else:
                self.lists.pop(0)      
        self.isValidBST(root.right)

        # print(self.lists)
        if len(self.lists) == 2:
            if self.lists[1] <= self.lists[0]:
                return False
            else:
                return True



# root.left.val < root.val and root.right.val > root.val
# https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution
class Solution2:
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # print(root,floor,ceiling)
        if root == None:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False 

        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)



# test
root = TreeNode(1)
s = TreeNode(2)
s.left = TreeNode(3)
root.right = s

test = Solution2()
res = test.isValidBST(root)
print(res)