# 2018-9-6
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
import numpy as np
import matplotlib.pyplot
import scipy.special
import os
import cv2
from scipy import ndimage
# import cv # 已经被遗弃


# 生成随机数组
# randomByteArray = bytearray(os.urandom(1080 * 1920 * 3))
# flatArray = np.array(randomByteArray)
# img = flatArray.reshape(1080 , 1920, 3)
# cv2.imwrite('testResult/randomByteImage.png', img)
# matplotlib.pyplot.imshow(img, cmap='Greys', interpolation="None")


# 使用numpy.array访问图像数据
img = cv2.imread("image/1.png", 0)
# print(img.shape) # (500, 500, 3)

# # 返回索引处的值
# value = img.item(150, 120, 0) # 三个参数分别为x, y, 以及(x, y)位置的索引(此处索引为BGR的索引，因为是三元组所以， 0表示B， 1表示G， 2表示R)
# print(value) # 230
# # 设置索引处的值
# img.itemset((150, 120, 0), 33)
# print(img.item(150, 120, 0)) # 33

# # 使用切片快速复制块
# pice = img[0:200, 0:200]
# img[300:500,300:500] = pice
# matplotlib.pyplot.imshow(img, cmap='Greys', interpolation="None")
# matplotlib.pyplot.show()


# # 图像的一些属性
# shape = img.shape
# size = img.size
# dtype = img.dtype
# print(shape, size, dtype) # (500, 500, 3) 750000 uint8


# 计算机中常用的三种色彩空间： 灰度， BGR, HSV(Hue, Saturation, Value)
# 	a. 灰度
# 		通过去除彩色信息来将其信息转换成灰阶，灰度色彩空间对中间处理特别有效，比如人脸检测
# 	b. BGR
# 		即蓝，绿， 红色
# 	c. HSV(Hue, Saturation, Value)

# 傅里叶变换
# a. 高通滤波(HPF, High Pass Filter)
# 	高通滤波是检测图像的某个区域，然后根据像素与周围像素的亮度差值来提升该像素的亮度。 计算完中央像素与周围邻近像素的亮度差值之和后，如果亮度变化很大，中央像素的亮度会增加
# b. 低通滤波(LPF, Low Pass  Filter)
# 	在像素与周围像素的亮度的差值小于一个特定的值时，平滑该像素的亮度，主要用于去噪和模糊化



# k3x3 = np.array([[-1, -1, -1],
# 				 [-1, 8, -1],
# 				 [-1, -1, -1]])

# k5x5 = np.array([[-1, -1, -1, -1, -1],
# 				 [-1, 1, 2, 1, -1],
# 				 [-1, 2, 4, 2, -1],
# 				 [-1, 1, 2, 1, -1],
# 				 [-1, -1, -1, -1, -1]])

# k3 = ndimage.convolve(img, k3x3)
# k5 = ndimage.convolve(img, k5x5)


# # cv2.GaussianBlur(src,ksize,sigmaX)
# # kSize:核大小,sigmaX:高斯核在x轴的标准差,如果为0会根据核的宽和高重新计
# blurred = cv2.GaussianBlur(img, (11, 11), 0)

# g_hpf = img - blurred
# cv2.imshow("3x3", k3)
# cv2.imshow("5x5", k5)
# cv2.imshow("g_hpf", g_hpf)

# 边缘检测
# 有错误
# img = cv2.imread("image/1.png")
# cv2.imshow("imgd", img)
# blurred = cv2.medianBlur(img, 7)
# gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
# # Laplacian 作为边缘检测会产生明显的边缘线条，灰度图像更是如此
# cv2.Laplacian(gray, cv2.CV_8U, gray, ksize = 5)
# normalizedInverseAlpha = (1.0 / 225) * (255 - gray) # 归一化
# channels = cv2.split(img)
# for c in channels:
# 	c[:] = c * normalizedInverseAlpha
# cv2.merge(channels, 0)
# cv2.imshow("img", img)


# Canny边缘检测
# img = cv2.imread("image/4.jpg", 0)
# print(img.shape) # (640, 640)
# cv2.imwrite("testResult/4_canny.jpg", cv2.Canny(img, 200, 300))
# cv2.imshow("canny", cv2.imread("testResult/4_canny.jpg"))
# cv2.waitKey()
# cv2.destroyAllWindows()

# 轮廓检测
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255 # 绘制图像

ret, thresh = cv2.threshold(img, 127, 255, 0) # 二值化

# cv2.RETR_TREE: 得到图像中轮廓的整体层次结构。若想得到最外面的轮廓，可以使用cv2.RETR_EXTERNAL
# cv2.CHAIN_APPROX_SIMPLE： 轮廓逼近方法，此为压缩
# cv2.CHAIN_APPROX_NONE： 不压缩
# 返回修改后的图片， 图像的轮廓以及它们的层次
# contours : 矩阵的四个点
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("changed", image)
print(contours)
# contours结果
"""
[array([[[ 50,  50]],

       [[ 50, 149]],

       [[149, 149]],

       [[149,  50]]], dtype=int32)]
"""
print(hierarchy) # [[[-1 -1 -1 -1]]]
# 将灰度转换为彩色
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# drawContours() 它的第一个参数是原始图像，第二个参数是轮廓，一个python列表，第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为-1时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度。
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
