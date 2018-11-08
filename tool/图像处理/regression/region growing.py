# coding:UTF-8
# 2018-10-16
# region growing
# 区域生长法

import numpy as np
import os
import cv2
import datetime
from threshed import getThreshValue, loadData
from regression import *


__suffix = ["png", "jpg"]


def file(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def handle(dirs, out_dir, clip, w0):
    start_time = datetime.datetime.now()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = file(dirs)

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
            img = cv2.imread(f, 0)
            x,w,y,h = clip
            img = img[x:w , y:h]
            img= crop(img, img_dirs, w0)
            # img_new = normalization(img)
            # img_new = cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)

            # 6. 保存图片
            saveImage(img_dirs, img_new, "_new")

            # 控制台输出
            printToConsole(start_time, f, count, total, 5)
            success += 1

        except Exception as e:
            saveError(e, out_dir, f)
            fail += 1
            print()

    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


def crop(img, img_dirs, weight):
    img_w, img_h = img.shape
    saveImage(img_dirs, img, "_old")

    # 获得原图的自适应阈值图
    # adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

    # 去噪
    img_med = cv2.medianBlur(img, 5)
    kernel = np.zeros((7,7), np.uint8)
    img = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)
    saveImage(img_dirs, img, "_remove_noise") # 去除噪声的图片
    # 获得处理后的二值图像
    old_thresh, thresh = getThresh(img, weight)
    saveImage(img_dirs, thresh, "_raw_thresh") # 经过闭运算的二值图
    saveImage(img_dirs, old_thresh, "_old_thresh") # 没有经过闭运算的二值图

    # 使用区域生长获得轮廓
    res, growing = regionGrowing(img, thresh)


    # 旋转
    # res = ratation(res)


    # for i in range(img_w):
    #     for j in range(img_h):
    #         if growing[i][j] == 0:
    #             adaptive[i][j] = 0
    # 扩充边缘
    x, y, w, h = cv2.boundingRect(growing)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20

    # 切片
    img_new = res[y:y+h, x:x+w]
    # new_adaptive = adaptive[y:y+h, x:x+w]

    # # 保存基于原图的自适应分割图
    # new_adaptive = normalization(new_adaptive, new_adaptive.shape[1], new_adaptive.shape[0])
    # saveImage(img_dirs, new_adaptive, "_original_adaptive")

    # 保存二值图像, 生长区域
    saveImage(img_dirs, growing, "_growing_region")
    # saveImage(img_dirs, thresh, "_thresh")
    # 转换为数组
    img_new = np.array(img_new)

    return img_new


def saveImage(img_dirs, image, mid_name):
    """
    保存图像
    """
    basename = os.path.basename(img_dirs)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    suffix = file[-1]
    image_file = os.path.join("\\".join(img_dirs.split("\\")[:-1]), file_prefix + mid_name + suffix)
    cv2.imwrite(image_file, image)


def getThresh(img, weight):
    """
    获得二值图形
    """
    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    thresh_value, _, _, thresh = getThreshValue(img, weight)
    
    # 二值,闭运算
    ret, thresh = cv2.threshold(thresh , thresh_value, 255, cv2.THRESH_BINARY)
    old_thresh = thresh
    kernel = np.zeros((7,7), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) # 闭运算，封闭小黑洞
    thresh = cv2.medianBlur(thresh, 5)

    return old_thresh, thresh


def regionGrowing(img, thresh):
    """
    区域生长
    """
    m, n = thresh.shape
    r, c = m // 2, n // 2 # 种子起始点
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = []
    queue.append([r, c])
    visited[r][c] = True
    while len(queue) != 0:
        row, col = queue.pop()
        if row > 1 and not visited[row - 1][col] and thresh[row - 1][col] != 0:
            queue.append([row - 1, col])
            visited[row - 1][col] = True

        # 往右搜索
        if row + 1 < m and not visited[row + 1][col] and thresh[row + 1][col] != 0:
            queue.append([row + 1, col])
            visited[row + 1][col] = True

        # 往上搜索
        if col - 1 >= 0 and not visited[row][col - 1] and thresh[row][col - 1] != 0:
            queue.append([row, col -1])
            visited[row][col - 1] = True

        # 往下搜搜
        if col + 1 < n and not visited[row][col + 1] and thresh[row][col + 1] != 0:
            queue.append([row, col + 1])
            visited[row][col + 1] = True  

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                thresh[i][j] = 0
                img[i][j] = 0

    return img, thresh


def normalization(img, w, h):
    """
    归一化
    """
    if w > h:
        gap = w - h
        fill = np.zeros([1, w], np.uint8)
        for i in range(gap//2):
            img = np.concatenate((img,fill), axis = 0)
        for i in range(gap//2):
            img = np.concatenate((fill, img), axis = 0)
    elif w < h:
        gap = h - w
        fill = np.zeros([h, 1], np.uint8)
        for i in range(gap//2):
            img = np.concatenate((img,fill), axis = 1)
        for i in range(gap//2):
            img = np.concatenate((fill, img), axis = 1)
    else:
        pass

    img_new = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR)\

    return img_new

def ratation(res):
    img_w, img_h = np.shape(res)
    image, contours, hier = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

    # 寻找最大轮廓
    max_contour = None
    max_area = 0
    noise = 0.8 * img_w * img_h # 可能会识别边界, 但这样处理后会导致返回值为None
    for c in contours:
        # print(cv2.contourArea(c)) # test
        if cv2.contourArea(c) > max_area and cv2.contourArea(c) < noise:
            max_area = cv2.contourArea(c)
            max_contour = c


    width, height = cv2.minAreaRect(max_contour)[1]

    rect = cv2.minAreaRect(max_contour)
    box = cv2.boxPoints(rect)  # 获取最小外接矩形的4个顶点
    box = np.int0(box)

    if 0 not in box.ravel():

        '''绘制最小外界矩形
        for i in range(4):
            cv2.line(image, tuple(box[i]), tuple(box[(i+1)%4]), 0)  # 5
        '''
        # 旋转角度
        theta = cv2.minAreaRect(max_contour)[2]
        # if abs(theta) <= 45:
        print('图片的旋转角度为%s.'%theta)
        sign = 1
        if theta < 0:
            sign = -1
        if abs(theta) > 45:
            angle = sign * (abs(theta) - 90)
        else:
            angle = theta

    center = (img_w//2, img_h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    res = cv2.warpAffine(res, M, (img_w*4, img_h*4), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return res

if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image\\thresh" # 原图片存储路径
    out_dir = "C:\\Study\\test\\xxxx" # 存储路径

    # 加载数据
    data = "new_data.txt"

    # # 通过handleData.py 文件获得
    # label = "C:\\Study\\test\\data\\label.txt"
    # d = "C:\\Study\\test\\data\\data.txt"
    # from handleData import *
    # getData(label, d, data)

    feature, label = loadData(data)
    # 训练
    print ("traing...")
    method = ""
    if method == "bfgs":  # 选择BFGS训练模型
        print("using BFGS...")
        w0 = bfgs(feature, label, 0.5, 50, 0.4, 0.55)
    elif method == "lbfgs":  # 选择L-BFGS训练模型
        print("using L-BFGS...")
        w0 = lbfgs(feature, label, 0.5, 50, m=20)
    else:  # 使用最小二乘的方法
        print("using LMS...")
        w0 = ridgeRegression(feature, label, 0.5)

    print("\nhandling...")
    handle(dirs, out_dir, (45,-45,45,-45), w0)