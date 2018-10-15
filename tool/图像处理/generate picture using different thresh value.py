# coding:UTF-8
# 2018-10-15
# 确定阈值

import numpy as np
import os
import cv2

__suffix = ["png", "jpg"]


def loadPic(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file

def handle(dirs, out_dir, clip):
    """
    随机选取20张图片,在像素平均值附近取值
    dirs: 原图路径,20张图片
    out_dir: 二值图片输出路径
    clip = (30,-30,30,-30)
    """
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    files = loadPic(dirs)
    out_data = os.path.join(out_dir, 'adata.txt')
    data_file = open(out_data, "w")

    count = 0
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
        print("mean value: ",mean_value)

        # 计算方差的
        sum_diff = 0
        for i in range(img_w):
            for j in range(img_h):
                diff = float((mean_value - thresh[i][j]) * (mean_value - thresh[i][j]))
                sum_diff += diff
        print(sum_diff)
        variance = int((sum_diff // (img_w * img_h))**0.5)
        print("variance: ", variance)

        # 写入数据
        # 图像索引+均值+标准偏差 如: 0   28  38
        data = str(count) + "\t" + str(mean_value) + "\t" + str(variance) + '\n'
        data_file.write(data)

        # 获取10个阈值
        thresh_value = []
        small = mean_value
        left = 0
        while small > 0 and left < 10:
            thresh_value.append(small)
            small -= 2
            left += 1


        # 大于均值的很差，所以不考虑了
        # large = mean_value
        # right = 0
        # while large < 255 and right < 10:
        #     thresh_value.append(large)
        #     large += 3
        #     right += 1

        
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
    os.startfile(out_dir)


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image\\thresh"
    out_dir = "C:\\Study\\test\\thresh"
    handle(dirs, out_dir, clip=(35,-35,35,-35))




