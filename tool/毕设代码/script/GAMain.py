# coding:utf-8
# 2019-12-3
# 遗传算法寻优
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
logger.setLevel(logging.DEBUG)   # 设置日志级别，设置INFO时时DEBUG不可见

modelPathFormat = r"C:\Study\github\Lookoops\tool\毕设代码\data/{}.model"	# 模型路径format

def getModelName():
    """选择出来的最佳模型"""
    names = []
    names.append("quadraticRegression")
    names.append("stackingModel")

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
        lbin = [1, 1, 1, 1, 1]
        ubin = [1, 1, 1, 1, 1]
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, self.Dim, varTypes, lb, ub, lbin, ubin)
    
    def aimFunc(self, pop): # 目标函数
        model = self.loadModel()
        X = pop.Phen # 得到决策变量矩阵
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
        modelPath = modelPathFormat.format(self.modelName)
        model = io.getData(modelPath)

        return model

def train(modelName, dim, maxIter):
	problem = MyProblem(modelName)
	NIND = dim             # 种群规模

	Encoding = 'RI'	# 实整数编码
	Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)
	
	population = ea.Population(Encoding, Field, NIND) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
	myAlgorithm = ea.soea_SEGA_templet(problem, population) # 实例化一个算法模板对象
	myAlgorithm.MAXGEN = maxIter # 最大进化代数
	[population, obj_trace, var_trace] = myAlgorithm.run() # 执行算法模板
	population.save() # 把最后一代种群的信息保存到文件中

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

def main():
	dim = 10000
	maxIter = 10000
	names = getModelName()
	for n in names:
		logger.info("[INFO] optimus model: {}".format(n))
		train(n, dim, maxIter)

if __name__ == '__main__':
	main()