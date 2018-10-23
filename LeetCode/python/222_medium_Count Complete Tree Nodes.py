'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

# 2018-10-20
# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/maximal-square/


"""
class Solution:
    def countNodes(self, root):
        height = 0
        temp = root
        # get maxHeight of the tree
        while temp != None:
            height += 1
            temp = temp.left
        return self.count(root, height)
            
    def count(self, root, maxHeight):
        if root is None:
            return 0
        if root.left is None:
            return 1
        height = 0
        temp = root.left
        while temp != None:
            height += 1
            temp = temp.right
        if height == (maxHeight - 1): # left tree is perfect at the lowest level
            return pow(2, height) + self.count(root.right, maxHeight - 1)
        else: # right tree must be perfect at one level shallower
            return pow(2, height) + self.count(root.left, maxHeight - 1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        temp = root
        # get maxHeight of the tree
        while temp != None:
            height += 1
            temp = temp.left
        return self.count(root, height)
            
    def count(self, root, maxHeight):
        if root is None:
            return 0
        if root.left is None:
            return 1
        height = 0
        temp = root.left
        while temp != None:
            height += 1
            temp = temp.right
        if height == (maxHeight - 1): # left tree is perfect at the lowest level
            return pow(2, height) + self.count(root.right, maxHeight - 1)  # 右子树是完美树，则左子树也是完美树。右子树进入递归计算
        else: # right tree must be perfect at one level shallower
            return pow(2, height) + self.count(root.left, maxHeight - 1) # 右子树不是完美树此时右子树+左子树进入递归