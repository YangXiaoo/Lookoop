# 2018-9-10
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892

# 第七章笔记
# 目标检测与识别

import numpy as np
from matplotlib import pyplot as plt
import os
import cv2

目标检测与识别技术:
	a. 梯度直方图(HOG, Histogram of Oritened Gradient)
	b. 图像金字塔(image pyramid)
	c. 滑动窗口(sliding window)

HOG描述符
	HOG是一个特征描述符, 将图像划分为多个部分，并计算各个部分的梯度。
	图像被分为小单元，每个小单元为16x16的像素块，每个单元都包括视觉表示，该视觉表示按八个方向所计算的颜色梯度，每个单元的八个值就是直方图。
	a. 尺度问题
	b. 位置问题
	c. 非最大(或非极大)抑制
	d. 支持向量机


# 人检测关键代码
# 人检测默认器
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# 产生一个与矩形相关的数组
found, w = hog.detectMultiScale(img, winStride=(8,8),scale=1.05)



# 构建分类器需要SVM与词袋
# 词袋(BOW, Bag-of-Word)
a. 在文档中统计次数然后重新构建文档。可用于垃圾过滤
b. 计算机视觉中的BOW
	实现步骤：
		1. 取一个数据样本
		2. 对数据集中的每幅图像提取描述符(SIFT, SURF)
		3. 将每个描述符都添加到BOW训练器中
		4. 将描述符聚类到k簇中(从可视化角度来看，K-means就是这个簇中点的几何中心)