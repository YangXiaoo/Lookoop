# coding:UTF-8
# 使用特征检测获得特征点，然后用聚类获得ROI, 并进行裁剪
import os
import pickle

import cv2
import numpy as np
import copy


import DBSCAN
import api
import util


# 定义切边补偿值
up = 100    # 由于手指上方缺失部分较多,所以定义为100
right = 100  # 右边补偿
left = 100   # 左边补偿

def getROIPoint(img, f="SIFT"):
    """使用SIFT,SURF,ORB获得特征点"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_m, gray_n = np.shape(gray)
    def func(algorithm, par=None):
        algorithms = {
            "SIFT" : cv2.xfeatures2d.SIFT_create(),
            "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
            "ORB": cv2.ORB_create()
        }
        return algorithms[algorithm]

    alg = func(f)
    keypoints, descriptor = alg.detectAndCompute(gray, None)
    points = cv2.KeyPoint_convert(keypoints) 

    return points


def getMaxCluster(points, minPoints=5):
    """使用DBSAN获得最大聚类
    @param points 特征点
    @param minPoints 每个簇的最少点数
    @return 最大簇
    """
    eps = DBSCAN.epsilon(points, minPoints)

    types, sub_class = DBSCAN.dbscan(points, eps, minPoints)

    # 统计每个簇类点的数量
    cluster = {}
    sub_m, sub_n = np.shape(sub_class)
    for i in range(sub_m):
        for j in range(sub_n):
            cluster[sub_class[i, j]] = cluster.get(sub_class[i,j], 1) + sub_class[i,j]


    # 找到点数最多的簇类
    max_cluster_class,max_total = 0, 0
    for k,v in cluster.items():
        if v > max_total:
            max_cluster_class, max_total = k, v

    max_cluster = [] # 存储簇类的坐标
    for i in range(sub_m):
        for j in range(sub_n):
            if sub_class[i, j] == max_cluster_class:
                max_cluster.append(points[j, :])

    return max_cluster


def savePointsImg(savePath, cluster, size):
    """保存特征点"""
    mask = np.zeros(size)
    for i in cluster:
        cv2.circle(mask, tuple(i), 3, (255, 255, 255), 2) # 33
    cv2.imwrite(savePath, mask)

    return None


def getMargin(cluster):
    """获得特征点的边界"""
    u, r, d, l = 9999, 0, 0, 9999
    for p in cluster:
        # height
        if p[1] < u:
            u = p[1]
        if p[1] > d:
            d = p[1]

        # width
        if p[0] < l:
            l = p[0]
        if p[0] > r:
            r = p[0]

    return [int(u), int(r), int(d), int(l)]


def cropImage(img, margin):
    """根据边界裁剪图片"""
    u, r, d, l = margin

    # img[0:u, :] = 0
    # img[d:-1, :] = 0
    # img[:, 0:l] = 0
    # img[:, r:-1] = 0

    return img[u:d, l:r]


def writeMarginInfo(outputPath, marginInfo):
    """记录裁剪信息
    @param outputPath 保存路径
    @param marginInfo dict 边界信息：{'fm-1-2.4_new.png': [287, 1011, 1621, 269]}
    """
    fp = open(outputPath, "wb")
    pickle.dump(marginInfo, fp)
    fp.close()

def moveMargin(img, margin):
    """去除图片边框"""
    x, w, y, h = margin

    return img[x:w, y:h]

def process(imageDir, outputDir):
    """使用DBSACN裁剪图片"""
    files = api.getFiles(imageDir)
    total = len(files)

    pointsDir = os.path.join(outputDir, "points")
    cluserDir = os.path.join(outputDir, "cluster")
    cropDir = os.path.join(outputDir, "crop")
    util.mkdirs([cluserDir, cropDir, pointsDir])

    marginInfo = {}
    for i, f in enumerate(files):
        basename = os.path.basename(f)
        print("[info] crop image, process {} / {}: {}".format(i+1, total, basename))
        img = cv2.imread(f)

        cropImg = moveMargin(img, (45,-45,45,-45))   # 删除边框特征

        maxMargin = None
        method = ["SIFT", "SURF", "ORB"]
        mergePoints = []
        for m in method:
            img = copy.deepcopy(cropImg)
            curpointsDir = os.path.join(pointsDir, m)
            curcluserDir = os.path.join(cluserDir, m)
            curcropDir = os.path.join(cropDir, m)
            util.mkdirs([curcluserDir, curcropDir, curpointsDir])


            points = getROIPoint(img, f=m)               # 获得ROI点

            # 保存ROI
            pointsSavePath = os.path.join(curpointsDir, basename)
            savePointsImg(pointsSavePath, points, img.shape)

            try:
                maxCluster = getMaxCluster(points, 40)  # 获得最大聚类
            except:
                print("[error] skip: {}".format(basename))
                continue
            mergePoints.extend(maxCluster)          # 融合特征点

            # 保存关键点图像
            clusterSavePath = os.path.join(curcluserDir, basename)
            savePointsImg(clusterSavePath, maxCluster, img.shape)

            margin = getMargin(maxCluster)  # 获得边界点u, r, d, l
            if not maxMargin:
                maxMargin = margin
            else:
                u, r, d, l = margin
                maxMargin[0] = min(maxMargin[0], u) 
                maxMargin[1] = max(maxMargin[1], r) 
                maxMargin[2] = max(maxMargin[2], d) 
                maxMargin[3] = min(maxMargin[3], l) 

            retImg = cropImage(img, margin) # 裁剪图片

            # 保存裁剪结果
            cropSavePath = os.path.join(curcropDir, basename)
            cv2.imwrite(cropSavePath, retImg)

        # 三种方法获得的最大边界
        w, h = img.shape[0], img.shape[1]
        if maxMargin[0] - up < 0:
            maxMargin[0] = 0
        else:
            maxMargin[0] -= up

        if maxMargin[1] + right > w:
            maxMargin[1] = w - 1
        else:
            maxMargin[1] += right
        # 图片下边缘不补偿
        if maxMargin[3] - left < 0:
            maxMargin[3] = 0
        else:
            maxMargin[3] -= left

        marginInfo[basename] = maxMargin    # 记录切边信息
        retImg = cropImage(img, maxMargin)  # 裁剪图片

        # 保存不同特征点融合图像
        mergeSavePath = os.path.join(pointsDir, "mergePoints_{}".format(basename))
        savePointsImg(mergeSavePath, mergePoints, img.shape)

        # 保存裁剪结果
        cropSavePath = os.path.join(cropDir, basename)
        cv2.imwrite(cropSavePath, retImg)

        # if i == 5: assert False, 'break'

    writeMarginInfo(os.path.join(outputDir, "marginInfo.txt"), marginInfo)   # 保存到结果目录

    os.startfile(outputDir)


if __name__ == '__main__':
    imageDir = r"C:\Study\test\bone\100-gt"
    outputDir = r"C:\Study\test\bone\gt-crop-test-results-01"

    process(imageDir, outputDir)
