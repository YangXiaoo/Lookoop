# coding:UTF-8
# 2018-11-4
# 标准图片切片

import numpy as np
import os
import cv2
import datetime



__suffix = ["png", "jpg"]


def getFile(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def handle(dir_path):
    files = getFile(dir_path)
    for f in files:
        img = cv2.imread(f, 0)
        x,w,y,h = 45,-45,45,-45
        img = img[x:w , y:h]
        saveImage(f, img, "_new")



def saveImage(img_dirs, image, mid_name):
    """
    保存图像
    """
    basename = os.path.basename(img_dirs)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    suffix = file[-1]
    image_file = os.path.join("\\".join(img_dirs.split("\\")[:-1]), file_prefix + mid_name + suffix)
    cv2.imwrite(image_file, image)


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\est_model\\standard" # 原图片存储路径
    handle(dirs)