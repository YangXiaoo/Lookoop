# 2018-9-6
# 一些函数

################################### 第三章函数 ###################################
cv2.imread(filepath,flags)
# filepath：要读入图片的完整路径
# flags：读入图片的标志 
# cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
# cv2.IMREAD_GRAYSCALE：读入灰度图片
# cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# dv2.destroyWindow(wname)
# cv2.waitKey顾名思义等待键盘输入，单位为毫秒，即等待指定的毫秒数看是否有键盘输入，若在等待时间内按下任意键则返回按键的ASCII码，程序继续运行。若没有按下任何键，超时后返回-1。参数为0表示无限等待。不调用waitKey的话，窗口会一闪而逝，看不到显示的图片。
# cv2.destroyAllWindow()销毁所有窗口
# cv2.destroyWindow(wname)销毁指定窗口


cv2.imwrite('1.png',img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
cv2.imwrite('1.png',img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
# 使用函数cv2.imwrite(file，img，num)保存一个图像。第一个参数是要保存的文件名，第二个参数是要保存的图像。可选的第三个参数，它针对特定的格式：对于JPEG，其表示的是图像的质量，用0 - 100的整数表示，默认95;对于png ,第三个参数表示的是压缩级别。默认为3.
# 注意:
# cv2.IMWRITE_JPEG_QUALITY类型为 long ,必须转换成 int
# cv2.IMWRITE_PNG_COMPRESSION, 从0到9 压缩级别越高图像越小。


# 彩色图像转为灰度图像
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
# 灰度图像转为彩色图像
img3 = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# cv2.COLOR_X2Y，其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS



# https://www.kancloud.cn/aollo/aolloopencv/271603 
cv2.Canny(img, minVal, maxval, Ssize, Bool)
#第一个参数是输入图像，第二和第三个分别是minVal和maxVal。第三个参数设置用来计算图像梯度的Sobel卷积核的大小，默认值为3。最后一个参数是L2gradient，它可以用来设定求梯度大小的方程
# 当图像的灰度梯度高于maxVal时被认为是真的边界，那些低于minVal的边界会被抛弃。如果介于两者之间的话，就要看这个点是否与某个被确定为真正边界点相连，如果是，就认为它也是边界点，如果不是就抛弃。



# threshold：固定阈值二值化
# https://docs.opencv.org/3.2.0/d7/d4d/tutorial_py_thresholding.html
ret, dst = cv2.threshold(src, thresh, maxval, type)
# src： 输入图，只能输入单通道图像，通常来说为灰度图
# dst： 输出图
# thresh： 阈值
# maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
# type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV



# 轮廓查找
image, contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_TREE: 得到图像中轮廓的整体层次结构。若想得到最外面的轮廓，可以使用cv2.RETR_EXTERNAL
# cv2.CHAIN_APPROX_SIMPLE： 轮廓逼近方法，此为压缩
# cv2.CHAIN_APPROX_NONE： 不压缩
# 返回修改后的图片， 图像的轮廓以及它们的层次
# contours : 矩阵的四个点


# 绘图
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
# drawContours() 它的第一个参数是原始图像，第二个参数是轮廓，一个python列表，第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为-1时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度。



# 绘制矩形
cv2.boundingRect(img)
# img是一个二值图，也就是它的参数；返回四个值，分别是x，y，w，h；
# x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
# 第一个参数：img是原图
# 第二个参数：（x，y）是矩阵的左上点坐标
# 第三个参数：（x+w，y+h）是矩阵的右下点坐标
# 第四个参数：（0,255,0）是画线对应的rgb颜色
# 第五个参数：2是所画的线的宽度



# 绘制最小矩阵, 下面配合使用
# find minimum area
rect = cv2.minAreaRect(c) # c中含有包含最小矩阵的点集, 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
# calculate coordinates of the minimum area rectangle
box = cv2.boxPoints(rect) # cv2.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
# normalize coordinates to integers
box = np.int0(box)



# 凸形
# 
perimeter = cv2.arcLength(cnt,True)
# 将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定，使用的Douglas-Peucker算法.
# 假设我们要在一幅图像中查找一个矩形，但是由于图像的种种原因我们不能得到一个完美的矩形，而是一个“坏形状”，现在就可以使用这个函数来近似这个形状，第二个参数是epsilon，它是从原始轮廓到近似轮廓的最大距离，它是一个准确度参数。
# 轮廓近似
cv2.approxPolyDP(cnt,epsilon,True)
# 第一个参数为轮廓
# 第二个参数为 r 值， 表示原轮廓与近似多边形的最大差值(值越小近似多边形与原轮廓越接近)
# 第三个参数为布尔值标记， 表示这个多边形是否合并
# 也被称为弧长。可以使用函数cv2.arcLength()计算得到。这个函数的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。
epsilon=0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
hull = cv2.convexHull(cnt,hull,clockwise,returnPoints)
# 参数：
# cnt我们要传入的轮廓
# hull输出，通常不需要
# clockwise方向标志，如果设置为True，输出的凸包是顺时针方向的，否则为逆时针方向。
# returnPoints默认值为True。它会返回凸包上点的坐标，如果设置为False，就会返回与凸包点对应的轮廓上的点。
# 但是如果你想获得凸性缺陷，需要把returnPoints设置为False。以上面矩形为例，首先我们找到他的轮廓从cnt。现在把returnPoints设置为True查找凸包，得到的就是矩形的四个角点。把returnPoints设置为False，得到的是轮廓点的索引



# 直线检测
cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength,maxLineGap)
# edges: 需要处理的图像， 一般已经由Candy检测边缘了
# 几何表示的rho和theta,一般分别取1和np.pi/180
# 阈值，低于阈值的直线会被忽略
# minLineLength,maxLineGap：最小直线长度(更短的会被忽略)最大间隙， 一条线段的间隙长度大于这个值会被忽视为两条分开线段



# 圆的检测
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,
                             param1=100,param2=30,minRadius=0,maxRadius=0)
# 与直线检测参数类似





################################### 第四章函数 ###################################
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# img 输入图像
# mask 蒙板图像，确定前景区域，背景区域，不确定区域，可以设置为cv2.GC_BGD,cv2.GC_FGD,cv2.GC_PR_BGD,cv2.GC_PR_FGD，也可以输入0,1,2,3
# rect 前景的矩形，格式为（x,y,w,h），分别为左上角坐标和宽度，高度
# bdgModel, fgdModel 算法内部是用的数组，只需要创建两个大小为(1,65）np.float64的数组。
# iterCount 迭代次数
# mode cv2.GC_INIT_WITH_RECT 或 cv2.GC_INIT_WITH_MASK，使用矩阵模式还是蒙板模式。



# 检测角点
dst = cv2.cornerHarris(gray, 2, 23, 0.04)
# 输入图像必须是 float32
# 第二个参数越小，标记角点的记号越小
# 第三个参数限制了Sobel算子的中孔(aperture), 该参数定义了角点检测的敏感度，其值必须是介于3和31之间的奇数
# 最后一个参数在 0.04 到 0.05 之间