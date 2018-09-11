# 2018-9-8
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892

# 第八章笔记
# 目标跟踪

import numpy as np
from matplotlib import pyplot as plt
import os
import cv2



# # 基本运动检测
# camera = cv2.VideoCapture(0)

# es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
# kernel = np.ones((5,5),np.uint8)
# background = None

# while (True):
#   ret, frame = camera.read()
#   if background is None:
#     background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     background = cv2.GaussianBlur(background, (21, 21), 0) # 高斯模糊
#     continue
  
#   gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
#   diff = cv2.absdiff(background, gray_frame) # 得到差值
#   diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1] # 二值化
#   diff = cv2.dilate(diff, es, iterations = 2) # 根据元素结构膨胀
#   image, cnts, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
#   for c in cnts:
#     if cv2.contourArea(c) < 1500:
#       continue
#     (x, y, w, h) = cv2.boundingRect(c)
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
  
#   cv2.imshow("contours", frame)
#   cv2.imshow("dif", diff)
#   if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
#       break

# cv2.destroyAllWindows()
# camera.release()