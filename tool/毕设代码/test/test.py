# coding:utf-8
import math
import numpy as np 
import datetime
import os


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
    modelPathFormat = "../data/sarsa-2020-1-5.model"
    print(os.path.basename(modelPathFormat))
    print(os.path.dirname(modelPathFormat))

