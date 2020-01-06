# coding:utf-8
import sys
sys.path.append("../")

import math
import numpy as np 
import datetime
import os
import sklearn

from util import io, tool

dataFilePath = "../data/samples-data.data"
labelsFilePath = "../data/samples-data-labels.data"

def getTrainData():
    """获取训练数据"""
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

def foo():
    print(GLOBAL_VAR)

GLOBAL_VAR = "GLOBAL_VAR"

foo()

class A():
    def __init__(self):
        self.data = []

    def add(self):
        self.data.append(1)


if __name__ == '__main__':
    nums = np.array([[1,2,3],[4,5,6]])
    print(nums)
    print(list(nums))

