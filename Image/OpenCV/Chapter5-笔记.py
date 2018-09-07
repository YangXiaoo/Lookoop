# 2018-9-6
# OpenCV3 计算机视觉 Python语言实现
# Github : https://github.com/techfort/pycv
# 英文教程： https://docs.opencv.org/3.2.0/d6/d00/tutorial_py_root.html
# 中文翻译： https://www.cnblogs.com/Undo-self-blog/p/8423851.html
# opencv中文教程: https://www.kancloud.cn/aollo/aolloopencv/272892
# 第五章笔记
import numpy as np
import matplotlib.pyplot
import scipy.special
import os
import cv2
from scipy import ndimage
# import cv # 已经被遗弃


# 视频人脸识别
def detect():
    face = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
    eye = cv2.CascadeClassifier("data/haarcascade_eye.xml")

    camera = cv2.VideoCapture(0) # 0表示使用第一个摄像头

    while True:
        ret, frame = camera.read() # ret:布尔值表示是否读取帧成功, frame为帧本身
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 检测人脸需要基于灰度图像

        faces = face.detectMultiScale(gray, 1.3, 5) 
        # faces = face.detectMultiScale(gray, scaleFactor, minNeighbors)
        # scaleFactor: 每次迭代时图像的压缩率
        # minNeighbors: 每个人脸矩形保留近似邻近数目的最小值

        for x,y,w,h in faces:
            img = cv2.rectangle(frame, (x,y), (x + w, y + h), (250, 0, 0), 2)

            eye_area = gray[y : y + h, x : x + w]
            eyes = eye.detectMultiScale(eye_area, 1.03, 5, 0, (40, 40))
            # eye.detectMultiScale(eye_area, 1.03, 5, 0, (40, 40))中
            # (40, 40)参数目的是为了消除假阳性(false positive)的影响， 将眼睛搜索的最小尺寸现实为40x40
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(frame, (x + ex, y + ey),(x + ex + ew, y + ey + eh), (0, 255, 0), 2)

        cv2.imshow("face", frame)
        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect()



# 生成人脸识别数据
def generateFace():
    face = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
    eye = cv2.CascadeClassifier("data/haarcascade_eye.xml")

    camera = cv2.VideoCapture(0)
    count = 0 # 图片计数
    end = 100 # 生成100图片

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)

        for x,y,w,h in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            f = cv2.resize(gray[y : y + h, x : x + w], (200, 200)) # 将人脸resize

            # 保存
            cv2.imwrite("face/yx/%s.pgm" % str(count), f)
            count += 1

        cv2.imshow("face", frame)

        if cv2.waitKey(1000 // 12) & 0xff == ord("q") or count == end:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generateFace()