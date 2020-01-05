# coding:utf-8
# 2019-12-2
"""
- 将原始尺寸添加到数据中
- 保存仿真结果替代原始随机测试数据
"""
import sys
sys.path.append('../../')

import numpy as np
from util import io

oldDataFilePath = "../../data/samples-data_backup.data"
dataFilePath = "../../data/samples-data.data"
labelsFilePath = "../../data/samples-data-labels.data"
curveFitModelSavingPath = "../../data/quadraticRegression.model"

# X = io.getData(oldDataFilePath)

def getLables():
	"""仿真阻力值"""
	y = [
			[39435.643],	# FFD0 原始尺寸
			[38071.185],	# FFD2 对应电脑中的目录名
			[39200.969],	# FFD3
			[39193.068],	# FFD4
			[37650.16],		# FFD5
			[39066.458],	# FFD6
			[39035.507],	# FFD7
			[38455.18],		# FFD8
			[38374.768],	# FFD9
			[37974.92],		# FFD10
			[39167.307],	# FFD11
			[38902.142],	# FFD12
			[39334.767],	# FFD13
			[37980.654],	# FFD14
			[38298.512],	# FFD15
			[39840.227],	# FFD16
			[38051.073],	# FFD17
			[38501.634],	# FFD18
			[38330.912],	# FFD19
			[39060.899],	# FFD20
			[39617.136],	# FFD21
			[38163.894],	# FFD22
			[39591.876],	# FFD23
			[37145.634],	# FFD24
			[37913.137],	# FFD25
			[38977.855],	# FFD26
			[38604.855],	# FFD27
			[38008.155],	# FFD28
			[39062.525],	# FFD29
			[38227.168],	# FFD30
			[38967.278],	# FFD31
		]

	return np.array(y) 

def dataConcate():
	"""拼接数据"""
	addData = np.array([[0, 0, 0, 0, 0]])
	ret = np.concatenate([addData,X], axis=0)

	return ret 

def main():
	# 处理变形控制点
	# newData = dataConcate()
	# print(newData)
	# io.saveData(newData, dataFilePath)

	# 仿真结果保存
	y = getLables()
	io.saveData(y, labelsFilePath)

if __name__ == '__main__':
	main()