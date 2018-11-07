# coding:UTF-8
# 2018-11-4
# 标准图片切片

import cv2
import os
from api import getFiles, saveImage

def handle(dir_path, out_dir):
    files = getFiles(dir_path)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    for f in files:
        img = cv2.imread(f, 0)
        out_path = os.path.join(out_dir, f.split("\\")[-1])
        x,w,y,h = 45,-45,45,-45
        img = img[x:w , y:h]
        saveImage(out_path, "_new", img)
    os.startfile(out_dir)


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\est_model\\standardxxxx" # 原图片存储路径
    out_dirs = "C:\\Study\\test\\est_model\\xxx" # 输出路径
    handle(dirs, out_dirs)