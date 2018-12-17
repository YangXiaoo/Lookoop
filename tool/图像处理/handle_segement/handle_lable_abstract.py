# coding:UTF-8
# 2018-12-17
# 图像归一化

import numpy as np  
import os
import cv2
import datetime
from api import getFiles, saveImage, saveError, printToConsole,  moveMargin, normalization

def handle(dirs, out_dir):
    start_time = datetime.datetime.now()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = getFiles(dirs)

    total = len(files)
    fail, success, skip, count = 0, 0, 0, 0

    for f in files:
        count += 1
        print(count, '/', total)
        img_dirs = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_dirs):
            skip += 1
            continue
        try:
            img = cv2.imread(f, 0)
            img_new = moveMargin(img, img)
            img_new = normalization(img_new)
            saveImage(img_dirs, "", img_new)

            # 打印信息到输出台
            printToConsole(start_time, f, count, total, 5)
            success += 1
        except Exception as e:
            # 错误情况
            saveError(e, out_dir, f)
            fail += 1


    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


if __name__ == '__main__':
    file_path = "C:\\Study\\test\\bone\\100-gt"
    out_dir = "C:\\Study\\test\\abstract"
    handle(file_path, out_dir)