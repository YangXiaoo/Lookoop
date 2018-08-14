# 2018-8-10
# B-tree
# Reference
# Introduction to Algorithms [P174]
# python http://blog.51cto.com/thuhak/1269059
# https://blog.csdn.net/screaming/article/details/50932166
# C https://blog.csdn.net/xiaohusaier/article/details/76708490
# detail introduction: https://blog.csdn.net/endlu/article/details/51720299
# C++ ** https://blog.csdn.net/Ture010Love/article/details/6720855
# CSDN https://blog.csdn.net/guoziqing506/article/details/64122287
# https://www.cs.usfca.edu/~galles/visualization/BTree.html

from random import randint,choice
from bisect import bisect_left
from collections import deque

class BTreeNode(object):
    def __init__(self, t, parent=None):
        self.clist = []
        self.klist = []
        self.degree = t # integer
        self.parent = parent

    def isleaf(self):
        return len(self.clist) == 0

    def traversal(self):
        res = []
        def getValue(n):
            if n.clist == []:
                res.extend(n.klist)
            else:
                for i,k in enumerate(n.klist):
                    getValue(n.clist[i])
                    res.append(k)
                getValue(n.clist[-1]) # the last one
        getValue(self)
        return res

class IndexFile(object):
    def __init__(self, fname, cellsize):
        f = open(fname, "w+")
        f.close()
        self.name = fname
        self.cellsize = cellsize

    def write(obj, pos):
        pass

    def read(obj, pos):
        pass        

class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.degree = t
        self.full = t * 2 - 1
        self.mid = int(self.full / 2 + 1)

    def insert(self,k):
        T = self.root
        def split(node):
            mid = self.mid
            new = BTreeNode(self.degree, parent = node.parent)
            new.klist = node.klist[mid:]
            new.clist = node.clist[mid:]
            for c in new.clist:
                c.parent = new
            if node.parent is None:
                newroot = BTreeNode(self.degree)
                newroot.klist = [node.klist[mid-1]]
                newroot.clist = [node, new]
                node.parent = new.parent = newroot
                self.root = newroot
            else:
                index = node.parent.clist.index(node)
                node.parent.klist.insert(index, node.klist[mid-1])
                node.parent.clist.insert(index+1, new)
            node.klist = node.klist[:mid-1] # remove node.klist[mid-1]
            node.clist = node.clist[:mid]
            return node.parent

        def insertNode(node):
            # print(node.klist)
            if len(node.klist) == self.full:
                insertNode(split(node))
            else:
                if node.klist == []:
                    node.klist.append(k)
                else:
                    if node.isleaf():
                        p = bisect_left(node.klist, k)
                        node.klist.insert(p, k)
                    else:
                        p = bisect_left(node.klist, k)
                        insertNode(node.clist[p])

        insertNode(T)

    def searchRange(self, mins=None, maxs=None):
        res = []
        root = self.root
        if mins is None and maxs is None:
            print("Miss input")
            return False
        if mins is not None and maxs is not None and maxs < mins:
            print("Error input")
            return False
        def searchNode(n):
            if mins is None:    
                if not n.isleaf():
                    for i,k in enumerate(n.klist):
                        if v <= maxs:
                            res.extend(n.clist[i].traversal())
                            res.append(v)
                        else:
                            break
                    searchNode(n.clist[-1])
                else:
                    for k in n.klist:
                        if k <= maxs:
                            res.append(k)
                        else:
                            break
            elif maxs is None:
                if not n.isleaf():
                    for i,k in enumerate(n.klist):
                        if v >= mins:
                            searchNode(n.clist[i])
                            while i < len(n.klist):
                                res.extend(n.clist[i].traversal())
                                res.append(n.klist[i])
                                i += 1
                        else:
                            break
                    searchNode(n.clist[-1])
                else:
                    for k in n.klist:
                        if k <= maxs:
                            res.append(k)
                        else:
                            break
            else:
                if not n.isleaf():
                    for i,v in enumerate(n.klist):
                        if v < mins:
                            continue
                        elif mins <= v <= maxs:
                            searchNode(n.clist[i])
                            res.append(v)
                        elif v > maxs:
                            searchNode(n.clist[i])
                    searchNode(n.clist[-1])
                else:
                    for v in n.klist:
                        if mins <= v <= maxs:
                            res.append(v)
                        elif v > maxs:
                            break
        searchNode(root)
        return res

def test():
    mins=50
    maxs=200
    testlist=[]
    for i in range(1,1001):
        key=randint(1,1000)
        testlist.append(key)
    mybtree=BTree(3)
    for x in testlist:
        mybtree.insert(x)
    print ('\nnow we are searching item between %d and %d\n'%(mins,maxs))
    print ([k for k in mybtree.searchRange(mins,maxs)])

if __name__=='__main__':
    test()