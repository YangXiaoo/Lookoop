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

print("xx"+"ee")

