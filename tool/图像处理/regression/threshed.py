# coding:UTF-8
# 2018-10-15
# 确定阈值
# 自适应阈值处理: https://blog.csdn.net/sinat_21258931/article/details/61418681
# update:2018-10-22(新的数据处理方法)
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
        for i in range(len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        feature.append(feature_tmp)
        label.append(float(lines[-1]))
    f.close()

    # 处理数据
    m, n = len(feature), len(feature[0])
    data = np.mat(np.ones((m, n)))
    for i in range(m):
        h = 0
        data[i, 0] = 1
        for j in range(1, n):
            if feature[i][j] > feature[i][j - 1]:
                h = j
                data[i, j] = data[i, j - 1] + 1
            else:
                if feature[i][j] == feature[i][j - 1]:
                    h = j
                for k in range(j, h, -1):
                    if data[i, j] >= data[i, j - 1]:
                        data[i, j - 1] += 1

    
    return data, np.mat(label).T


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
    histogram = [0 for _ in range(256)]
    for i in range(img_w):
        for j in range(img_h):
            histogram[thresh[i][j]] += 1

    ######### 通过权重得到阈值 ##########
    inputs = [mean_value, variance]
    inputs.extend(histogram)
    n = len(inputs)

    data_tmp = [0 for _ in range(n)]
    data_tmp[0] = 1
    h = 0
    for i in range(1, n):
        if inputs[i] > inputs[i - 1]:
            h = i
            data_tmp[i] = data_tmp[i-1] + 1
        else:
            if inputs[i] == inputs[i - 1]:
                h = i 
            for j in range(i, h, -1):
                if data_tmp[j] >= data_tmp[j - 1]:
                    data_tmp[j - 1] += 1

    data = np.mat(data_tmp)
    print(np.shape(data), np.shape(weight))

    v = int((data * weight)[0, 0])


    # 对阈值进行判断, 去除漂移值
    if v > mean_value * 0.9:
        v = int(mean_value * 0.9)
    if v < mean_value * 0.6:
        v = int(mean_value * 0.6)

    return v, mean_value, variance, thresh


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image\\train-m"
    out_dir = "C:\\Study\\test\\threshed_new"

    print("loading data ...")
    # 加载数据
    data = "new_data.txt"
    feature, label = loadData(data)
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
    # handle(dirs, out_dir, (40,-40,40,-40), w0)


    x = []
    y = []
    index = 0
    for w in w0:
        x.append(index)
        y.append(w[0, 0])
    x = np.array(x)
    y = np.array(y)
    # color = np.arctan2(y, x)
    # # 绘制散点图
    # plt.scatter(x, y, s = 75, c = color, alpha = 0.5)
    # # 设置坐标轴范围
    # plt.xlim((-5, 5))
    # plt.ylim((-5, 5))

    # # 不显示坐标轴的值
    # plt.xticks(())
    # plt.yticks(())

    # plt.show()

    # # 设置matplotlib正常显示中文和负号
    # matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
    # matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
    # # 随机生成（10000,）服从正态分布的数据
    # index = 0
    # data = []
    # for i in y:
    #     for c in range(i):
    #         data.append(index)
    #     index += 1
    # """
    # 绘制直方图
    # data:必选参数，绘图数据
    # bins:直方图的长条形数目，可选项，默认为10
    # normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
    # facecolor:长条形的颜色
    # edgecolor:长条形边框的颜色
    # alpha:透明度
    # """
    # plt.hist(data, bins=256, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    # # 显示横轴标签
    # plt.xlabel("区间")
    # # 显示纵轴标签
    # plt.ylabel("频数/频率")
    # # 显示图标题
    # plt.title("频数/频率分布直方图")
    # plt.show()
    print(y)
    plt.bar(range(len(y)), y)

    plt.show()