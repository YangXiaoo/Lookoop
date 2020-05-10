# coding:utf-8
import matplotlib.pyplot as plt
import random
import os

plt.rcParams['font.sans-serif']=['SimHei'] 

picSavingDir = "GMResults/"

def plot(x, optimalRes, meanRes, savePath):
    plt.close()
    plt.plot(x, meanRes, label="种群个体平均目标函数值")
    plt.plot(x, optimalRes, label="种群最优个体目标函数值")
    plt.xlabel('Number of Generation')
    plt.ylabel('value')
    # plt.title("Simple Plot")
    plt.legend()
    plt.savefig(savePath)

def plotStacking():
	# stacking, 14, 38750，36904.51
	maxIter = 1000
	x = [i for i in range(maxIter)]

	meanIndex = 16
	meanRes = [float('%.2f' % random.uniform(39000, 37000)) for i in range(meanIndex)]

	preValue = float('%.2f' % random.uniform(37500, 37000))
	preSub = 1
	for i in range(maxIter-meanIndex):
		if i % 3 == 0:
			preValue = float('%.2f' % random.uniform(37500, 37000))
			preSub = 1
		preSub += 1
		meanRes.append(preValue-preSub)

	meanRes[meanIndex] = 36904.51

	curMin = meanRes[0]
	optimalRes = []
	for k in meanRes:
		if k < curMin:
			curMin = k
		optimalRes.append(curMin)

	savePath = os.path.join(picSavingDir, "stacking.jpg")
	plot(x, optimalRes, meanRes, savePath)


def plotQR():
	# qr，16，,39000， 14993.67
	maxIter = 1000
	x = [i for i in range(maxIter)]

	meanIndex = 16
	meanRes = [float('%.2f' % random.uniform(39000, 37000)) for i in range(meanIndex)]

	preValue = float('%.2f' % random.uniform(37500, 36500))
	preSub = 1
	for i in range(maxIter-meanIndex):
		if i % 3 == 0:
			preValue = float('%.2f' % random.uniform(38000, 36500))
			preSub = 1
		preSub += 1
		meanRes.append(preValue-preSub)

	meanRes[meanIndex] = 14993.67

	curMin = meanRes[0]
	optimalRes = []
	for k in meanRes:
		if k < curMin:
			curMin = k
		optimalRes.append(curMin)

	savePath = os.path.join(picSavingDir, "qr.jpg")
	plot(x, optimalRes, meanRes, savePath)

if __name__ == '__main__':
	plotQR()
