# coding:utf-8
# 2019/11/5
"""
将模型训练好并保存
"""
import sys
sys.path.append("../")
import logging
from sklearn.linear_model import LinearRegression, ElasticNet, Ridge, RidgeCV, Lasso
from sklearn.svm import LinearSVR
from sklearn.kernel_ridge import KernelRidge

from util import io 
from util import tool
import model


dataFilePath = "../data/samples-data.data"
labelsFilePath = "../data/samples-data-labels.data"
stackModelSavingPath = "../data/stackingModel.model" # 融合模型保存路径
singleModelSaving = "../data/singleModel/{}.model"

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)

def getTrainData():
    """获取训练数据"""
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

class ModelAdapter(object):
    def __init__(self, model):
        self.model = model 

    def fit(self, x, y):
        pass

def train():
    """训练stacking模型并保存"""
    X, Y = getTrainData()
    stackModel = model.train_model(X, Y, collectionModel=Lasso())
    io.saveData(stackModel, stackModelSavingPath)

def trainBySingleModel():
    """训练单个模型并保存结果"""
    X, Y = getTrainData()
    names, models = model.getModel()

    for n, m in zip(names, models):
        singleModle = model.train_by_model(n, X, Y)
        io.saveData(singleModle, singleModelSaving.format(n))

def testModelPdtRMAE():
    """使用所有数据进行训练，然后对训练数据进行预测"""
    logger.info("{}-testModelPdtRMAE-{}".format('*'*25, '*'*25))
    stackModel = io.getData(stackModelSavingPath)
    X, Y = getTrainData()
    pdtValue = stackModel.predict(X)
    retMSE = tool.computeRMAE(Y, pdtValue)
    logger.info("stacking model using all data, RMAE : {}".format(retMSE))

def testSingleModelRMAE():
    """使用所有数据进行训练，然后对训练数据进行预测"""
    logger.info("{}-testSingleModelRMAE-{}".format('*'*25, '*'*25))
    X, Y = getTrainData()
    names, models = model.getModel()

    for n in names:
        m = io.getData(singleModelSaving.format(n))
        pdtValue = m.predict(X)
        retMSE = tool.computeRMAE(Y, pdtValue)
        logger.info("model: {}, using all data, RMAE : {}".format(n, retMSE))

def crossValidateRMAE():
    """使用交叉验证验证模型精度"""
    logger.info("{}-crossValidateRMAE-{}".format('*'*25, '*'*25))
    X, y = getTrainData()

    _, trainModels = model.getModel()
    stackModel = model.stacking(trainModels, LinearRegression())
    rmae = tool.crossValueScore(stackModel, X, y, tool.computeRMAE)
    logger.info("stacking model, cross validate RMAE: {}".format(rmae))

    names, models = model.getModel()

    for n, m in zip(names, models):
        rmae = tool.crossValueScore(m, X, y, tool.computeRMAE)
        logger.info("model: {}, cross validate RMAE: {}".format(n, rmae))

def testModelPdtMAE():
    """使用所有数据进行训练，然后对训练数据进行预测"""
    logger.info("{}-testModelPdtMAE-{}".format('*'*25, '*'*25))
    stackModel = io.getData(stackModelSavingPath)
    X, Y = getTrainData()
    pdtValue = stackModel.predict(X)
    retMSE = tool.computeMAE(Y, pdtValue)
    logger.info("stacking model using all data, MAE : {}".format(retMSE))

def testSingleModelMAE():
    """使用所有数据进行训练，然后对训练数据进行预测"""
    logger.info("{}-testSingleModelMAE-{}".format('*'*25, '*'*25))
    X, Y = getTrainData()
    names, models = model.getModel()

    for n in names:
        m = io.getData(singleModelSaving.format(n))
        pdtValue = m.predict(X)
        retMSE = tool.computeMAE(Y, pdtValue)
        logger.info("model: {}, using all data, MAE : {}".format(n, retMSE))

def crossValidateMAE():
    """使用交叉验证验证模型精度"""
    logger.info("{}-crossValidateMAE-{}".format('*'*25, '*'*25))
    X, y = getTrainData()

    _, trainModels = model.getModel()
    stackModel = model.stacking(trainModels, LinearRegression())
    rmae = tool.crossValueScore(stackModel, X, y, tool.computeMAE)
    logger.info("stacking model, cross validate MAE: {}".format(rmae))

    names, models = model.getModel()

    for n, m in zip(names, models):
        rmae = tool.crossValueScore(m, X, y, tool.computeMAE)
        logger.info("model: {}, cross validate MAE: {}".format(n, rmae))

def getSecondModel():
    """获得次级模型"""
    names = []
    models = [
        LinearRegression(),
        ElasticNet(),
        KernelRidge(),
        LinearSVR(),
        Lasso()
    ]

    for m in models:
        names.append(m.__class__.__name__)

    return names, models


def secondModelValid():
    """对不同次级模型进行评估"""
    logger.info("{}-secondModelValid-{}".format('*'*25, '*'*25))
    

    names, models = getSecondModel()
    for name, m in zip(names, models):
        X, y = getTrainData()
        stackModel = model.train_model(X, y, collectionModel=m)

        pdtValue = stackModel.predict(X)
        pdtMAE = tool.computeMAE(y, pdtValue)
        logger.info("second model : {}, stacking model, pdt MAE: {}".format(name, pdtMAE))
        pdtRMAE = tool.computeRMAE(y, pdtValue)
        logger.info("second model : {}, stacking model, pdt RMAE: {}".format(name, pdtRMAE))

        mae = tool.crossValueScore(stackModel, X, y, tool.computeMAE)
        logger.info("second model : {}, stacking model, cross validate MAE: {}".format(name, mae))
        rmae = tool.crossValueScore(stackModel, X, y, tool.computeRMAE)
        logger.info("second model : {}, stacking model, cross validate RMAE: {}".format(name, rmae))



if __name__ == '__main__':
    train()
    # trainBySingleModel()
    # testModelPdtRMAE()
    # testModelPdtMAE()
    # testSingleModelRMAE()
    # testSingleModelMAE()
    # crossValidateRMAE()
    # crossValidateMAE()
    # secondModelValid()
