'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

# 2018-11-19
# 337. House Robber III
# https://leetcode.com/problems/house-robber-iii/


# https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        val = 0
        if root.left != None:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right != None:
            val += self.rob(root.right.left) + self.rob(root.right.right)

        return max(val + root.val, self.rob(root.left) + self.rob(root.right))


# https://leetcode.com/problems/house-robber-iii/discuss/79363/Easy-understanding-solution-with-dfs
# use dfs
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """