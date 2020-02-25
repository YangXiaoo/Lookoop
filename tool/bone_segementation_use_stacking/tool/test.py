# coding:utf-8
# 2019-5-9
# 根据切边信息裁剪图片
import os
import pickle
import cv2
import datetime
import numpy as np


testPic = r"C:\Study\test\bone\crop-test\fm-1-2.4_new.png"
img = cv2.imread(testPic)
print(img.shape)	# w,h

