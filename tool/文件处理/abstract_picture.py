# coding:UTF-8
# 2018-11-6
# 将图片xxx/label.png重命名为xxx.png并保存
import os
import sys 
import numpy as np
__suffix = ["png", "jpg"]
def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file

file_path = "C:\\Study\\test\\fm-1-2.4"
out_dir = "C:\\Study\\test\\out" # 保存目录
if not os.path.isdir(out_dir):
    os.mkdir(out_dir)
files = getFiles(file_path)
for f in files:
    basename = os.path.basename(f)
    preffix = basename.split('.')[0]
    if preffix != "label":
        continue
    new_name = f.split('\\')[-2] + '.png'
    new_path = os.path.join(out_dir, new_name)
    os.system("copy %s %s" % (f, new_path))
os.startfile(out_dir)

