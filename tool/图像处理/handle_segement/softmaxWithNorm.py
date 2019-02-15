# coding:UTF-8
# 2018-11-15
# 使用softmax到阈值分割，未归一化

import numpy as np
import os
import cv2
import datetime
import pickle
from softmax import train
import matplotlib
import matplotlib.pyplot as plt
import traceback
matplotlib.use('Agg')
from api import getFiles, saveImage, saveError, printToConsole, moveNoise, loadData, getHistogram, regionGrowing, getThreshValuebySoftmax, handleHistogram, loadWeights, batchProcess, printEst, saveEst, moveMargin, normalization

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
            # saveImage(img_dirs, "_original", img) # 保存原图

            # 获得预测值阈值，二值化
            thresh_value = getThreshValuebySoftmax(img, w0)
            threshold, thrshed_img = cv2.threshold(img, thresh_value + 2, 255, cv2.THRESH_BINARY)
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
            traceback.print_exc()


    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


if __name__ == '__main__':
    file_path = r"C:\Study\test\bone\2"
    out_dir = "C:\\Study\\test\\softmax_norm_test"
    # weights_file = "weights.npy"
    # w0 = loadWeights(weights_file)
    # w0 = np.load(weights_file)
    # print(np.shape(w0))
    # print(w0)
    inputfile = "data.txt"
    feature, label = loadData(inputfile)
    feature = handleHistogram(feature)
    # print(np.shape(feature), np.shape(label))
    # print(feature)
    k = 256
    w0 = train(feature, label, k, 100000, 0.1)

    fp = open("pickle_weight_test.dat", "wb")
    pickle.dump(w0, fp)
    fp.close()

    handle(file_path, out_dir, (45,-45,45,-45), w0)

    # # 分割评估
    # file_path = "C:\\Study\\test\\100-gt" # 标准分割图像目录路径
    # out_dir = "C:\\Study\\test\\est_results" #结果保存目录
    # print("softmax")
    # file_path_2 = "C:\\Study\\test\\softmax_no_norm_no_limited" # 方法一得到分割图像路径
    # res = batchProcess(file_path, file_path_2)
    # printEst(res, "softmax")
    # saveEst(res, "softmax", out_dir)