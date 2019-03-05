# coding:UTF-8
# 2018-10-15
# update: 2018-10-17(增加序号对应的图片)
# 确定阈值

"""
运行之后，手选最佳阈值并填入label.txt文件中, 每个数据之间间隔为制表符
"""

import numpy as np
import os
import cv2
from api import getFiles

def handle(dirs, out_dir, clip):
    """
    随机选取20张图片,在像素平均值附近取值
    dirs: 原图路径,20张图片
    out_dir: 二值图片输出路径
    clip = (30,-30,30,-30)
    """
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    files = getFiles(dirs)

    # 在label.txt里加上阈值
    out_label = os.path.join(out_dir, 'label.txt')
    label_file = open(out_label, "w")

    out_data = os.path.join(out_dir, 'data.txt')
    data_file = open(out_data, "w")

    # 原图对应序号
    record = os.path.join(out_dir, 'record.txt')
    record_file = open(record, "w")

    count = 0
    for f in files:

        record_data = str(count) + '\t' + str(f) + '\n'
        record_file.write(record_data)
        # continue


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
        print()

        # 计算方差的
        sum_diff = 0
        for i in range(img_w):
            for j in range(img_h):
                diff = float((mean_value - thresh[i][j]) * (mean_value - thresh[i][j]))
                sum_diff += diff
        # print(sum_diff)
        variance = int((sum_diff // (img_w * img_h))**0.5)
        print("mean value: ",mean_value, ", variance: ", variance)

        # 计算直方图
        histogram = [0 for _ in range(256)]
        for i in range(img_w):
            for j in range(img_h):
                histogram[thresh[i][j]] += 1
        # print(histogram)
        for i in range(len(histogram)):
            histogram[i] = str(histogram[i])
            
        # 写入数据
        # 先写入均值 直方图 方差 数据 至 data.txt

        # histogram转换类型
        for i in range(len(histogram)):
            histogram[i] = str(histogram[i])

        data = str(count) + "\t" + str(mean_value) + "\t" + str(variance) + '\t' + "\t".join(histogram) + '\n'
        data_file.write(data)

        # 写入标签数据至label.txt
        label = str(count) + "\t" + str(mean_value) + "\t" + str(variance) + '\n'
        label_file.write(label)


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


        # 大于均值的很差，所以不考虑了
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

            # 保存
            basename = os.path.basename(f)
            file = os.path.splitext(basename)
            file_prefix = str(count) # file[0]
            file_suffix = file[-1]
            if v == mean_value:
                image_name = file_prefix + '_thresh_value_' + str(v) + '_mean' + file_suffix
            else:
                image_name = file_prefix + '_thresh_value_' + str(v) + file_suffix
            out_file = os.path.join(out_dir,  image_name)
            print("saving :", out_file)
            cv2.imwrite(out_file, new_thresh)

        count += 1

    data_file.close()
    label_file.close()
    record_file.close()
    os.startfile(out_dir)


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image\\failed"
    out_dir = "C:\\Study\\test\\thresh_failed"
    handle(dirs, out_dir, clip=(40,-40,40,-40))




