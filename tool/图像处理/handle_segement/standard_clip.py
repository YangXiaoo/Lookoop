# coding:UTF-8
# 2018-11-4
# 标准图片切片

import cv2
import os
from api import getFiles, saveImage, standardPicClip


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\est_model\\standardxxxx" # 原图片存储路径
    out_dirs = "C:\\Study\\test\\est_model\\xxx" # 输出路径
    standardPicClip(dirs, out_dirs)