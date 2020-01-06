# coding:utf-8
# 2019/11/25
"""多元二次响应面拟合"""
import sys
sys.path.append("../")

from util import io 
from util import tool

# 使用非线性最小二乘法拟合
from scipy.optimize import curve_fit
import numpy as np
import logging

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)


dataFilePath = "../data/samples-data.data"
labelsFilePath = "../data/samples-data-labels.data"
curveFitModelSavingPath = "../data/quadraticRegression.model"

def getTrainData():
    """获取训练数据"""
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

class CurveFitHandler():
    """模板"""
    def __init__(self):
        self.y = None
        self.pdtResult = None

    def adaptData(self, X):
        """将数据变形为系数矩阵"""
        newData = []
        for data in X:
            var = [1]
            for v in data:
                var.append(v)

            tmp = []
            for i in range(len(var)):
                for j in range(i, len(var)):
                    tmp.append(var[i]*var[j])
                    
            newData.append(tmp)
        newData = np.array(newData)

        return newData

    def fit(self, X, y):
        """训练"""
        pass

    def amiFunc(self, x, *args):
        """目标函数"""
        pass

    def predict(self, X):
        """预测"""
        pass

    def getMSE(self):
        """计算均方误差"""
        m = np.shape(self.y)[0]
        tmpSum = 0
        for i in range(m):
            tmpSum += abs(self.y[i] - self.pdtResult[i])**2

        return tmpSum / m

class CurveFit(CurveFitHandler):
    """针对五个变量的例子"""
    def __init__(self):
        super(CurveFit, self).__init__()
        self.coef = None    # 二次项系数

    def fit(self, X, y):
        """训练
        @param X mxn维数组，训练数据
        @param y 1xm or mx1 维数组，标签
        """
        if np.shape(y)[0] != 1:
            y = y.reshape(1, len(y))[0]
        self.y = y

        self.coef, pcov = curve_fit(self.amiFunc, X, y)

    def amiFunc(self, x, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                c11, c12, c13, c14, c15, c16, c17, c18, c19, c20):
        """目标函数"""
        newData = self.adaptData(x)
        c = np.array([c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
             c11, c12, c13, c14, c15, c16, c17, c18, c19, c20])
        c = c.reshape(len(c), 1)
        ret = np.dot(newData, c)
        ret = ret.reshape(1, len(ret))[0]   # 转为一维

        return ret

    def predict(self, X):
        """预测
        @param X mxn维数组

        @returns pdt mx1维预测值
        """
        c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20 = self.coef
        self.pdtResult = self.amiFunc(X, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
             c11, c12, c13, c14, c15, c16, c17, c18, c19, c20)

        return self.pdtResult

def crossValidate(X,y):
    """使用交叉验证的方式对模型进行训练，看模型对未知数据的拟合能力"""
    logger.info("{}-crossValidate-{}".format('*'*25, '*'*25))
    curveFit = CurveFit()    
    rmae = tool.crossValueScore(curveFit, X, y, tool.computeRMAE)
    logger.info("quadratic regression, cross validate RMAE: {}".format(rmae))

def train(X, y):
    """使用所有数据对模型进行训练, 保存模型"""
    curveFit = CurveFit()
    curveFit.fit(X, y)
    io.saveData(curveFit, curveFitModelSavingPath)  # 保存当前模型

def testModel(X, y):
    """测试模型对已有训练数据的拟合能力"""
    logger.info("{}-testModel-{}".format('*'*25, '*'*25))
    curveFit = io.getData(curveFitModelSavingPath)
    pdt = curveFit.predict(X)
    rmae = tool.computeRMAE(y, pdt)
    logger.info("quadratic regression, predict rmae : {}".format(rmae))

if __name__ == '__main__':
    X, Y = getTrainData()
    y = Y.reshape(1, len(Y))[0]
    train(X, y)
    testModel(X, y)
    crossValidate(X, y)
    # train(X, y)

