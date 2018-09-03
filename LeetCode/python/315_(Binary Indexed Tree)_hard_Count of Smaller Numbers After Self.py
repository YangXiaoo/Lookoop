'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

# 2018-9-3
# 315. Count of Smaller Numbers After Self
# Binary Indexed Tree
class BSTNode(object):
    def __init__(self, index, x):
        self.val = x
        self.right = None
        self.left = None
        self.count = 0
        self.index = index
        self.leftSize = 0

class BinarySearchTree(object):
    def __init__(self, lens):
        self.root = None
        self.res = [0] * lens # 直接加入此项，避免重新遍历

    def insert(self, x, root, pre=None, left=False):
        if self.root == None:
            self.root = x
            self.res[x.index] = x.count
            return 
        if root == None:
            if left:
                pre.left = x
            else:
                pre.right = x
            self.res[x.index] = x.count
            return 
        if x.val < root.val:
            pre = root
            root.leftSize += 1
            self.insert(x, root.left, pre, True)
        elif x.val == root.val:
            root.leftSize += 1
            self.insert(x, root.left, root, True)
        else:
            x.count += root.leftSize + 1
            self.insert(x, root.right, root)


    # def traversal(self):
    #     root = self.root
    #     def tra(root):
    #         if root != None:
    #             # print(root.val)
    #             self.hash[root.index] = root.count
    #             tra(root.left)
    #             tra(root.right)
    #     tra(root)


class Solution1:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        tree = BinarySearchTree(len(nums))
        for index, i in enumerate(nums[::-1]):
            node = BSTNode(index, i)
            tree.insert(node, tree.root)
        return tree.res[::-1]
        # tree.traversal()
        # for i in range(len(nums)):
        #     res[i] = tree.hash[i]
        # return res[::-1]

import bisect
class Solution2:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        tmp = []
        for i in nums[::-1]:
            index = bisect.bisect_left(tmp, i)
            res.append(index)
            tmp.insert(index, i)
        return res[::-1]


nums = [5,2,0,2,1, 7,7,5,4,3,2]
test = Solution1()
res = test.countSmaller(nums)
print(res)
# [7, 2, 0, 1, 0, 4, 4, 3, 2, 1, 0]