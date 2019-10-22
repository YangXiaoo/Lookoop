# coding:utf-8

"""
姓氏是人的符号标志，是家族血脉的传承；族谱是家族血脉传承的文字记载。同姓的两个中国人，根据族谱或许能够查出上面几代内是同一个祖先。查一下族谱，也许当代某位同姓名人就是你的远房亲戚，惊喜不惊喜，意外不意外！！！



输入
二元查找树（1.若左子树不空，左子树值都小于父节点；2.如右子树不空，右子树值都大于父节点；3.左、右子树都是二元查找树；4. 没有键值相等的节点）上任意两个节点的值，请找出它们最近的公共祖先。

输入三行行，第一行为树层级，第二行为数节点（其中-1表示为空节点），第三行为需要查找祖先的两个数。

在例图中（虚线框没有真实节点，为了输入方便对应位置输-1）查找12和20的最近公共祖先输入为：

4

9 6 15 2 -1 12 25 -1 -1 -1 -1 -1 -1 20 37

12 20


输出
输出给出两个数在树上的最近公共祖先数值，如果没有公共祖先，输出-1；如果其中一个节点是另一个节点的祖先，输出这个祖先点（如例图中找15、20最近公共祖先，输出15）；如果输入无效，输出-1。


样例输入
4
9 6 15 2 -1 12 25 -1 -1 -1 -1 -1 -1 20 37
12 20
样例输出
15
"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(level, nums):
    root = TreeNode(nums[0])
    que = [root]
    index = 1
    flag = False
    while len(que) != 0:
        tmp = []
        curSize = len(que)
        for i in range(curSize):
            curNode = que.pop(0)
            left = nums[index]
            index += 1
            if index == len(nums) - 1:
                flag = True
            right = nums[index]

            leftNode = None
            rightNode = None
            if left != -1:
                leftNode = TreeNode(left)
                tmp.append(leftNode)

            if right != -1:
                rightNode = TreeNode(right)
                tmp.append(rightNode)

            curNode.left = leftNode
            curNode.right = rightNode
        if flag:
            break
        que = tmp

    return root

def ancestor(root, node1, node2):
    if  root == None or root.val == node1 or root.val == node2:
        return root

    left = ancestor(root.left, node1, node2)
    right = ancestor(root.right, node1, node2)

    if left and right:
        return root

    return [right, left][right == None]


def solver(n, nums, node1, node2):
    root = constructTree(n, nums)

    ret = ancestor(root, node1, node2)

    return ret 


def test():
    n = 4
    strs = "9 6 15 2 -1 12 25 -1 -1 -1 -1 -1 -1 20 37"
    nums = list(map(int, strs.split()))
    node1, node2 = 12, 20
    ret = solver(n, nums, node1, node2)

    if ret != None:
        print(ret.val)
    else:
        print(-1)

def inputs():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    node1, node2 = list(map(int, input().strip().split()))
    ret = solver(n, nums, node1, node2)

    if ret != None:
        print(ret.val)
    else:
        print(-1)

if __name__ == '__main__':
    test()