# coding:utf-8
# 2019/10/16
# 遗传算法

import matplotlib.pyplot as plt
import math
import random
import numpy as np

class FormulationHandler(object):
    def predict(self, feature):
        """预测，并返回值"""
        pass

class GAHandler(object):
    def __init__(self, func, featureSize, populationSize, upperLimit, lowerLimit, chromosomeLength, maxIter, pc, pm, isMax, threshedValue):
        self.func = func
        self.featureSize = featureSize  # 特征长度
        self.populationSize = populationSize    # 种群大小
        self.upperLimit = upperLimit    # 自变量的上界
        self.lowerLimit = lowerLimit    # 自变量的下界
        self.threshedValue = 10         # 加速求解的阈值
        self.chromosomeLength = chromosomeLength
        self.maxIter = maxIter          # 最大迭代数
        self.printBase = 1              # 打印间隔
        self.pc = pc    # 杂交概率
        self.pm = pm    # 变异概率
        self.population = []
        self.isMax = isMax   # 是否求极大值

    def initPopulation(self):
        """初始化种群"""
        print("[INFO] initialize population")
        self.population = [[[random.randint(0, 1) for _ in range(self.chromosomeLength)] for _ in range(self.featureSize)] for _ in range(self.populationSize)]
        # print("[DEBUG] population : {}".format(self.population))
        # assert False, "debug"

    def decodeChromosome(self):
        """解编码并计算"""
        # print("[INFO] decode chromosome")
        ret = []
        for _, r in enumerate(self.population):
            tmpRet = []
            for k, c in enumerate(r):
                tmpValue = 0
                for i, coff in enumerate(c):
                    tmpValue += coff * (2**i)
                tmpValue = self.lowerLimit[k] + tmpValue * (self.upperLimit[k] - self.lowerLimit[k]) / (2**self.chromosomeLength - 1)   # https://blog.csdn.net/robert_chen1988/article/details/79159244
                tmpRet.append(tmpValue)
            ret.append(tmpRet)
        return ret

    def calcObjValue(self):
        """计算值"""
        # print("[INFO] calculate object value")
        objValue = []
        X = self.decodeChromosome()
        for r in X:
            curValue = self.func.predict(np.array([r]))
            # print("[DEBUG] cur predict Value : {}".format(curValue))
            objValue.append(curValue[0])

        return objValue

    def calcFitValue(self, objValue):
        """排除计算结果中的异常值"""
        # print("[INFO] calculate fit object value")
        fitValue = []
        for v in objValue:
            curValue = v
            # 加速收敛
            if v < 0:
                curValue = 0
            # if v > self.upperLimit:
            #     curValue = self.upperLimit
            fitValue.append(curValue)

        return fitValue

    def findBest(self, fitValue):
        """找到最优解"""
        # print("[INFO] find best score value")
        bestIndividual = self.population[0]
        bestFit = fitValue[0]
        for i in range(1, len(self.population)):
            if fitValue[i] <= 0:    # 保证 bestFit > 0
                continue
            if bestFit <= 0:
                bestIndividual = self.population[i]
                bestFit = fitValue[i]
                continue
            if self.isMax:
                if fitValue[i] >= bestFit:
                    bestFit = fitValue[i]
                    bestIndividual = self.population[i]
            else:
                if fitValue[i] <= bestFit:
                    bestFit = fitValue[i]
                    bestIndividual = self.population[i]
        if bestFit <= 0:
            print("[WARNING] cur iter cant find best results.")
            bestFit = float("inf")
        return bestIndividual, bestFit

    def bin2Decimal(self, bestIndividual):
        """二进制转换为十进制"""
        # print("[INFO] bin2Decimal")
        decimal = [0 for _ in bestIndividual]
        for i, r in enumerate(bestIndividual):
            curValue = 0
            for j in range(len(r)):
                curValue += r[j] * 2 ** j
            curValue = self.lowerLimit[i] + curValue * (self.upperLimit[i] - self.lowerLimit[i]) / (2**self.chromosomeLength - 1)
            decimal[i] = curValue

        return decimal

    def computeSum(self, pFitValue):
        """计算累计概率"""
        for i in range(1, len(pFitValue)):
            pFitValue[i] = pFitValue[i] + pFitValue[i-1]

    def selection(self, fitValue):
        """轮赌法选择"""
        pFitValue = []  # 概率
        totalFitValue = sum(fitValue)
        if totalFitValue == 0:
            assert False, "ZeroDivisionError: division by zero"
            
        for i in range(len(fitValue)):
            pFitValue.append(fitValue[i] / totalFitValue)
        self.computeSum(pFitValue)  # 计算累计概率
        popRowLen, popColLen = len(self.population), len(self.population[0])
        dial = [random.random() for i in range(popRowLen)
            ]  # 应该不需要排序
        fitIndex = 0
        newIndex = 0
        newPopulation = self.population[:]
        while newIndex < popRowLen:
            if (dial[newIndex] < pFitValue[fitIndex]):  # 如果这个值的概率大于随机出来的概率，那就选择这个
                newPopulation[newIndex] = self.population[fitIndex]
                newIndex += 1
            else:
                fitIndex += 1
        self.population = newPopulation[:]

    def intersect(self):
        """交叉"""
        # print("[INFO] intersect")
        # assert False, "population[0]: {}".format(self.population[0])
        for i in range(len(self.population) - 1):
            for j in range(len(self.population[0])):
                curPro = random.random()
                if curPro < self.pc:
                    intersectPoint = random.randint(0, self.chromosomeLength-1)    # 选取杂交点
                    self.population[i][j][intersectPoint:], self.population[i + 1][j][intersectPoint:] = self.population[i + 1][j][intersectPoint:], self.population[i][j][intersectPoint:] # 替换

    def mutation(self):
        """变异"""
        # print("[INFO] mutation")
        for r in range(len(self.population)):
            for c in range(len(self.population[0])):
                # for i in range(len(self.population[r][c])):
                curPro = random.random()
                if curPro < self.pm:
                    mPoint = random.randint(0, self.chromosomeLength-1)
                    self.population[r][c][mPoint] = [0, 1][self.population[r][c][mPoint] == 0]

    def fit(self):
        """训练"""
        print("[INFO] starting fit")
        self.initPopulation()
        ret = []
        bestIter = 0
        for it in range(self.maxIter):
            objValue = self.calcObjValue()
            fitValue = self.calcFitValue(objValue)
            # print("[DEBUG] iter: {}, fitvalue: {}".format(it, fitValue))
            bestIndividual, bestFit = self.findBest(fitValue)
            if len(bestIndividual) == 0:
                assert False, "best individual is empty"

            curValue = [self.bin2Decimal(bestIndividual), bestFit]
            if len(ret) == 0:
                ret = curValue
            else:
                if self.isMax:
                    if ret[-1] <= curValue[-1]:
                        ret = curValue
                        bestIter = it
                else:
                    if ret[-1] >= curValue[-1]:
                        ret = curValue
                        bestIter = it
            # print("[DEBUG] iter: {}, bestIndividual: {}, bestFit: {}".format(it, bestIndividual, bestFit))
            # ret.append([self.bin2Decimal(bestIndividual), bestFit])
            # print("[DEBUG] iter: {}, ret: {}".format(it, ret))

            self.selection(fitValue)    # 选择
            self.intersect()            # 交叉
            self.mutation()             # 变异

            if (it % self.printBase == 0) or (it == (self.maxIter - 1)):
                print("iter: {}, best iter: {}, cur best fit : {}".format(it, bestIter, ret))
                # print("iter: {}, optimus value: {}".format(it, bestFit))

class GA(GAHandler):
    """极大值"""
    def __init__(self, func, featureSize, populationSize, upperLimit, lowerLimit, chromosomeLength, maxIter=1000, pc=0.6, pm=0.01, isMax=True, threshedValue=10):
        super(GA, self).__init__(func, featureSize, populationSize, upperLimit, lowerLimit, chromosomeLength, maxIter, pc, pm, isMax, threshedValue)

