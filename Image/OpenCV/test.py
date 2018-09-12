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

# 图像裁剪
img = cv2.imread("image/m_5.jpg", 0) # 0表示以对读入图像灰度处理
w, h= img.shape
print(img.shape)
s = min(w, h)  # 取最小值裁剪成sxs大小
pre = dummy = img
dummy = transform.resize(dummy, (500, 500))
plt.subplot(121)
plt.imshow(dummy)
img = img[:s, :s]
print(img)
img=transform.resize(img, (500, 500))
cv2.imwrite("xx.jpg", np.asarray(img, np.uint8))
plt.subplot(122)
plt.imshow(img)
plt.show()


# n = [[1,2,3,5,65,7], [55,233,44,66,8798,2], [55444,233,44,66,8798,2]]
# p = np.asarray(n)
# t = [0, 2,2]
# r = p[t[:2]]
# print(math.abs(-1))