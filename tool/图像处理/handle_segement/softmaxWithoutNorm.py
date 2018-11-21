# coding:UTF-8
# 2018-11-15
# 使用softmax到阈值分割，未归一化

import numpy as np
import os
import cv2
import datetime
from softmax import train, predict
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from api import getFiles, saveImage, saveError, printToConsole, moveNoise, loadData, getHistogram, regionGrowing, getThreshValuebySoftmax, handleHistogram, loadWeights, batchProcess, printEst, saveEst, saveModel

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
            # 获得预测值
            thresh_value = getThreshValuebySoftmax(img, w0)
            # 二值化
            threshold, thrshed_img = cv2.threshold(img, thresh_value + 2, 255, cv2.THRESH_BINARY)
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
    out_dir = "C:\\Study\\test\\softmax_no_norm_no_limited"
    # weights_file = "weights.npy"
    # w0 = loadWeights(weights_file)
    # w0 = np.load(weights_file)
    # print(np.shape(w0))
    # print(w0)
    inputfile = "data.txt"
    feature, label = loadData(inputfile)
    feature = handleHistogram(feature)
    # print(np.shape(feature), np.shape(label))
    #print(feature)
    k = 256
    w0 = train(feature, label, k, 200000, 0.1)
    saveModel("weights.txt", w0)
    actual_x = [] # 绘制直线的x轴坐标
    predict_x = [] # 绘制预测值的x坐标
    for i in label:
        actual_x.append(int(i[0]))
        predict_x.append(i[0])
    actual_y = actual_x # 直线的y坐标

    # 得到预测值
    predition = predict(feature, w0)
    m, n = np.shape(predition)
    error = np.mat(np.zeros((m)))
    predict_y = [] # 预测值的y坐标
    for i in predition:
        predict_y.append(i[0])
    color = np.arctan2(predict_y, predict_x)
    # 绘制散点图
    plt.scatter(predict_x, predict_y, s = 10, c = color, alpha = 1)
    # 设置坐标轴范围
    plt.xlim([0, 150])
    plt.ylim([0, 150])
    error[predict_y == actual_x] = 1
    print("correct rate:", np.sum(error)/m)
    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(actual_x, actual_y)
    plt.savefig("soft_max_iteration_100000")
    plt.show()

    handle(file_path, out_dir, (45,-45,45,-45), w0)

    file_path = "C:\\Study\\test\\100-gt" # 标准分割图像目录路径
    out_dir = "C:\\Study\\test\\est_results" #结果保存目录
    print("softmax")
    file_path_2 = "C:\\Study\\test\\softmax_no_norm_no_limited" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_2)
    printEst(res, "softmax")
    saveEst(res, "softmax", out_dir)