# 2018-9-4
# Segment Tree
# https://www.cnblogs.com/xiaoyao24256/p/6590885.html


"""
线段树又名区间树， 是一种二叉搜索树。
当父节点的区间为[x, y]时，左子孩子的区间必须为[x. (x + y) / 2], 有孩子区间必为[(x + y) / 2 + 1, y].
常用于： 建树, 单点修改, 区间求和, 查询区间最值, 区间修改
"""

class STNode(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.sum = 0
        self.lazyTag = 0
        self.left = None
        self.right = None


class STTree(object):
    def __init__(self, size):
        self.tree = [STNode()] * size