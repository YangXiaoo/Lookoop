# coding:UTF-8
# 2018-11-6
# 使用回归法得到阈值分割，未归一化

import numpy as np
import os
import cv2
import datetime
from regression import ridgeRegression
from api import getFiles, saveImage, saveError, printToConsole, moveNoise, loadData, getHistogram, regionGrowing, getThreshValuebyHistogram, handleHistogram

def handle(dirs, out_dir, clip, w0):
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
            img = moveNoise(img)

            # 获得阈值并二值化
            thresh_value = getThreshValuebyHistogram(img, w0, is_handle=False)
            threshold, thrshed_img = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)
            saveImage(img_dirs, "_threshed_raw", thrshed_img)

            # 使用区域生长法分割
            img_segement, thresh_img = regionGrowing(img, thrshed_img)
            saveImage(img_dirs, "_threshed", thresh_img)

            # 去除多余边缘
            img_remove_margin = moveMargin(img_segement, thresh_img)
            saveImage(img_dirs, "_remove_margin", img_remove_margin)

            # 扩充为正方形并缩小为256x256
            img_new = normalization(img_remove_margin)
            saveImage(img_dirs, "_new", img_new)
            
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
    file_path = "C:\\Study\\test\\old"
    out_dir = "C:\\Study\\test\\old_no_norm_no_sucessxxx"
    data = "new_data.txt"
    feature, label = loadData(data)
    # 直方图归一化
    # feature = handleHistogram(feature)
    w0 = ridgeRegression(feature, label, 0.5)
    handle(file_path, out_dir, (45,-45,45,-45), w0)