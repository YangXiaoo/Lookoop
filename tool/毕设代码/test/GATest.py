# coding:utf-8
# 2019/10/17
# GA-test

import sys
sys.path.append('../')

import numpy as np
import math

from algorithms.optimus import GA
from util import io 

def test():
	modelName = "Linear"
	modelPath = "../data/{}.model".format(modelName)
	model = io.getData(modelPath)
	# __init__(self, func, featureSize, populationSize, upperLimit, lowerLimit, chromosomeLength, maxIter=1000, pc=0.6, pm=0.01, threshedValue=10)
	ga = GA.GA(model, 18, 500, 100, -100, 10, 5000)
	ga.fit()

class Formulation(GA.FormulationHandler):
	def __init__(self):
		super(Formulation, self).__init__()

	def predict(self, feature):
		
		curValue = [10 * math.sin(5 * feature) + 7 * math.cos(4 * feature)]
		# assert False, "feature: {}, value: {}".format(feature, curValue)

		return curValue

def testSingleVar():
	func = Formulation()
	ga = GA.GA(func, 1, 500, 10, 0, 8, maxIter=1000, pc=0.6, pm=0.01, threshedValue=1)
	ga.fit()

if __name__ == '__main__':
	testSingleVar()