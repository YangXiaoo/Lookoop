'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# 2018-9-27
# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        res = []
        if root:
            queue.append(root)
            res.append(root.val)
        else:
            return res

        while len(queue) != 0:
            lens = len(queue)
            tmp_nodes = []
            while lens > 0:
                node = queue.pop()
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)
                lens -= 1
            if len(tmp_nodes) != 0:
                last = tmp_nodes[-1].val
                if last:
                    res.append(last)
            tmp_nodes = tmp_nodes[::-1]
            queue.extend(tmp_nodes[:])

        return res






        