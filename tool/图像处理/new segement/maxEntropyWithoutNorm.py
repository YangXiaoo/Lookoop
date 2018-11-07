# coding:UTF-8
# 2018-11-6
# 使用信息熵作为阈值进行分割，没有进行归一化处理

import numpy as np
import os
import cv2
import datetime
from api import getFiles, saveImage, saveError, printToConsole, maxEntrop, moveNoise, regionGrowing

def handle(dirs, out_dir, clip):
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
            # 读取图片
            img = cv2.imread(f, 0)
            # 切边
            x,w,y,h = clip
            img = img[x:w , y:h]
            # 去除噪点
            img = moveNoise(img, 7)
            # 根据最大熵算法获得最佳阈值
            threshed = maxEntrop(img)
            # 二值化
            threshold, thrshed_img = cv2.threshold(img, threshed*0.4, 255, cv2.THRESH_BINARY)
            # 使用区域生长法分割
            img_segement, thresh_img = regionGrowing(img, thrshed_img)
            # 保存
            saveImage(img_dirs, "_new", img_segement)

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
    file_path = "C:\\Study\\test\\1ssssssss"
    out_dir = "C:\\Study\\test\\maxEntrop"
    handle(file_path, out_dir, (45,-45,45,-45))