#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

"""
在某个存储介质以如下形式保存一棵二叉树

1(2(3,4(,5)),6(7,))

上述序列表示的二叉树如下



观察后可以发现，每个节点的格式为

X，X可以为空

或者

X(Y, Z)，其中X不为空

请编写程序将以上述格式输入的二叉树输出为中序遍历顺序

输入
上述格式表示的二叉树字符串，用字符1~9表示每个二叉树的每个节点，字符可以重复使用

输出
二叉树的中序遍历结果


样例输入
1(2(3,4(,5)),6(7,))
样例输出
3245176
"""

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************

# ac 100%
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(serial):
    if len(serial) == 0 or serial[0] in [',', '(']:
        return None
    left, right = 0, len(serial) - 1

    if len(serial) > 1:
        start = 1
        count = 0
        if serial[1] == '(':
            count += 1
            for i in range(2, len(serial)):
                if serial[i] == ')':
                    count -= 1
                elif serial[i] == '(':
                    count += 1
                elif serial[i] == ',':
                    if count == 1:
                        left = i
                        break
    # print("left:{}, right:{}".format(left, right))
    # print("root.val:{}, left:{}, right:{}".format(serial[0],serial[2:left], serial[left:right]))
    root = TreeNode(serial[0])
    root.left = construct(serial[2:left])
    root.right = construct(serial[left+1:right])

    return root

def getInOder(root, ret):
    if root:
        getInOder(root.left, ret)
        ret.append(root.val)
        getInOder(root.right, ret)

def  solution(serial):
    root = construct(serial)
    ret = []
    getInOder(root, ret)

    ret = [str(x) for x in ret]

    return "".join(ret)


#******************************结束写代码******************************

def inputs():
    try:
        _input = input()
    except:
        _input = None

      
    res = solution(_input)

    print(res + "\n")

def test():
    serial = "1(2(3,4(,5)),6(7,))"
    ret = solution(serial)
    print(ret)

if __name__ == '__main__':
    inputs()

