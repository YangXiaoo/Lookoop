# 2018-9-8
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第六章笔记
# 图像检索以及基于图像描述符的搜索
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2

# 特征定义
#     有意义的图像区域，该区域有独特性或易于识别性。因此角点以及高密度区域是很好地特征。
#     大多数算法都会涉及到角点，边，斑点的识别



# 检测角点特征
# cv2.cornerHarris函数介绍：https://www.cnblogs.com/DOMLX/p/8763369.html
img = cv2.imread("image/4.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 23, 0.04)
img[dst > 0.01 * dst.max()] = [0, 0, 225]
while True:
    cv2.imshow("corner", img)
    if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()




# 使用DoG 和 SIFT进行特征提取与描述
# SIFT(Scale-Invariant Feature Transform),尺度不变特征变换
# SIFT不会检测关键点，关键点可以由DoG(Dofference of Gaussians)检测，但SIFT会通过一个特征向量来描述关键点周围区域的情况

# SURF采用快速Hessian算法检测关键点
# cv2.xfeatures2d.SURF_create(value) # value越高能识别的特征越少
img = cv2.imread("image/4.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def func(algorithm, par=None):
    algorithms = {
        "SIFT" : cv2.xfeatures2d.SIFT_create(),
        "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
        "ORB": cv2.ORB_create()
    }
    return algorithms[algorithm]

f = "ORB"
alg = func(f)
keypoints, descriptor = alg.detectAndCompute(gray, None)
img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, color=(51, 163, 236))
cv2.imshow(f, img)
cv2.waitKey()
cv2.destroyAllWindows()



# 基于ORB的特征检测和特征匹配
# a. FAST(Features from Accelerated Segment Test)
#     该算法会在像素周围绘制一个圆，该圆包括16个像素。FAST会将每个像素与加上一个阈值的圆心像素值进行比较，若有连续、比加上一个阈值的圆心的像素还亮或暗的像素，则可以认为圆心是角点。
#     FAST算法与阈值紧密相关
# b. BRIEF(Binary Robust Independent Elementary Features)
#     不是一个特征检测算法，而是一个描述符。
#     关键点描述符是图像的一种表示, 因此可以比较两个点的关键点描述符, 并找到他们的共同之处, 所以描述符可以作为一种特征匹配的方法
# c. Brute-Force
#     暴力破解匹配方法是一种描述符匹配方法，该方法会比较两个描述符，并产生匹配结果的列表。

log = cv2.imread("image/manowar_logo.png", 0)
img = cv2.imread("image/manowar_single.jpg", 0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(log, None)
kp2, des2 = orb.detectAndCompute(img, None)

# 匹配
# 遍历描述符, 确定描述符是否已经匹配, 然后计算匹配质量(距离)并排序, 这样就可以在一定置信度下显示前n个匹配, 从而得到哪两幅图像是匹配的。
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matche = bf.match(des1, des2)
matches = sorted(matche, key=lambda x:x.distance)
imgout = cv2.drawMatches(log, kp1, img, kp2, matches[:40], img, flags=2)
plt.imshow(imgout)       
plt.show()



# K-最近匹配(KNN)
# 有问题
log = cv2.imread("image/manowar_logo.png", 0)
img = cv2.imread("image/manowar_single.jpg", 0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(log, None)
kp2, des2 = orb.detectAndCompute(img, None)

# 匹配
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.knnMatch(des1, des2, k=2) # 返回k个匹配
imgout = cv2.drawMatchesKnn(log, kp1, img, kp2, matches, img, flags=2)
plt.imshow(imgout)       
plt.show()



FLANN(Fast Library for Approximate Nearest Neighbors)
可以通过数据本身来选择最合适的算法
FLANN的单应性： 为一个条件，该条件表明当两幅图像中的一幅出现畸变(perspective distortion)时, 它们还能匹配