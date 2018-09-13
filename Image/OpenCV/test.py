# 2018-9-6
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第五章笔记
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from skimage import transform
import math

# # 图像裁剪
# img = cv2.imread("image/m_5.jpg", 0) # 0表示以对读入图像灰度处理
# w, h= img.shape
# print(img.shape)
# s = min(w, h)  # 取最小值裁剪成sxs大小
# pre = dummy = img
# dummy = transform.resize(dummy, (500, 500))
# plt.subplot(121)
# plt.imshow(dummy)
# img = img[:s, :s]
# print(img)
# img=transform.resize(img, (500, 500))
# cv2.imwrite("xx.jpg", np.asarray(img, np.uint8))
# plt.subplot(122)
# plt.imshow(img)
# plt.show()


# n = [[1,2,3,5,65,7], [55,233,44,66,8798,2], [55444,233,44,66,8798,2]]
# p = np.asarray(n)
# t = [0, 2,2]
# r = p[t[:2]]
# print(math.abs(-1))

# print(os.path.dirname(__file__))
# print(np.array((2.2,1), np.float32))


img = cv2.pyrDown(cv2.imread("image/m_L.png", 0))
cv2.imshow("orignal", img)
w, h= img.shape
# print(img.shape)
s = min(w, h)  # 取最小值裁剪成sxs大小
pre = dummy = img

dummy = cv2.resize(dummy, (200, 200), interpolation=cv2.INTER_LINEAR)
img = img[:s, :s]


ret, thresh = cv2.threshold(img.copy() , 127, 255, cv2.THRESH_BINARY)

black = cv2.cvtColor(np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8), cv2.COLOR_GRAY2BGR)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
  	epsilon = 0.01 * cv2.arcLength(cnt,True) # 获得轮廓周长
  	approx = cv2.approxPolyDP(cnt,epsilon,True)
  	# cv2.approxPolyDP(cnt,epsilon,True)
	# 第一个参数为轮廓
	# 第二个参数为 e 值， 表示原轮廓与近似多边形的最大差值(值越小近似多边形与原轮廓越接近)
	# 第三个参数为布尔值标记， 表示这个多边形是否合并
	# 也被称为弧长。可以使用函数cv2.arcLength()计算得到。这个函数的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。
  	hull = cv2.convexHull(cnt) # 凸包
	# hull = cv2.convexHull(cnt,hull,clockwise,returnPoints)
	# 参数：
	# cnt我们要传入的轮廓
	# hull输出，通常不需要
	# clockwise方向标志，如果设置为True，输出的凸包是顺时针方向的，否则为逆时针方向。
	# returnPoints默认值为True。它会返回凸包上点的坐标，如果设置为False，就会返回与凸包点对应的轮廓上的点。
	# 但是如果你想获得凸性缺陷，需要把returnPoints设置为False。以上面矩形为例，首先我们找到他的轮廓从cnt。现在把returnPoints设置为True查找凸包，得到的就是矩形的四个角点。把returnPoints设置为False，得到的是轮廓点的索引
  	cv2.drawContours(black, [cnt], -1, (0, 255, 0), 2)
  	cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
  	cv2.drawContours(black, [hull], -1, (0, 0, 255), 2)

cv2.imshow("hull", black)
cv2.waitKey()
cv2.destroyAllWindows()