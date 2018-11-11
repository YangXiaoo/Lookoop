'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# 2018-11-11
# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time Limit Exceeded 47/48
import collections
class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret, nil = [], "null"
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:
            tmp_len, tmp_res, count = len(queue), [], 0
            while count < tmp_len:
                tmp_node = queue.popleft()
                if tmp_node == None:
                    tmp_res.append(nil)
                    queue.extend([None, None])
                else:
                    tmp_res.append(tmp_node.val) 
                    queue.extend([tmp_node.left, tmp_node.right])
                count += 1
            if [nil] * tmp_len == tmp_res:
                return ret
            # print(ret, tmp_len)
            ret.extend(tmp_res)
        # print(ret)
        return ret # [1,2,3,null,null,4,5]


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        data = data[::-1]
        len_data = len(data)
        height, root = 0, TreeNode(data[-1])
        up_nodes = collections.deque()
        up_nodes.append(root)
        data.pop()
        while len(data) != 0:
            up_len, count = len(up_nodes), 0
            while count < up_len or len(data) != 0:
                tmp_root = up_nodes.popleft()
                if tmp_root == None:
                    data.pop()
                    data.pop()
                    up_nodes.extend([None, None])
                else:
                    tmp_node_left_val = data.pop()
                    tmp_node_right_val = data.pop()
                    if tmp_node_left_val != 'null':
                        tmp_node_left = TreeNode(tmp_node_left_val)
                        tmp_root.left = tmp_node_left
                        up_nodes.append(tmp_node_left)
                    else:
                        up_nodes.append(None)

                    if tmp_node_right_val != 'null':
                        tmp_node_right = TreeNode(tmp_node_right_val)
                        tmp_root.right = tmp_node_right
                        up_nodes.append(tmp_node_right)
                    else:
                        up_nodes.append(None)
                count += 1
        return root

class Codec2:
    def __init__(self):
        self.ret = []
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return 
        self.serialize(root.left)
        self.ret.append(root.val)
        self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None
        data = data[::-1]
        len_data = len(data)
        height, root = 0, TreeNode(data[-1])
        up_nodes = collections.deque()
        up_nodes.append(root)
        data.pop()
        while len(data) != 0:
            up_len, count = len(up_nodes), 0
            while count < up_len or len(data) != 0:
                tmp_root = up_nodes.popleft()
                if tmp_root == None:
                    data.pop()
                    data.pop()
                    up_nodes.extend([None, None])
                else:
                    tmp_node_left_val = data.pop()
                    tmp_node_right_val = data.pop()
                    if tmp_node_left_val != 'null':
                        tmp_node_left = TreeNode(tmp_node_left_val)
                        tmp_root.left = tmp_node_left
                        up_nodes.append(tmp_node_left)
                    else:
                        up_nodes.append(None)

                    if tmp_node_right_val != 'null':
                        tmp_node_right = TreeNode(tmp_node_right_val)
                        tmp_root.right = tmp_node_right
                        up_nodes.append(tmp_node_right)
                    else:
                        up_nodes.append(None)
                count += 1
        return root

nums = [1,2,3,'null','null',4,5]
test = Codec2()
root = test.deserialize(nums)
# print(root)
se = test.serialize(root)
print(test.ret)


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))