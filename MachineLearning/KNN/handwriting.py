# coding:UTF-8
# 2018-10-29
# KNN识别手写数字
# 机器学习实战

from os import listdir
import numpy as np 
import KNN

def loadImage(file_name):
	"""
	从文本中加载图像数据
	图像尺寸：32x32
	"""
	img = np.zeros((1, 1024))
	f = open(file_name, "r")
	for i in range(32):
		line = f.readline()
		for j in range(32):
			img[0, 32 * i + j] = int(line[j])
	f.close()
	return img

def handWritingClassTest(training_file, test_file):
	"""
	使用KNN识别手写数字
	"""
	# 读取训练文件
	print("loading data...")
	training_list = listdir(training_file)
	m = len(training_list)
	train_labels = []
	train_data = np.zeros((m, 1024))
	for i in range(m):
		file = training_list[i]
		file_name = file.split('.')[0]
		number = int(file_name.split('_')[0]) # 数字
		train_labels.append(number)
		train_data[i, :] = loadImage("%s/%s" % (training_file, file))
	train_data = np.mat(train_data)
	# train_labels = np.mat(train_labels).T
	# print(np.shape(train_data), np.shape(train_labels))
	print("testing...")
	# 识别
	test_list = listdir(test_file)
	m_test = len(test_list)
	error = 0.0
	for i in range(m_test):
		file = test_list[i]
		file_name = file.split('.')[0]
		number= int(file_name.split('_')[0])
		test_data = loadImage("%s/%s" % (test_file, file))
		prediction = KNN.classify(test_data, train_data, train_labels, 3)
		print("test: %d, prediction: %d" % (number, prediction))
		if prediction != number:
			error += 1
	print("correct rate: %f" % (1 - error / m_test))


if __name__ == '__main__':
	training_file = 'trainingDigits'
	test_file = 'testDigits'
	handWritingClassTest(training_file, test_file)



