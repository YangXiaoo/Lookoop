# coding:utf-8
# 2019/10/17
# GA-test

import sys
sys.path.append('../')

import numpy as np
import math

from algorithms.optimus import GA
from util import io 

def testMultiVar():
	modelName = "ElasticNet"
	modelPath = "../data/{}.model".format(modelName)
	func = io.getData(modelPath)
	featureSize = 18
	populationSize = 500
	upperLimit = [100 for _ in range(featureSize)]
	lowerLimit = [-100 for _ in range(featureSize)]
	chromosomeLength = 10
	maxIter = 1000
	pc = 0.6
	pm = 0.01
	threshedValue = 10
	isMax = False
	ga = GA.GA(func, featureSize, populationSize, upperLimit, lowerLimit, chromosomeLength, maxIter=maxIter, pc=pc, pm=pm, isMax=isMax, threshedValue=threshedValue)
	ga.fit()


class Formulation(GA.FormulationHandler):
	"""重写表达式"""
	def __init__(self):
		super(Formulation, self).__init__()

	def predict(self, feature):
		"""重写"""
		curValue = [10 * math.sin(5 * feature) + 7 * math.cos(4 * feature)]

		return curValue

def testSingleVar():
	"""单变量表达式求最优值"""
	func = Formulation()
	featureSize = 1
	populationSize = 500
	upperLimit = [10]
	lowerLimit = [0]
	chromosomeLength = 10
	maxIter = 1000
	pc = 0.6
	pm = 0.01
	threshedValue = 10
	isMax = True
	ga = GA.GA(func, featureSize, populationSize, upperLimit, lowerLimit, chromosomeLength, maxIter=maxIter, pc=pc, pm=pm, isMax=isMax, threshedValue=threshedValue)
	ga.fit()

if __name__ == '__main__':
	testSingleVar()