# coding:utf-8
# 2019/11/5
"""
将模型训练好并保存
"""
import sys
sys.path.append("../")
import logging
from sklearn.linear_model import LinearRegression

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
    stackModel = model.train_model(X, Y)
    io.saveData(stackModel, stackModelSavingPath)

def trainBySingleModel():
    """训练单个模型并保存结果"""
    X, Y = getTrainData()
    names, models = model.getModel()

    for n, m in zip(names, models):
        singleModle = model.train_by_model(n, X, Y)
        io.saveData(singleModle, singleModelSaving.format(n))

def testModelPdt():
    """使用所有数据进行训练，然后对训练数据进行预测"""
    logger.info("{}-testModelPdt-{}".format('*'*25, '*'*25))
    stackModel = io.getData(stackModelSavingPath)
    X, Y = getTrainData()
    pdtValue = stackModel.predict(X)
    retMSE = tool.computeRMAE(Y, pdtValue)
    logger.info("stacking model using all data, RMAE : {}".format(retMSE))

def testSingleModel():
    """使用所有数据进行训练，然后对训练数据进行预测"""
    logger.info("{}-testSingleModel-{}".format('*'*25, '*'*25))
    X, Y = getTrainData()
    names, models = model.getModel()

    for n in names:
        m = io.getData(singleModelSaving.format(n))
        pdtValue = m.predict(X)
        retMSE = tool.computeRMAE(Y, pdtValue)
        logger.info("model: {}, using all data, RMAE : {}".format(n, retMSE))

def crossValidate():
    """使用交叉验证验证模型精度"""
    logger.info("{}-crossValidate-{}".format('*'*25, '*'*25))
    X, y = getTrainData()

    _, trainModels = model.getModel()
    stackModel = model.stacking(trainModels, LinearRegression())
    rmae = tool.crossValueScore(stackModel, X, y, tool.computeRMAE)
    logger.info("stacking model, cross validate RMAE: {}".format(rmae))

    names, models = model.getModel()

    for n, m in zip(names, models):
        rmae = tool.crossValueScore(m, X, y, tool.computeRMAE)
        logger.info("model: {}, cross validate RMAE: {}".format(n, rmae))

if __name__ == '__main__':
    testModelPdt()
    testSingleModel()
    crossValidate()
