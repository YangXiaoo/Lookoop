# coding:UTF-8
# 2018-10-15
# 确定阈值
# 自适应阈值处理: https://blog.csdn.net/sinat_21258931/article/details/61418681

"""
运行此程序获得原图像的二值图，并保存
"""

from regression import *
import numpy as np
import os
import cv2
import datetime
import matplotlib.pyplot as plt
import matplotlib
__suffix = ["png", "jpg"]


def loadPic(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def loadData(file_path):
    '''
    导入训练数据
    file_path: 数据文件
    '''
    # 将标签添加到数据中
    f = open(file_path)
    feature = []
    label = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        for i in range(2, len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        feature.append(feature_tmp)
        label.append(float(lines[-1]))
    f.close()
    
    return np.mat(feature), np.mat(label).T


def handle(dirs, out_dir, clip, weight):
    """
    二值处理
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

        v, mean_value, variance, thresh = getThreshValue(img, weight)

        print("mean value: ", mean_value, "variance: ", variance, "thresh value: ", v)


        ######### 二值处理 ##########
        ret, new_thresh = cv2.threshold(thresh , v, 255, cv2.THRESH_BINARY)
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

def getThreshValue(img, weight):
    """
    获得图像img的拟合阈值
    """
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

    # 获得直方图
    histogram = [1 for _ in range(256)]
    for i in range(img_w):
        for j in range(img_h):
            histogram[thresh[i][j]] += 1


    ######### 通过权重得到阈值 ##########
    inputs = [] # inputs = [mean_value, variance]
    inputs.extend(histogram)
    data = []
    for i in inputs:
        data.append([i])
    data = np.mat(data)
    # print(np.shape(data), np.shape(weight))

    v = int((data.T * weight)[0, 0])


    # 对阈值进行判断, 去除漂移值
    if v > mean_value * 0.9:
        v = int(mean_value * 0.9)
    if v < mean_value * 0.6:
        v = int(mean_value * 0.6)

    return v, mean_value, variance, thresh


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image\\train-m"
    out_dir = "C:\\Study\\test\\threshed_old"

    print("loading data ...")
    feature, label = loadData("new_data.txt")
    # 训练
    print ("traing...")
    method = ""  # 选择的方法
    if method == "bfgs":  # 选择BFGS训练模型
        print("using BFGS...")
        w0 = bfgs(feature, label, 0.5, 50, 0.4, 0.55)
    elif method == "lbfgs":  # 选择L-BFGS训练模型
        print("using L-BFGS...")
        w0 = lbfgs(feature, label, 0.5, 50, m=20)
    else:  # 使用最小二乘的方法
        print("using LMS...")
        w0 = ridgeRegression(feature, label, 0.5)

    # print(w0)
    # print("\nhandling picture...")
    x = []
    y = []
    index = 0
    for w in w0:
        x.append(index)
        y.append(w[0, 0])
    x = np.array(x)
    y = np.array(y)
    print(np.shape(y))
    print(y)
    plt.bar(range(len(y)), y)

    plt.show()
    # handle(dirs, out_dir, (40,-40,40,-40), w0)




