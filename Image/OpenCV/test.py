# 2018-9-6
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第五章笔记
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import os
import cv2
from scipy import ndimage
from skimage import transform


# import cv # 已经被遗弃


img = cv2.imread("image/m_5.jpg", 0)
w, h= img.shape
s = min(w, h)
img = img[:s, :s]
print(img)
img=transform.resize(img, (500, 500))
cv2.imwrite("xx.jpg", np.asarray(img, np.uint8))
plt.imshow(img)
plt.show()