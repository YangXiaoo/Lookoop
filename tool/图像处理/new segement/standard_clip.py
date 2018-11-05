# coding:UTF-8
# 2018-11-4
# 标准图片切片

import cv2
from api import getFiles, saveImage


def handle(dir_path):
    files = getFiles(dir_path)
    for f in files:
        img = cv2.imread(f, 0)
        x,w,y,h = 45,-45,45,-45
        img = img[x:w , y:h]
        saveImage(f, "_new", img)


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\est_model\\standardxxxx" # 原图片存储路径
    handle(dirs)