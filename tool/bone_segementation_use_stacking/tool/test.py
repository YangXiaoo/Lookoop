# coding:utf-8
# 2019-5-9
# 根据切边信息裁剪图片
import os
import pickle
import cv2
import datetime
import numpy as np

import api


data = pickle.load(open(r"C:\Study\test\bone\ret_DecisionTree\DecisionTree_predictValueRecord.dat", "rb"))
print(data)

