# coding:UTF-8
# 2018-11-16
# api
import os 
import cv2
import math
import numpy as np

__suffix = ["png", "jpg"]

def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def getTrainingData(dir_path):
	"""
	加载训练数据
	"""
	files = getFiles(dir_path)
	data, labels = [], []
	for f in files:
		img = cv2.imread(f, 0)
		m, n = img.shape
		img = np.array(img)
		# tmp_data = []
		# for i in range(m):
		# 	for j in range(n):
		# 		tmp_data.append(img[i, j])
		year = float(os.path.basename(f).split("-")[1])
		# print(year)
		label_tmp = np.zeros(18) + 0.01
		label_tmp[int(year)] = 0.99

		data.append(img)
		labels.append(label_tmp)

	return np.array(data), labels

if __name__ == '__main__':
	data, labels = getTrainingData("C:\\Study\\test\\histogram_no_norm")
	print(data[1], labels[0])