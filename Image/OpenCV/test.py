# 2018-8-19
# test
# C:\Study\github\Lookoop\Image\Python神经网络\test.py
import os
import cv2
import numpy as np
import sys
def create(dirpath):
	file = []
	for root, dirs, files in os.walk(dirpath, topdown=False):
		for f in files:
			path = os.path.join(root, f)
			file.append(path)
			t = os.path.splitext(path)
			print(t)

create("C:\\Study\\github\\Lookoop\\Image")