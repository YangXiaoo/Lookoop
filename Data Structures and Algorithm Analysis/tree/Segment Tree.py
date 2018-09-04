# 2018-9-4
# Segment Tree
# https://www.cnblogs.com/xiaoyao24256/p/6590885.html
# https://blog.csdn.net/icyday/article/details/50778104

"""
线段树又名区间树， 是一种二叉搜索树。
当父节点的区间为[x, y]时，左子孩子的区间必须为[x. (x + y) / 2], 有孩子区间必为[(x + y) / 2 + 1, y].
常用于： 建树, 单点修改, 区间求和, 查询区间最值, 区间修改
"""

class ST(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.sum = 0
        self.lazyTag = 0
        self.left = None
        self.right = None
        if l < r:
            mid = (l + r) // 2
            self.left = ST(l, mid)
            self.right = ST(mid + 1, r)


    def build(self, p, value):
        if self.l == self.r:
            self.sum = value
            return 
        mid = (self.l + self.r) // 2
        if p <= mid:
            self.left.build(p, value)
        else:
            self.right.build(p, value)

        self.pushUp()

    def pushUp(self):
        self.sum = self.left.sum + self.right.sum

    def query(self, x, y):
        if x <= self.l and y >= self.r:
            return self.sum

        # 叶子
        if self.l == self.r:
            return self.sum

        mid = (self.l + self.r) // 2
        if mid >= y:
            return self.left.query(x, y)
        elif mid < x:
            return self.right.query(x, y)
        else:
            return self.left.query(x, mid) + self.right.query(mid + 1, y)


def test():
    N = 1026
    tree = ST(0, N)

    for i in range(N+1):
        tree.build(i, 1)
    print(tree.query(20, 50))

if __name__ == "__main__":
    test()
