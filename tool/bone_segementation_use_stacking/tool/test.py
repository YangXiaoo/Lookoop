# coding:utf-8
# 2019-5-9
# 根据切边信息裁剪图片
import os
import pickle
import cv2
import datetime
import numpy as np

import api


def handle(dirs, out_dir, clip):
    start_time = datetime.datetime.now()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = api.getFiles(dirs)

    total = len(files)
    fail, success, skip, count = 0, 0, 0, 0

    for f in files[:10]:
        count += 1
        print(count, '/', total)
        img_dirs = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_dirs):
            skip += 1
            continue
        # try:
        # 读取图片
        img = cv2.imread(f)
        # 切边
        x,w,y,h = clip
        img = img[x:w , y:h]
        # 去除噪点
        img = api.moveNoise(img, 7)
        # 根据最大熵算法获得最佳阈值
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # noise removal
        kernel = np.ones((3,3),np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernel, iterations = 4)

        # sure background area
        sure_bg = cv2.dilate(opening,kernel,iterations=4)
        api.saveImage(img_dirs, "_sure_bg", sure_bg)

        # Finding sure foreground area
        dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
        ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

        api.saveImage(img_dirs, "_sure_fg", sure_fg)

        # Finding unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg,sure_fg)

        api.saveImage(img_dirs, "_unknown", unknown)
        # Marker labelling
        ret, markers = cv2.connectedComponents(sure_fg)
        api.saveImage(img_dirs, "_markers", markers)

        # Add one to all labels so that sure background is not 0, but 1
        markers = markers+1

        # Now, mark the region of unknown with zero
        markers[unknown==255] = 0
        markers = cv2.watershed(img, markers)
        img[markers == -1] = [255,0,0]
            
        # threshold, thrshed_img = cv2.threshold(img, threshed, 255, cv2.THRESH_BINARY)
        # # saveImage(img_dirs, "_threshed_raw", thrshed_img)

        # # 使用区域生长法分割
        # img_segement, thresh_img = regionGrowing(img, thrshed_img)
        api.saveImage(img_dirs, "_threshed", img)


        # 扩充为正方形并缩小为256x256
        # img_new = api.normalization(threshed)
        # saveImage(img_dirs, "_new", img_new)

        # 打印信息到输出台
        api.printToConsole(start_time, f, count, total, 5)
        success += 1
        # except Exception as e:
        #     # 错误情况
        #     api.saveError(e, out_dir, f)
        #     fail += 1

    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


if __name__ == '__main__':
    file_path = r"C:\Study\test\bone\1ssssssss"
    out_dir = r"C:\Study\test\bone\watershed"
    handle(file_path, out_dir, (45,-45,45,-45))

