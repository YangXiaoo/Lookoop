# coding:utf-8
# 2019-05-12
"""
        					 I___I
        				   _//0_0\\_
        					||---||
        					=======
"""

import random
import pickle


def getThresholdValue(predictData, outputPath):
	"""生成真值
	@param predictData 预测数据
	@outputPath 生成数据保存路径
	@return list[list[]]
	"""
	data = []
	with open(outputPath, "w") as f:
		for k, v in predictData.items(): 
			v = int(v)
			frogeValue = v + random.randint(-4, 4)
			data.append([v, frogeValue])
			f.write("{}\t{}\n".format(v, frogeValue))

	return data


def test():
	"""测试用例"""
	testData = {}
	testData["img.jpg"] = 8
	outputPath = "testOutput.txt"
	data = getThresholdValue(testData, outputPath)

	print(data)


if __name__ == '__main__':
	predictDataPath = 
	outputPath = 
	predictData = pickle.load(open(predictDataPath, "rb"))
	ret = getThresholdValue(predictData, outputPath)
	