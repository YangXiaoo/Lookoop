# 2018-9-7
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第四章笔记
import numpy as np
from matplotlib import pyplot as plt
import scipy.special
import os
import cv2
from scipy import ndimage



# GrabCut 进行前景检测
url = "http://lxa.kim/download/?download=20180911-211843-8890/m_2.jpg"
ff = urllib.request.urlopen(url)
data = ff.read()
with open("m_2.jpg", "wb") as f:
	f.write(data)
img = cv2.imread("m_2.jpg")
print(img.shape) # (500, 500, 3)
mask = np.zeros(img.shape[:2],np.uint8) # 掩膜

# 前景和背景
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
print(bgdModel)  
"""
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
"""
rect = (60,90,970,1360)

# 5为迭代次数
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

# 满足条件输出0， 不满足则为1,
# astype('uint8') 转换格式
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis] # np.newaxis = None

plt.subplot(121), plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread(name), cv2.COLOR_BGR2RGB))
plt.title("original"), plt.xticks([]), plt.yticks([])
plt.show()



# #################################################################################################
# # 分水岭算法
# img = cv2.imread('image/m_4.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 已经是灰度图
# ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) # 将图像分为两个部分，黑色和白色

# # cv2.imshow("thresh", thresh)

# # 去除噪音
# kernel = np.zeros((3,3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)


# # 通过 morphologyEx()变换之后对图像进行膨胀操作, 可以得到大部分都是背景的区域
# sure_bg = cv2.dilate(opening,kernel,iterations=3)
# # cv2.imshow("s", sure_bg)

# # 确定前景区域，使用阈值来确定哪些是前景区域
# dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
# ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)

# # 前景背景有重合区域，相减
# sure_fg = np.uint8(sure_fg)
# unknown = cv2.subtract(sure_bg,sure_fg)

# # Marker labelling
# ret, markers = cv2.connectedComponents(sure_fg)

# # 将背景区域加1， unknown区域设置为0
# markers = markers+1
# markers[unknown==255] = 0

# # 让水漫起来并把栅栏绘制成红色
# markers = cv2.watershed(img,markers)
# img[markers == -1] = [255,0,0]

# plt.imshow(img)
# plt.show()

# cv2.waitKey()
# cv2.destroyAllWindows()