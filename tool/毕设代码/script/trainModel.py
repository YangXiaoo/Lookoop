# coding:utf-8
# 2019/11/5
"""
将模型训练好并保存
"""
import sys
sys.path.append("../")

from util import io 
from util import tool
import model

dataFilePath = "../data/samples-data.data"
labelsFilePath = "../data/samples-data-labels.data"
stackModelSavingPath = "../data/stackingModel.model" # 融合模型保存路径


def getTrainData():
    """获取训练数据"""
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

def train():
    """训练stacking模型并保存"""
    X, Y = getTrainData()
    stackModel = model.train_model(X, Y)
    io.saveData(stackModel, stackModelSavingPath)

def trainBySingleModel():
    """训练单个模型并保存结果"""
    X, Y = getTrainData()
    modelSaving = "../data/singleModel/{}.model"
    names, models = model.getModel()

    for n, m in zip(names, models):
        singleModle = model.train_by_model(n, X, Y)
        io.saveData(singleModle, modelSaving.format(n))

def testModelPdt():
    """测试模型的预测能力"""
    stackModel = io.getData(stackModelSavingPath)
    X, Y = getTrainData()
    pdtValue = stackModel.predict(X)
    retMSE = tool.computeMSE(pdtValue, Y)
    print("MSE : {}".format(retMSE))
    # print("X-pdt: {}".format(pdtValue))
    # print("Y-val: {}".format(Y))

def testSingleModel():
    X, Y = getTrainData()
    modelSaving = "../data/singleModel/{}.model"
    names, models = model.getModel()

    for n in names:
        m = io.getData(modelSaving.format(n))
        pdtValue = m.predict(X)
        retMSE = tool.computeMSE(pdtValue, Y)
        print("model: {}, MSE : {}".format(n, retMSE))

if __name__ == '__main__':
    testSingleModel()