# 2018-9-6
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第三章笔记
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

# 返回索引处的值
value = img.item(150, 120, 0) # 三个参数分别为x, y, 以及(x, y)位置的索引(此处索引为BGR的索引，因为是三元组所以， 0表示B， 1表示G， 2表示R)
print(value) # 230
# 设置索引处的值
img.itemset((150, 120, 0), 33)
print(img.item(150, 120, 0)) # 33



# # 使用切片快速复制块
pice = img[0:200, 0:200]
img[300:500,300:500] = pice
matplotlib.pyplot.imshow(img, cmap='Greys', interpolation="None")
matplotlib.pyplot.show()



# # 图像的一些属性
shape = img.shape
size = img.size
dtype = img.dtype
print(shape, size, dtype) # (500, 500, 3) 750000 uint8



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



# 滤波
k3x3 = np.array([[-1, -1, -1],
				 [-1, 8, -1],
				 [-1, -1, -1]])

k5x5 = np.array([[-1, -1, -1, -1, -1],
				 [-1, 1, 2, 1, -1],
				 [-1, 2, 4, 2, -1],
				 [-1, 1, 2, 1, -1],
				 [-1, -1, -1, -1, -1]])

k3 = ndimage.convolve(img, k3x3)
k5 = ndimage.convolve(img, k5x5)


# cv2.GaussianBlur(src,ksize,sigmaX)
# kSize:核大小,sigmaX:高斯核在x轴的标准差,如果为0会根据核的宽和高重新计
blurred = cv2.GaussianBlur(img, (11, 11), 0)

g_hpf = img - blurred
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpf", g_hpf)



# 边缘检测
# 有错误
img = cv2.imread("image/1.png")
cv2.imshow("imgd", img)
blurred = cv2.medianBlur(img, 7)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
# Laplacian 作为边缘检测会产生明显的边缘线条，灰度图像更是如此
cv2.Laplacian(gray, cv2.CV_8U, gray, ksize = 5)
normalizedInverseAlpha = (1.0 / 225) * (255 - gray) # 归一化
channels = cv2.split(img)
for c in channels:
	c[:] = c * normalizedInverseAlpha
cv2.merge(channels, 0)
cv2.imshow("img", img)



# Canny边缘检测
img = cv2.imread("image/4.jpg", 0)
print(img.shape) # (640, 640)
cv2.imwrite("testResult/4_canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("canny", cv2.imread("testResult/4_canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()



# 轮廓检测
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255 # 绘制图像

ret, thresh = cv2.threshold(img, 127, 255, 0) # 二值化

# cv2.RETR_TREE: 得到图像中轮廓的整体层次结构。若想得到最外面的轮廓，可以使用cv2.RETR_EXTERNAL
# cv2.CHAIN_APPROX_SIMPLE： 轮廓逼近方法，此为压缩
# cv2.CHAIN_APPROX_NONE： 不压缩
# 返回修改后的图片， 图像的轮廓以及它们的层次
# contours : 矩阵的四个点
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2HAIN_APPROX_SIMPLE).C
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



# 边界框, 最小矩形区域, 最小闭圆的轮廓
print(cv2.IMREAD_UNCHANGED, cv2.COLOR_BGR2GRAY, cv2.THRESH_BINARY, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE ) # -1 6 0 0 2
# img = cv2.pyrDown(cv2.imread("image/hammer.jpg", cv2.IMREAD_UNCHANGED))
# ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)
img = cv2.pyrDown(cv2.imread("image/m_5.jpg", cv2.IMREAD_UNCHANGED))
ret, thresh = cv2.threshold(img.copy() , 127, 255, cv2.THRESH_BINARY)

image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
for c in contours:
	# 绘制矩阵
  	# find bounding box coordinates
  	x,y,w,h = cv2.boundingRect(c)
  	cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

  	# find minimum area
  	rect = cv2.minAreaRect(c) # c中含有包含最小矩阵的点集, 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
  	# calculate coordinates of the minimum area rectangle
  	box = cv2.boxPoints(rect) # cv2.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
  	# normalize coordinates to integers
  	box = np.int0(box)
  	# draw contours
  	cv2.drawContours(img, [box], 0, (0,0, 255), 3)
  
  	# calculate center and radius of minimum enclosing circle
  	(x,y),radius = cv2.minEnclosingCircle(c)
  	# cast to integers
  	center = (int(x),int(y))
  	radius = int(radius)
  	# draw the circle
  	img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()



# 凸轮廓与Douglas-Peucker算法
# img = cv2.pyrDown(cv2.imread("image/hammer.jpg", cv2.IMREAD_UNCHANGED))
# ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)

img = cv2.pyrDown(cv2.imread("image/m_2.jpg", cv2.IMREAD_UNCHANGED))
cv2.imshow("orignal", img)
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
  	# cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
  	# cv2.drawContours(black, [hull], -1, (0, 0, 255), 2)

cv2.imshow("hull", black)
cv2.waitKey()
cv2.destroyAllWindows()



# 直线检测
img = cv2.imread('image/m_1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,40,50,200)
minLineLength = 20
maxLineGap = 20
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
  cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite("testResult/line.jpg", edges)

cv2.imshow("edges", edges)
cv2.imshow("lines", img)

cv2.waitKey()
cv2.destroyAllWindows()



# 圆的检测
planets = cv2.imread('image/3.jpg')
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,
                            param1=100,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0]: # circles[0, :]
    # draw the outer circle
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite("testResult/circles.jpg", planets)
cv2.imshow("HoughCirlces", planets)
cv2.waitKey()
cv2.destroyAllWindows()