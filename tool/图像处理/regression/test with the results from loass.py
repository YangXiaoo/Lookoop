# coding:UTF-8
# 2018-10-15
# 确定阈值
# 自适应阈值处理: https://blog.csdn.net/sinat_21258931/article/details/61418681
from loass import *
import numpy as np
import os
import cv2
import datetime

__suffix = ["png", "jpg"]


def loadPic(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file

def handle(dirs, out_dir, clip, weight):
    """
    根据w得出阈值
    """
    start_time = datetime.datetime.now()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    files = loadPic(dirs)


    count, total = 1, len(files)
    for f in files:
        img = cv2.imread(f, 0)

        print()
        print(count, '/', total)
        if count % 5 == 0:
            end_time = datetime.datetime.now()
            expend = end_time - start_time
            print("expend time:", expend, "\nexpected time: ", expend / count * total)

        # 裁剪边缘
        x, w, y, h = clip
        img = img[x:w,y:h]

        img_w, img_h = img.shape

        # 去噪
        img_med = cv2.medianBlur(img, 5)
        kernel = np.zeros((7,7), np.uint8)
        thresh = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)


        ######### 计算特征参数 ##########
        # 不同阈值处理
        # 计算均值
        sums = 0
        for i in range(img_w):
            for j in range(img_h):
                sums += thresh[i][j]
        mean_value = sums // (img_w * img_h)

        # 计算标准方差的
        sum_diff = 0
        for i in range(img_w):
            for j in range(img_h):
                diff = float((mean_value - thresh[i][j]) * (mean_value - thresh[i][j]))
                sum_diff += diff
        variance = int((sum_diff // (img_w * img_h))**0.5)


        ######### 通过权重得到阈值 ##########
        # inputs = [mean_value, variance]
        # inputs = np.mat(inputs)
        # v = getPrediction(inputs, weight)[0, 0]
        v = int(1 * weight[0, 0] + mean_value * weight[1, 0] + variance * weight[2, 0])

        # 对阈值进行判断, 去除漂移值
        if v > mean_value * 0.9:
            v = int(mean_value * 0.9)
        if v < mean_value * 0.6:
            v = int(mean_value * 0.6)

        print("mean value: ", mean_value, "variance: ", variance, "thresh value: ", v)


        ######### 二值处理 ##########
        ret, new_thresh = cv2.threshold(thresh , v, 255, cv2.THRESH_BINARY)
        # new_thresh = cv2.adaptiveThreshold(thresh,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        #     cv2.THRESH_BINARY,11,2)
        kernel = np.zeros((7,7), np.uint8)
        new_thresh = cv2.morphologyEx(new_thresh, cv2.MORPH_CLOSE, kernel)
        new_thresh = cv2.medianBlur(new_thresh, 5)

        ######### 保存 ##########
        basename = os.path.basename(f)
        file = os.path.splitext(basename)
        file_prefix = file[0]
        file_suffix = file[-1]
        image_name = file_prefix + file_suffix
        out_file = os.path.join(out_dir,  image_name)
        print("saving :", out_file)
        cv2.imwrite(out_file, new_thresh)

        count += 1

    os.startfile(out_dir)


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image\\train-m"
    out_dir = "C:\\Study\\test\\thresh_test"

    print("loading data ...")
    feature, label = loadData("data.txt")
    # 训练
    print ("traing...")
    method = "lbfgs"  # 选择的方法
    if method == "bfgs":  # 选择BFGS训练模型
        print("using BFGS...")
        w0 = bfgs(feature, label, 0.5, 50, 0.4, 0.55)
    elif method == "lbfgs":  # 选择L-BFGS训练模型
        print("using L-BFGS...")
        w0 = lbfgs(feature, label, 0.5, 50, m=20)
    else:  # 使用最小二乘的方法
        w0 = ridgeRegression(feature, label, 0.5)

    print("\nhandling picture...")
    handle(dirs, out_dir, (40,-40,40,-40), w0)




