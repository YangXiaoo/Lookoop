# coding:utf-8

import pickle 

def saveData(data, path):
    """保存数据"""
    fp = open(path, "wb")
    pickle.dump(data, fp)
    fp.close()

def getData(dataFilePath):
	"""读取数据"""
	data = pickle.load(open(dataFilePath, 'rb'))

	return data 