# coding:UTF-8
# 2018-12-9
# 将图片xxx/label.png转换为0,256并重命名为xxx.png并保存
import os
import numpy as np
import cv2
from PIL import Image

__suffix = ["png"]

def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


file_path = "C:\\Study\\test\\1"
out_dir = "C:\\Study\\test\\out_test" # 保存目录

if not os.path.isdir(out_dir):
    os.mkdir(out_dir)

files = sorted(getFiles(file_path))
count = 0
for i, f in enumerate(files):
    basename = os.path.basename(f)
    preffix = basename.split('.')[0]
    if preffix != "label":
        continue
    print(f)
    img = np.matrix(Image.open(f))
    back = np.ones(img.shape) * 256
    ret = np.multiply(img, back)
    # ret_path = os.path.join(out_dir, f.split('\\')[-2] + '.png')
    ret_path = os.path.join(out_dir, str(count) + '.png')
    cv2.imwrite(ret_path, ret)
    count += 1
os.startfile(out_dir)