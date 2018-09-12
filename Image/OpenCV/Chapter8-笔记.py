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



# 卡尔曼滤波器预测鼠标位置
# https://blog.csdn.net/angelfish91/article/details/61768575
measurements = []
predictions = []
frame = np.zeros((800, 800, 3), np.uint8)
last_measurement = current_measurement = np.array((2,1), np.float32) 
last_prediction = current_prediction = np.zeros((2,1), np.float32)

def mousemove(event, x, y, s, p):
    global frame, current_measurement, measurements, last_measurement, current_prediction, last_prediction
    last_prediction = current_prediction
    last_measurement = current_measurement
    current_measurement = np.array([[np.float32(x)],[np.float32(y)]])
    kalman.correct(current_measurement)
    current_prediction = kalman.predict()
    lmx, lmy = last_measurement[0], last_measurement[1]
    cmx, cmy = current_measurement[0], current_measurement[1]
    lpx, lpy = last_prediction[0], last_prediction[1]
    cpx, cpy = current_prediction[0], current_prediction[1]
    cv2.line(frame, (lmx, lmy), (cmx, cmy), (0,255,0))
    cv2.line(frame, (lpx, lpy), (cpx, cpy), (0,0,255))


cv2.namedWindow("kalman_tracker")
cv2.setMouseCallback("kalman_tracker", mousemove);

kalman = cv2.KalmanFilter(4,2,1)
kalman.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
kalman.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)
kalman.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],np.float32) * 0.03

while True:
    cv2.imshow("kalman_tracker", frame)
    if (cv2.waitKey(30) & 0xFF) == 27:
        break
    if (cv2.waitKey(30) & 0xFF) == ord('q'):
        cv2.imwrite('kalman.jpg', frame)
        break

cv2.destroyAllWindows()
