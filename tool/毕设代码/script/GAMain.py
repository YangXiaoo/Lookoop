# coding:utf-8
# 2019-12-3
# 遗传算法寻优
# 源码路径: C:\Users\Yauno\AppData\Roaming\Python\python36\site-packages
import sys
sys.path.append("../")

import logging
import numpy as np
import geatpy as ea
import pickle

import model
from util import io, tool
from quadRegresstion import *

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)

# 模型路径format
modelPathFormat = r"C:\Study\github\Lookoops\tool\毕设代码\data/{}.model"
singleModelPathFormat = r"C:\Study\github\Lookoops\tool\毕设代码\data/singleModel/{}.model"

def getModelName():
    """获得选择出来的最佳模型名称"""
    names = ["quadraticRegression", "stackingModel"]

    return names

def getSingleModel():
    """获得单个模型的名称"""
    names, models = model.getModel()

    return names

class MyProblem(ea.Problem): # 继承Problem父类
    def __init__(self, modelName):
        name = 'MyProblem'
        self.modelName = modelName
        M = 1 # 目标维数
        maxormins = [1] # 1：最小化该目标；-1：最大化该目标
        self.Dim = 5 # 决策变量维数
        varTypes = [0 for _ in range(self.Dim)] # 元素为0表示对应的变量是连续的；1表示是离散的
        # lb = [-300 for _ in range(self.Dim)] # 决策变量下界
        # ub = [300 for _ in range(self.Dim)] # 决策变量上界
        lb = [-300, -300, -300, -300, -200]
        ub = [300, 300, 100, 300, 200]
        lbin = [0, 0, 0, 0, 0]  # 1表示能取到边界，0表示取不到边界
        ubin = [0, 0, 0, 0, 0]
        ea.Problem.__init__(self, name, M, maxormins, self.Dim, varTypes, lb, ub, lbin, ubin)
    
    def aimFunc(self, pop):
        """自定义目标函数"""
        model = self.loadModel()
        X = pop.Phen
        # logger.info(X)
        feature = []
        for i in range(self.Dim):
            feature.append(X[:, [i]][0])
        val = model.predict(X)
        ret = []
        for v in val:
            ret.append(v)
        x = np.array(ret)
        x = x[:, np.newaxis]
        pop.ObjV = x
    
    def loadModel(self):
        """加载模型"""
        modelPath = modelPathFormat.format(self.modelName)
        model = io.getData(modelPath)

        return model

def train(modelName, dim, maxIter):
    """训练"""
    problem = MyProblem(modelName)
    NIND = dim  # 种群规模

    Encoding = 'RI' # 实整数编码
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)
    
    population = ea.Population(Encoding, Field, NIND)
    myAlgorithm = ea.soea_SEGA_templet(problem, population)
    myAlgorithm.MAXGEN = maxIter # 最大进化代数
    [population, obj_trace, var_trace] = myAlgorithm.run()
    population.save()

    # 输出结果
    best_gen = np.argmin(problem.maxormins * obj_trace[:, 1]) # 记录最优种群个体是在哪一代
    best_ObjV = obj_trace[best_gen, 1]
    logger.info('最优的目标函数值为：%s'%(best_ObjV))
    logger.info('最优的控制变量值为：')
    for i in range(var_trace.shape[1]):
        logger.info(var_trace[best_gen, i])
    logger.info('有效进化代数：%s'%(obj_trace.shape[0]))
    logger.info('最优的一代是第 %s 代'%(best_gen + 1))
    logger.info('评价次数：%s'%(myAlgorithm.evalsNum))
    logger.info('时间已过 %s 秒'%(myAlgorithm.passTime))

def mainModelOptimus():
    """对二次响应面，Stacking模型进行优化"""
    dim = 1000
    maxIter = 1000
    names = getModelName()
    for n in names:
        logger.info("cur params, dim: {}, maxIter: {}".format(dim, maxIter))
        logger.info("optimus model: {}".format(n))
        train(n, dim, maxIter)

def singleModelOptimus():
    """对单个模型进行优化"""
    global modelPathFormat
    modelPathFormat = singleModelPathFormat
    dim = 1000
    maxIter = 10000
    names = getSingleModel()
    for n in names:
        logger.info("cur params, dim: {}, maxIter: {}".format(dim, maxIter))
        logger.info("optimus model: {}".format(n))
        train(n, dim, maxIter)

if __name__ == '__main__':
    mainModelOptimus()