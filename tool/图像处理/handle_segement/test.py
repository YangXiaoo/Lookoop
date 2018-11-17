# coding:UTF-8
# 2018-11-6
# 将图片xxx/label.png重命名为xxx.png并保存
import os
import sys 
import numpy as np
import cv2
from api import getFiles, saveImage, skipChar
from PIL import Image

file_path = "C:\\Study\\test\\100-original"
out_dir = "C:\\Study\\test\\1ssssssss"

skipChar(file_path, out_dir)


# file_path = "C:\\Study\\test\\fm-1-2.4\\label.png"
# s_img = Image.open(file_path)
# s_img = s_img.convert("L")
# data_f = s_img.getdata()
# data_f = np.matrix(data_f)
# m, n = np.shape(data_f)
# for i in range(m):
#   for j in range(n):
#       if data_f[i, j] == 1:
#           data_f[i. j] = 255
# cv2.imwrite()
