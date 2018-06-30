"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

# 2018-6-30
# Recovery Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
https://www.cnblogs.com/zuoyuan/p/3746594.html
题目有一个附加要求就是要求空间复杂度为常数空间。而算法一的空间复杂度为O(N)，还不够省空间。以下的解法也是中序遍历的写法，只是非常巧妙，使用了一个prev指针。例如一颗被破坏的二叉查找树如下：

　　　　　　　   4

　　　　　　　/     \

　　        2        6

          /   \    /   \

          1    5  3    7

很明显3和5颠倒了。那么在中序遍历时：当碰到第一个逆序时：为5->4，那么将n1指向5，n2指向4，注意，此时n1已经确定下来了。然后prev和root一直向后遍历，直到碰到第二个逆序时：4->3，此时将n2指向3，那么n1和n2都已经确定，只需要交换节点的值即可。prev指针用来比较中序遍历中相邻两个值的大小关系，很巧妙。 
"""
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root



    def FindTwoNodes(self, root):
            if root:
                self.FindTwoNodes(root.left)
                if self.prev and self.prev.val > root.val:
                    self.n2 = root
                    if self.n1 == None: self.n1 = self.prev # 确定第一个逆序
                self.prev = root
                self.FindTwoNodes(root.right)