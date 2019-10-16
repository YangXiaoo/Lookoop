# coding:utf-8
# 2019/10/16
# 遗传算法

import matplotlib.pyplot as plt
import math
import random

class GA(object):
    def __init__(self, func, populationSize, upperLimit, chromosomeLength, maxIter=1000, pc=0.6, pm=0.01):
        self.func = func
        self.populationSize = populationSize
        self.upperLimit = upperLimit
        self.chromosomeLength = chromosomeLength
        self.maxIter = maxIter 
        self.printBase = 10
        self.pc = pc    # 杂交概率
        self.pm = pm    # 变异概率
        self.population = []

    def initPopulation(self, featureSize):
        """初始化种群"""
        self.population = [[[random.randint(0, 1) for i in range(self.chromosomeLength)] for _ in range(featureSize)] for j in range(self.populationSize)]

        # return population
    def calcObjValue(self):
        """计算值"""
        pass

    def calcFitValue(self):
        """排除异常值"""
        pass

    def findBest(self):
        """找到评分最高的值"""
        pass

    def bin2Decimal(self):
        """二进制转换为十进制"""
        pass

    def selection():
        """选择"""
        pass

    def intersect():
        """交叉"""
        pass

    def mutation():
        """变异"""
        pass

    def fit(self, feature, labels):
        """训练"""
        w, h = np.shape(feature)
        self.initPopulation(w)
        ret = []
        for it in range(self.maxIter):
            objValue = self.calcObjValue()
            fitValue = self.calcFitValue(objValue)
            bestIndividual, bestFit = self.findBest(self.population, fitValue)
            ret.append([self.bin2Decimal(bestIndividual), bestFit])

            self.selection(fitValue)    # 选择
            self.intersect()            # 交叉
            self.mutation()             # 变异

            if it % self.printBase == 0:
                print("iter: {}".format(it))
