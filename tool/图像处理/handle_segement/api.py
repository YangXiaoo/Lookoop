# coding : UTF-8
# 2018-11-5
# 分割过程中一些基本操作封装

import os
import cv2
import datetime
import numpy as np
import numpy
import math
from decimal import *
import DBSCAN

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


__suffix = ["png", "jpg"]
__total = 256

def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def getData(file_path, new_file, out_file):
    '''
    合并训练数据
    file_path: 标签文件
    new_file: 数据文件
    将数据合成保存到out_file文件中
    '''
    # 获得数据标签   
    f = open(file_path)
    feature = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        for i in range(len(lines)):
            feature_tmp.append(lines[i])
        feature.append(feature_tmp)
    f.close()

    # 将标签添加到数据中
    new_f = open(new_file)
    new_feature = []
    label = []
    row = 0
    for line in new_f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        # print(row, float(feature[row][0]), float(lines[0]))
        if  row < len(feature) and float(feature[row][0]) == float(lines[0]):
            for i in range(len(lines) - 1):
                feature_tmp.append(lines[i])
            new_feature.append(feature_tmp)
            label.append(feature[row][-1])
            row += 1
    new_f.close()

    n_f = open(out_file, "w")
    m = len(new_feature)
    for i in range(m):
        n_f.write("\t".join(new_feature[i]) + '\t' + str(label[i]) + '\n')

    n_f.close()


def loadData(file_path, gap=1):
    '''
    导入训练数据
    数据格式
    [[0 41  33  176 58  95  193 615 922 1193    ...     ]
    [...]
    ...
    [...]]
    file_path: 数据文件
    gap: 参数减少倍数
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
        label.append(int(lines[-1]))
    f.close()

    # # 调整数据
    # fea = []
    # for i in feature:
    #     index = 0
    #     tmp = []
    #     while index < __total:
    #         tmp.append(sum(i[index : index + gap])/gap)
    #         index += gap
    #     fea.append(tmp)
    # print(len(fea[0]))

    return np.mat(feature), np.mat(label).T


def getThreshValuebyHistogram(img, weight, is_handle=True):
    """
    根据权重预测阈值
    """
    img = moveNoise(img, 7) # 去噪
    histogram = getHistogram(img) # 获得直方图
    if is_handle:
        histogram = np.mat(histogram)
        histogram = handleHistogram(histogram)
    mean_value = getMean(img)
    data = np.mat(histogram) # 转换为矩阵类型
    v = int((data * weight)[0, 0]) # 预测最佳阈值
    dummy_v = v
    # 对阈值进行判断, 去除漂移值
    if v > mean_value * 0.9:
        v = int(mean_value * 0.9)
    if v < mean_value * 0.35:
        v = int(mean_value * 0.35)
    print("prediction: %d, limited to: %d" % (dummy_v, v))
    return v


def getThreshValuebySoftmax(img, weight):
    """
    根据权重预测阈值
    weight: softmax训练获得
    """
    histogram = getHistogram(img, to_float=True) # 获得直方图
    histogram = np.mat(histogram)
    histogram = handleHistogram(histogram)
    mean_value = getMean(img)
    data = np.mat(histogram) # 转换为矩阵类型
    # print(np.shape(data), data)
    h = data * weight  # 预测最佳阈值
    v = h.argmax(axis=1)
    dummy_v = v
    # 对阈值进行判断, 去除漂移值
    # if v > mean_value * 0.9:
    #     v = int(mean_value * 0.9)
    # if v < mean_value * 0.7:
    #     v = int(mean_value * 0.7)
    print("prediction: %d, limited to: %d" % (dummy_v, v))
    return v


def handleHistogram(data, alpha=0.99, is_total=False):
    """
    对直方图进行数据归一化处理
    """
    m, n = np.shape(data)
    ret = np.zeros((m, n))
    for i in range(m):
        total = np.sum(data[i, :])
        max_value = np.max(data[i, :])
        for j in range(n):
            if is_total:
                ret[i, j] = data[i, j] / total * alpha
            else:
                ret[i, j] = [data[i, j], 1][data[i, j] == 0] / max_value * alpha
    return ret


def moveNoise(img, kernel_size):
    """
    二值处理前去除噪点
    """
    img_med = cv2.medianBlur(img, 5)
    kernel = np.zeros((7,7), np.uint8)
    thresh = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)
    return thresh


def getMean(img):
    """
    获得图像像素均值
    """
    img_w, img_h = np.shape(img)
    sums = 0
    for i in range(img_w):
        for j in range(img_h):
            sums += img[i][j]
    mean_value = sums // (img_w * img_h)

    return mean_value


def getCov(img, mean_value):
    """
    获得图像像素标准均方差
    """
    img_w, img_h = np.shape(img)
    sum_diff = 0
    for i in range(img_w):
        for j in range(img_h):
            diff = float((mean_value - img[i][j]) * (mean_value - img[i][j]))
            sum_diff += diff
    variance = int((sum_diff // (img_w * img_h))**0.5)

    return variance


def getHistogram(img, to_float=False):
    """
    获得图像直方图统计
    """
    img_w, img_h = np.shape(img)
    histogram = [0 for _ in range(256)]
    for i in range(img_w):
        for j in range(img_h):
            histogram[img[i][j]] += 1
    # 转为浮点数
    if to_float:
        ret = []
        for k,v in enumerate(histogram):
            ret.append(float(v))
        return ret

    return histogram


def saveImage(img_dirs, mid_name, image):
    """
    保存图像
    img_dirs:保存目录
    mid_name:新保存图片后缀
    image:图像
    """
    basename = os.path.basename(img_dirs)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    suffix = file[-1]
    image_file = os.path.join("\\".join(img_dirs.split("\\")[:-1]), file_prefix + mid_name + suffix)
    cv2.imwrite(image_file, image)



def maxRegionGrowing(img, thresh):
    """
    最大连通域进行分割
    Img: 待分割图
    thresh:二值图
    """
    # 最大连通区域
    print("finding maximum region...")
    m, n = thresh.shape
    visited = [[False for _ in range(n)] for _ in range(m)]

    max_area = 0 # 最大连通点个数
    max_visited = [] # 连通区域记录
    for i in range(m):
        for j in range(n):
            queue = []
            if visited[i][j] or thresh[i][j] == 0:
                continue
            else:
                tmp_area = 0
                tmp_visited = [[False for _ in range(n)] for _ in range(m)]
                queue.append([i, j])
                visited[i][j] = True
                tmp_visited[i][j] = True
                while len(queue) != 0:
                    row, col = queue.pop()
                    if row > 1 and not visited[row - 1][col] and thresh[row - 1][col] != 0:
                        queue.append([row - 1, col])
                        visited[row - 1][col] = True
                        tmp_visited[row - 1][col] = True
                        tmp_area += 1

                    # 往右搜索
                    if row + 1 < m and not visited[row + 1][col] and thresh[row + 1][col] != 0:
                        queue.append([row + 1, col])
                        visited[row + 1][col] = True
                        tmp_visited[row + 1][col] = True
                        tmp_area += 1

                    # 往上搜索
                    if col - 1 >= 0 and not visited[row][col - 1] and thresh[row][col - 1] != 0:
                        queue.append([row, col -1])
                        visited[row][col - 1] = True
                        tmp_visited[row][col - 1] = True
                        tmp_area += 1

                    # 往下搜搜
                    if col + 1 < n and not visited[row][col + 1] and thresh[row][col + 1] != 0:
                        queue.append([row, col + 1])
                        visited[row][col + 1] = True
                        tmp_visited[row][col + 1] = True
                        tmp_area += 1 

                if tmp_area > max_area:
                    max_visited = tmp_visited
                    max_area = tmp_area
    for i in range(m):
        for j in range(n):
            if not max_visited[i][j]:
                img[i][j] = 0
                thresh[i][j] = 0
    return img_new, thresh


def regionGrowing(img, thresh):
    """
    区域生长
    img: 待分割图
    thresh:二值图
    rtype: 分割图，分割图对应的二值图
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


def waterBfs(img, old_image):
    """
    获取最大轮廓后进行分割
    img: 轮廓
    old_image: 待分割图
    rtype: 分割图，分割图对应的二值图
    """
    row, col = img.shape
    # 得到rowxcol的矩阵[[False, False...], ..., [False, False...]]
    visited = [[False for _ in range(col)] for _ in range(row)] 
    queue = [] # 存放每一次遍历的起点
    def bfs(img, row, col, visited):
        m, n = img.shape
        queue.append([row, col])
        visited[row][col] = True 

        while len(queue) != 0:
            row, col = queue.pop()
            # print(len(queue))
            
            # 往左搜索
            if row >= 1 and not visited[row - 1][col] and img[row - 1][col] == 0:
                queue.append([row - 1, col])
                visited[row - 1][col] = True

            # 往右搜索
            if row + 1 < m and not visited[row + 1][col] and img[row + 1][col] == 0:
                queue.append([row + 1, col])
                visited[row + 1][col] = True

            # 往上搜索
            if col - 1 >= 0 and not visited[row][col - 1] and img[row][col - 1] == 0:
                queue.append([row, col -1])
                visited[row][col - 1] = True

            # 往下搜搜
            if col + 1 < n and not visited[row][col + 1] and img[row][col + 1] == 0:
                queue.append([row, col + 1])
                visited[row][col + 1] = True

    # 第一行与最后一行开始
    for c in range(col):
        if not visited[0][c] and img[0][c] == 0:
            bfs(img, 0, c, visited)
        if not visited[-1][c] and img[-1][c] == 0:
            bfs(img, row - 1, c, visited)


    for r in range(row):
        if not visited[r][0] and img[r][0] == 0:
            bfs(img, r, 0, visited)
        if not visited[r][-1] and img[r][-1] == 0:
            bfs(img, r, col - 1, visited)

    # 将模板二值化0,1
    for i in range(row):
        for j in range(col):
            if not visited[i][j]:
                img[i][j] = 1

    # 原图与模板相乘
    res = np.multiply(img, old_image)
    return res, img


def normalization(img):
    """
    归一化
    """
    h, w = np.shape(img)
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

    img_new = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR)

    return img_new


def printToConsole(start_time, f, count, total, gap):
    """
    打印信息
    """
    print("handled: ", f.split("\\")[-1])
    if count % gap == 0 and count != total:
        end_time = datetime.datetime.now()
        expend = end_time - start_time
        print("\nexpend time:", expend, "\nexpected time: ", expend / count * total, '\n')


def saveError(e, out_dir, f):
    """
    当出现错误时打印错误并保存未处理的图片到指定目录
    """
    print("Error: " + str(e))    
    failed_dir = os.path.join("\\".join(out_dir.split("\\")[:-1]), out_dir.split("\\")[-1] + "_failed")
    print("failed to handle %s, skiped.\nsaved in %s" % (f,failed_dir))
    if not os.path.isdir(failed_dir):
        os.mkdir(failed_dir)
    print(os.path.join(failed_dir, f.split("\\")[-1]))
    os.system("copy %s %s" % (f, os.path.join(failed_dir, f.split("\\")[-1])))


def moveMargin(img, threshed_img):
    """
    去除多余的边缘
    img:已经分割好的图片
    threshed_img:分割图片对应得二值图
    """
    img_w, img_h = np.shape(img)
    x, y, w, h = cv2.boundingRect(threshed_img)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20
    return img[y:y+h, x:x+w]


def maxContour(img, thresh):
    """
    获得最大轮廓
    返回分割后的图像和对应的二值图
    """
    img_w, img_h = img.shape
    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    # 找轮廓
    image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

    # 寻找最大轮廓
    max_contour = None
    max_area = 0
    noise = 0.8 * img_w * img_h # 可能会识别边界, 但这样处理后会导致返回值为None
    for c in contours:
        if cv2.contourArea(c) > max_area and cv2.contourArea(c) < noise:
            max_area = cv2.contourArea(c)
            max_contour = c

    img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 0,0), 1)
    res, img =  waterBfs(img_contour, img)
    threshed = np.multiply(img, thresh)
    return res, threshed


def maxEntrop(img):
    """
    根据信息熵获得最佳阈值
    img：灰度图像
    return : 最佳阈值
    """
    histogram = [0] * 256
    m, n = np.shape(img)

    max_entropy = -1
    threshed = 0
    total_pixel = m * n 
    # 计算阈值
    for i in range(m):
        for j in range(n):
            histogram[img[i, j]] += 1

    for i in range(256):
        # 计算Pt
        p_t = 0
        for x in range(i):
            p_t += histogram[x]

        # 计算背景熵
        H_B = 0
        for x in range(i):
            if histogram[x] != 0:
                pi_pt = histogram[x] / p_t
                if pi_pt <= 0: continue
                H_B += - pi_pt * np.log(pi_pt)

        # 计算物体熵
        H_O = 0
        for x in range(i, 256):
            if histogram[x] != 0:
                pi_1_pt = histogram[x] / (total_pixel - p_t)
                if pi_1_pt <= 0: continue
                H_O += - pi_1_pt * np.log(pi_1_pt)

        total_entrop = H_O + H_B
        if total_entrop > max_entropy:
            max_entropy = total_entrop
            threshed  = i 

    return threshed


def rotation(res):
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


def grabCut(img):
    """
    根据grabCut算法分割前景
    """
    mask = np.zeros(img.shape[:2],np.uint8) # mask
    h, w, _ =  img.shape

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (int(w * 0.1), int(h * 0.1), int(w * 0.9), int(h * 0.9))

    # print(rect)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis] # np.newaxis = None
    return img


def watershed(img):
    """
    使用分水岭进行图像分割
    """
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 4)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=4)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0
    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    return img


def plotScatter(data, labels, w, lim, save_name):
    """
    绘制散点图; 横坐标真实值，纵坐标预测值
    data : 数据
    labels:标签
    w:mat 权重
    lim:[(), ()] x,y轴范围
    save_name: 散点图保存名称
    """
    actual_x = [] # 绘制直线的x轴坐标
    predict_x = [] # 绘制预测值的x坐标
    for i in labels:
        actual_x.append(int(i[0]))
        predict_x.append(i[0])
    actual_y = actual_x # 直线的y坐标

    # 得到预测值
    predition = data * w
    predict_y = [] # 预测值的y坐标
    for i in predition:
        predict_y.append(i[0])
    color = np.arctan2(predict_y, predict_x)
    # 绘制散点图
    plt.scatter(predict_x, predict_y, s = 10, c="k", alpha = 1)
    # 设置坐标轴范围
    plt.xlim(lim[0])
    plt.ylim(lim[1])

    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(actual_x, actual_y, c="k")
    plt.savefig(save_name)
    plt.show()


##############################################
def getArea(pic_file):
    """
    a. 读取图片
    b. 计算分割后手掌像素点个数
    return: 总的面积，分割出来的图像像素点索引
    """
    # print("reading imgage...")
    img = cv2.imread(pic_file, 0)
    m, n = np.shape(img)
    area = 0
    index = np.mat(np.zeros((m, n)))
    for i in range(m):
        for j in range(n):
            if img[i][j] != 0:
                area += 1
                index[i, j] = 1

    return area, index


def getAccuracyRate(Rs, Ts):
    """
    分割精度
    Rs:手工勾画的分割图像的参考面积
    Ts:算法分割得到的图像的真实面积
    """
    SA = (1- abs(Rs - Ts) / Rs)
    return SA


def getErrorRate(Os, Rs):
    """
    过分割率
    Os:本不应该包含在分割结果中的像素点个数，实际却在分割结果中的像素点个数
    Rs:手工勾画的分割图像的参考面积
    """
    OR = (Os / (Rs + Os))
    return OR


def getLossRate(Us, Rs, Os):
    """
    欠分割率：在GT图像参考面积之中欠缺的像素点的比率
    Us: 本应该在分割结果中的像素点的个数，实际却不在分割结果中的像素点的个数
    """
    UR = (Us / (Rs + Os))
    return UR


def getErrorPoints(standard, actual):
    """
    计算本不应该包含在分割结果中的像素点个数，实际上却在分割结果中的像素点个数
    standard:标准分割像素点索引，矩阵
    actual: 实际分割像素点索引，矩阵
    """
    error_count = 0
    m, n = np.shape(standard)
    for i in range(m):
        for j in range(n):
            if standard[i, j] == 0 and actual[i, j] == 1:
                error_count += 1
    return error_count


def getSamePoints(standard, actual):
    """
    计算标准分割与实际分割的集合
    standard:标准分割像素点索引，矩阵
    actual: 实际分割像素点索引，矩阵
    """
    same_points = 0
    m, n = np.shape(standard)
    for i in range(m):
        for j in range(n):
            if standard[i, j] != 0 and standard[i, j] == actual[i, j]:
                same_points += 1
    return same_points


def getLossPoints(standard, actual):
    """
    计算本应该在分割结果中的像素点的个数，实际却不在分割结果中的像素点的个数
    standard:标准分割像素点索引，矩阵
    actual: 实际分割像素点索引，矩
    """
    loss_count = 0
    m, n = np.shape(standard)
    for i in range(m):
        for j in range(n):
            if standard[i, j] == 1 and actual[i, j] == 0:
                loss_count += 1
    return loss_count


def getAccuracy(standard_file, file_path):
    """
    standard_file:标准分割图像的路径
    file_path:使用不同方法得到的图片路径
    return: 分割精度，过分割率，欠分割率. dice
    """
    # print("get accuracy...")
    area, index = getArea(standard_file)
    area_new, index_new = getArea(file_path)
    same_points = getSamePoints(index, index_new)
    dice = 2 * same_points / (area + area_new)
    error_count = getErrorPoints(index, index_new)
    loss_count = getLossPoints(index, index_new)
    # 计算该方法下的分割精度，过分割率，欠分割率
    accuracy_rate = getAccuracyRate(area, area_new)
    error_rate = getErrorRate(error_count, area)
    loss_rate = getLossRate(loss_count, area, error_count)
    return accuracy_rate, error_rate, loss_rate, dice


def batchProcess(file_path_1, file_path_2):
    """
    file_path_1:标准分割图像路径
    file_path_2：使用不同方法分割后的图像路径
    要求： 两个目录下面的图像个数、名称要一一对应
    return : {"pic_1":[accuracy_rate, error_rate, loss_rate]}
    """
    start_time = datetime.datetime.now()
    files_1 = sorted(getFiles(file_path_1))
    files_2 = sorted(getFiles(file_path_2))
    len_files = len(files_1)
    res = {}
    # 逐一处理
    count = 1
    for i in range(len_files):
        # print("Process %d: %s"% (count, files_1[i]))
        
        accuracy_rate, error_rate, loss_rate, dice = getAccuracy(files_1[i], files_2[i])
        # print(files_2[i])
        basename = os.path.basename(files_1[i])
        pic_name = os.path.splitext(basename)[0]
        res[pic_name] = [accuracy_rate, error_rate, loss_rate, dice]
        printToConsole(start_time, files_1[i], count, len_files, 5)
        count += 1

    return res


def printEst(res, way):
    """
    打印分割评估结果
    res: {"pic_file_name":[accuracy_rate, error_rate, loss_rate]}
    way:所使用的方法 type:str
    """
    total_ac, total_err, total_loss, dice, count = 0, 0, 0, 0, 0
    for k, v in res.items():
        total_ac += v[0]
        total_err += v[1]
        total_loss += v[2]
        dice += v[3]
        count += 1
        print("picture: %s , accuracy rate: %5f , error rate:  %5f , loss rate: %5f, dice: %5f" % (k, v[0], v[1], v[2], v[3]))
    print("%s mean results, accuracy rate: %5f , error rate:  %5f , loss rate: %5f, dice: %5f" % (way, total_ac/count, total_err/count, total_loss/count, dice/count))


def saveEst(res, way, out_dir):
    """
    将结果保存至out_dir目录中，文件名为out_dir/way + '_results.txt'
    """
    print("saving results...")
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    file_name = os.path.join(out_dir, way + '_results.txt')
    f = open(file_name, 'w')
    out_puts = ""
    total_ac, total_err, total_loss, dice, count = 0, 0, 0, 0, 0
    for k, v in res.items():
        total_ac += v[0]
        total_err += v[1]
        total_loss += v[2]
        dice += v[3]
        count += 1
        out_puts += "picture: %s , accuracy rate: %5f , error rate:  %5f , loss rate: %5f, dice: %5f\n" % (k, v[0], v[1], v[2], v[3])
    out_puts += "%s mean results, accuracy rate: %5f , error rate:  %5f , loss rate: %5f, dice: %5f" % (way, total_ac/count, total_err/count, total_loss/count, dice/count)
    f.write(out_puts)
    f.close()


###################生成标签########################
def generateImageLable(dirs, data_dir, handle=True, preffix=True):
    """
    数据路径: C:/software/caffe/caffe-master/data/xunlian/val/m-10-10.4 (2).png
    dirs: 训练数据与测试数据目录，list类型 dirs = ["train", "val"]
    data_dir： 训练数据与测试数据所在目录路径
    handle： 是否处理m-10-10.4 (2).png 这样带"()"的文件名, 默认处理该文件并生成标签. 默认参数True,意思是可以不输入handle=True
    handle=False：跳过该文件不处理
    preffix=True : 添加所在目录val\m-10-10.4 (2).png, 默认参数True
    preffix=False : 不添加所在目录m-10-10.4 (2).png

    生成的标签分别保存在dirs中的目录下["train", "val"]即C:/software/caffe/caffe-master/data/xunlian/val/val.txt
    """
    count = 0
    for d in dirs:
        d_dir = os.path.join(data_dir, d)
        dir_pre = d + "/"

        file = os.path.join(d_dir, d + ".txt")
        d_file = open(file, "w")
        files = os.listdir(d_dir)
        
        for f in files:
            count += 1
            s = f.split("-")[-1]
            year = s.split(".png")[0]
            # print(s.split(".png")[0])
            if '(' in year:
                year = year.split(" ")[0]
                # print("重复: ", year)
                if not handle:
                    continue
            try:
                year = round(float(year))
                if preffix:
                    d_file.write("{0}{1} {2}\n".format(dir_pre, f, year))
                else:
                    d_file.write("{0} {1}\n".format(f, year))
            except:
                pass
            
        d_file.close()
    print("Successful total: " + str(count))


def delFileChar(file):
    """
    删除空格，将xx(s).jpg改为xx_s.jpg
    """
    count = 0
    for f in file:
        f_old = f
        f_new = f.replace(' ','')
        f_new = f_new.replace('(','_')
        f_new = f_new.replace(')','')
        if f_old != f_new:
            os.rename(f_old, f_new)
            count += 1
            print("Old filename: %s" % f_old)
            print("New filename: %s\n" % f_new)
    print("Successful,total %s files renamed." % count)



############################### BP神经网络 ##############################################
class neuralNetwork(object):
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        """
        初始化网络参数, 共三层网络
        """
        self.in_nodes = inputNodes
        self.hide_nodes = hiddenNodes
        self.out_nodes = outputNodes
        self.l_rate = learningRate

        # 将input层与hidden层权重用矩阵表示
        # 同理表示 hidden层与output层
        # pow(self.hide_nodes, -0.5) 标准方差为传入链接数目的开方
        # 矩阵规模： hidden x in 这样表示是因为 weight_in_hide x inputs 才能正确相乘
        self.weight_in_hide = numpy.random.normal(0.0, pow(self.hide_nodes, -0.5), (self.hide_nodes, self.in_nodes))
        self.weight_hide_out = numpy.random.normal(0.0, pow(self.out_nodes, -0.5), (self.out_nodes, self.hide_nodes))

        self.active_function = lambda x: (1/(1 + math.e**(-x))) # sigmoid函数

    def train(self, inputs_list, targets_list):
        """
        训练数据集
        """
        inputs = numpy.array(inputs_list, ndmin=2).T #转换为2d array并且转置. ndmin表示矩阵维度
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.weight_in_hide, inputs)
        hidden_outputs = self.active_function(hidden_inputs)

        final_inputs = numpy.dot(self.weight_hide_out, hidden_outputs)
        final_outputs = self.active_function(final_inputs)

        output_errors = (targets - final_outputs) # 期望差值
        hidden_error = numpy.dot(self.weight_hide_out.T, output_errors) # 误差反向传播

        # 根据误差修改各层权重
        self.weight_hide_out += self.l_rate * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.weight_in_hide += self.l_rate * numpy.dot((hidden_error * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))


    def test(self, inputs_lists):
        """
        测试
        """
        inputs = numpy.array(inputs_lists, ndmin=2).T

        hidden_inputs = numpy.dot(self.weight_in_hide, inputs)
        hidden_outputs = self.active_function(hidden_inputs)

        final_inputs = numpy.dot(self.weight_hide_out, hidden_outputs)
        final_outputs = self.active_function(final_inputs)

        return final_outputs


def getHistogramMean(data):
    """
    根据直方图获得该图像的平均像素
    rtype: float, 平均像素
    """
    total_pixel = 0
    total = 0
    m, n = np.shape(data)
    count = 0
    for i in range(m):
        for j in range(n):
            total_pixel += count * int(data[i, j])
            total += int(data[i, j])
            count += 1
    return total_pixel / total


def standardPicClip(dir_path, out_dir, clip=(45,-45,45,-45)):
    """
    对图像进行切边
    dir_path：原图路径
    out_dir：切边后保存目录
    """
    files = getFiles(dir_path)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    for f in files:
        img = cv2.imread(f, 0)
        out_path = os.path.join(out_dir, f.split("\\")[-1])
        x,w,y,h = clip
        img = img[x:w , y:h]
        saveImage(out_path, "_new", img)
    os.startfile(out_dir)


def skipChar(file_path, out_dir, skip_word='_new'):
    """
    跳过含有skip_word字符的文件
    file_path: 原文件目录
    out_dir:输出文件目录
    """
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = getFiles(file_path)
    for f in files:
        if "_new" in f.split("\\")[-1]:
            continue
        new_dirs = os.path.join(out_dir, f.split("\\")[-1])
        os.rename(f, new_dirs)
    os.startfile(out_dir)



def getPredictionErrorRate(data, labels, w0):
    """
    得到误差均值
    """
    predition = data * w0
    m, n = np.shape(predition)
    # print(m,n)
    # print(error)
    error_sum = 0
    for i in range(m):
        for j in range(n):
            # print(error[i, j])
            err = abs(int(predition[i, j]) - labels[i, j])
            print(err)
            error_sum = error_sum + err
    # print(error_sum)
    return error_sum / (m * n)



# def dataFilter(data, labels):
#     """
#     过滤数据中异常项
#     data:直方图
#     labels:最佳阈值
#     return: 过滤后的直方图数据，以及对应标签
#     """
#     m, n = np.shape(data)
#     ret_data = []
#     ret_lables = []
#     for i in range(m):
#         histogram_mean = getHistogramMean(data[i, :])
#         if abs(int(histogram_mean) - int(labels[i, 0])) < 40:
#             ret_data.append(data[i, : ])
#             ret_lables.append(labels[i, ])
#     # print(ret_lables, ret_data)
#     print(np.shape(ret_data))
#     return ret_data, ret_lables


def  loadWeights(file):
    """
    加载权重数据
    """
    w = []
    f = open(file)
    data = f.readlines()
    for line in data:
        line_data = line[:-1].split("\t")
        w_tmp = []
        for x in line_data:
            w_tmp.append(x)
        w.append(w_tmp)
    f.close()
    return np.mat(w)


def getDBSCANvalue(gray, f="SIFT"):
    gray_m, gray_n = np.shape(gray)

    # 去噪形态学处理
    thresh = gray.copy()
    kernel = np.zeros((7,7), np.uint8)
    for i in range(10):
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite("mroph_pic.png", thresh)

    # 训练DBSCAN
    def func(algorithm, par=None):
        algorithms = {
            "SIFT" : cv2.xfeatures2d.SIFT_create(),
            "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
            "ORB": cv2.ORB_create()
        }
        return algorithms[algorithm]
    alg = func(f)
    keypoints, descriptor = alg.detectAndCompute(gray, None)
    points2f = cv2.KeyPoint_convert(keypoints) 
    min_pts = 5
    eps = DBSCAN.epsilon(points2f, min_pts)
    types, sub_class = DBSCAN.dbscan(points2f, eps, min_pts)

    # 获得最大簇类
    cluster = {}
    sub_m, sub_n = np.shape(sub_class)
    for i in range(sub_m):
        for j in range(sub_n):
            cluster[sub_class[i, j]] = cluster.get(sub_class[i,j], 1) + sub_class[i,j]
    max_cluster_class,max_total = 0, 0
    for k,v in cluster.items():
        if v > max_total:
            max_cluster_class, max_total = k, v

    max_cluster = [] # 存储簇类的坐标
    # print("key_point: ", np.shape(points2f))
    for i in range(sub_m):
        for j in range(sub_n):
            # print(sub_class[i, j], max_cluster_class)
            if sub_class[i, j] == max_cluster_class:
                max_cluster.append([int(points2f[j, 0]), int(points2f[j, 1])])


    dummy = np.zeros(gray.shape)
    for i in max_cluster:
        # print(i[0], i[1])
        cv2.circle(dummy, tuple(i), 3, (255, 255, 255), 2) #33
    cv2.imwrite("cluster.png", dummy)


    # 根据特征点获得周围像素的值，半径为5
    points = []
    r = 5
    for x in max_cluster:
        i, j = x
        for m in range(i - r, i + r):
            for n in range(j - r, j + r):
                if [m, n] not in points:
                    points.append([m, n])

    max_total = len(points)
    pixel_value = []
    for x in points:
        if int(x[0]) >= gray_m or x[1] >= gray_n: continue
        if thresh[int(x[0]), int(x[1])] != 0:
            pixel_value.append(thresh[int(x[0]), int(x[1])])
    pixel_mean = sum(pixel_value) // max_total


    print("pixel_mean: ", pixel_mean, "total_pixel:", max_total)
    # vprint(sorted(pixel_value))
    dicts = {}
    for i in pixel_value:
        dicts[i] = dicts.get(i, 0) + 1

    # set_value = set(pixel_value)
    # least_value = sorted(pixel_value)[int(max_total*0)]
    print("dicts", dicts)
    max_k, max_v = 0, 0
    for k,v in dicts.items():
        if v > max_v:
            max_k = k
            max_v = v
    print("least_value:", max_k)

    return max_k


def saveModel(file_name, weights):
    '''
    保存最终的模型
    input:  file_name(string):保存的文件名
            weights(mat):softmax模型
    '''
    f_w = open(file_name, "w")
    m, n = np.shape(weights)
    for i in range(m):
        w_tmp = []
        for j in range(n):
            w_tmp.append(str(weights[i, j]))
        f_w.write("\t".join(w_tmp) + "\n")
    f_w.close()