# coding:utf-8
# 2019-5-10
"""解决问题: 根据标准分割获得最佳阈值
1. 根据未分割的图片获得不同阈值分割图
2. 遍历原图i生成的不同分割图(经过最大连通域)，计算手掌区域T, 
	与标准手掌区域面积S作比较，得到分割图手掌区域P与手掌外区域Q比较
	准则:Q最小,P最大。最好的结果的阈值为最佳阈值

					 I___I
				   _//0_0\\_
					||---||
					=======
"""

import os
import pickle
import cv2

import api
import util

clip = []

def genDiffPicByThresholdValue(imgDir, outputDir):
	files = api.getFiles(imgDir)

	util.mkdirs(outputDir)

    for f in files:
        img = cv2.imread(f, 0)
        # 裁剪边缘
        x, w, y, h = clip
        img = img[x:w,y:h]

        ######### 二值处理 ##########
        img_w, img_h = img.shape
        # 去噪
        img_med = cv2.medianBlur(img, 5)
        kernel = np.zeros((7,7), np.uint8)
        thresh = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)

        # 不同阈值处理
        # 计算均值
        sums = 0
        for i in range(img_w):
            for j in range(img_h):
                sums += thresh[i][j]
        mean_value = sums // (img_w * img_h)


        # 获取n个阈值
        n = 20
        gap = 2 # 两个阈值之间的间隔
        thresh_value = []
        small = mean_value
        left = 0
        while small > 0 and left < n:
            thresh_value.append(small)
            small -= gap
            left += 1


        large = mean_value
        r = 5
        right = 0
        while large < 255 and right < r:
            thresh_value.append(large)
            large += 2
            right += 1

        for v in thresh_value:
            ret, new_thresh = cv2.threshold(thresh , v, 255, cv2.THRESH_BINARY)
            kernel = np.zeros((7,7), np.uint8)
            new_thresh = cv2.morphologyEx(new_thresh, cv2.MORPH_CLOSE, kernel)
            new_thresh = cv2.medianBlur(new_thresh, 5)

            out_file = os.path.join(outputdir,  image_name)
            cv2.imwrite(out_file, new_thresh)

        count += 1

def getBestThresholdValue():
	pass
	import random
	value =  predict + random.randint(-4, 4)