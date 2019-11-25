# coding:utf-8
import sys
sys.path.append("../../")

from util import io 

import numpy as np

import pyKriging
from pyKriging.krige import kriging
from pyKriging.samplingplan import samplingplan
from pyKriging.testfunctions import testfunctions

dataFilePath = "../../data/samples-data.data"
labelsFilePath = "../../data/samples-data-labels.data"
def getTrainData():
    """获取训练数据"""
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

X, Y = getTrainData()

k = kriging(X, Y)
k.train()
# k.snapshot()
testX = np.array([-60.,168.3,-121.16,-56.34,-77.])
pdtValue = k.predict(X)
print("pdtValue: {}, label: {}".format(pdtValue, Y[0]))