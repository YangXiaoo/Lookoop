# coding:utf-8
import math
import numpy as np 
import datetime
def foo():
    print(GLOBAL_VAR)

GLOBAL_VAR = "GLOBAL_VAR"

foo()

string = "hello world"

def characterCount(string):
    """统计词频"""
    ret = {}
    for c in string:
        if c == ' ': continue
        ret[c] = ret.get(c, 0) + 1

    return ret

def testCharacterCount():
    """测试"""
    string = "hello world"
    ret = characterCount(string)

    print(ret)

def openSomething():
    with open("record.txt") as f:
        lines = f.readlines()
        for line in lines:
            pass # ?????
class A():
    def __init__(self):
        self.data = []

    def add(self):
        self.data.append(1)


if __name__ == '__main__':
    a = 1 - 1e-4
    b = 1
    for i in range(5000):
        b = b * a
    print(b)
    a = 2 if 3 > 4 else 0
    print(a)

