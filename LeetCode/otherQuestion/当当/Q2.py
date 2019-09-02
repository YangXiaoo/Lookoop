# coding:utf-8
# 2019/9/2
# 找出重复次数最多的字符次数

import sys

def solver(s):
    ret = {}
    for c in s:
        if c != ' ':
            ret[c] = ret.get(c, 0) + 1

    maxDup = 0
    for k,v in ret.items():
        if v > maxDup:
            maxDup = v 

    return maxDup

def inputs():
    s = sys.stdin.readline().strip()
    ret = solver(s)
    print(ret)

if __name__ == '__main__':
    inputs()