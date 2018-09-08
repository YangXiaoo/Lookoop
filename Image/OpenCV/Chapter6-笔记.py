# 2018-9-8
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第六章笔记
# 图像检索以及基于图像描述符的搜索
import numpy as np
import matplotlib.pyplot
import scipy.special
import os
import cv2
from scipy import ndimage

# # 特征定义
# #     有意义的图像区域，该区域有独特性或易于识别性。因此角点以及高密度区域是很好地特征。
# #     大多数算法都会涉及到角点，边，斑点的识别



# # 检测角点特征
# # cv2.cornerHarris函数介绍：https://www.cnblogs.com/DOMLX/p/8763369.html
# img = cv2.imread("image/4.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray, 2, 23, 0.04)
# img[dst > 0.01 * dst.max()] = [0, 0, 225]
# while True:
#     cv2.imshow("corner", img)
#     if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
#         break
# cv2.destroyAllWindows()




# # 使用DoG 和 SIFT进行特征提取与描述
# # SIFT(Scale-Invariant Feature Transform),尺度不变特征变换
# # SIFT不会检测关键点，关键点可以由DoG(Dofference of Gaussians)检测，但SIFT会通过一个特征向量来描述关键点周围区域的情况

# # SURF采用快速Hessian算法检测关键点
# # cv2.xfeatures2d.SURF_create(value) # value越高能识别的特征越少
# img = cv2.imread("image/4.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# def func(algorithm, par=None):
#     algorithms = {
#         "SIFT" : cv2.xfeatures2d.SIFT_create(),
#         "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
#         "ORB": cv2.ORB_create()
#     }
#     return algorithms[algorithm]

# f = "ORB"
# alg = func(f)
# keypoints, descriptor = alg.detectAndCompute(gray, None)
# img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, color=(51, 163, 236))
# cv2.imshow(f, img)
# cv2.waitKey()
# cv2.destroyAllWindows()



# 基于ORB的特征检测和特征匹配
