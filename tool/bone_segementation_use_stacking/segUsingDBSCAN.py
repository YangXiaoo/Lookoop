# coding:utf-8
# 使用DBSCAN分割图像

import os
import numpy as np
import cv2
from sklearn.cluster import DBSCAN


from tool import util
from tool import api


def getMaxCluster(points, minPoints=5):
    """使用DBSAN获得最大聚类
    @param points 特征点
    @param minPoints 每个簇的最少点数
    @return 最大簇
    """
    db = DBSCAN(eps=200, min_samples=minPoints).fit(points)
    labels = db.labels_
    print(labels)
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print(n_clusters_)
    
    maxCluster = None
    maxCount = 0
    for i in range(n_clusters_):
        curCluster = points[labels == i]
        count = 0
        print(curCluster.shape)
        count = curCluster.shape[0] * curCluster.shape[1]
        if count > maxCount:
            maxCount = count
            maxCluster = curCluster

    print(len(maxCluster))
    return maxCluster


def getImageFromPoints(cluster, shape):
    """根据聚类点簇生成二值图"""
    mask = np.zeros(shape)
    for p in cluster:
        mask[p[0], p[1]] = 255

    return mask


def process(imageDir, outputDir):
    """使用DBSACN裁剪图片"""
    files = api.getFiles(imageDir)
    total = len(files)

    util.mkdirs(outputDir)


    for i, f in enumerate(files):
        basename = os.path.basename(f)
        print("process {} / {}: {}".format(i+1, total, basename))
        img = cv2.imread(f, 0)
        cluster = getMaxCluster(img, 40)

        retImg = getImageFromPoints(cluster, img.shape)

        # 保存裁剪结果
        imgSavePath = os.path.join(outputDir, basename)
        cv2.imwrite(imgSavePath, retImg)
        break

    os.startfile(outputDir)


if __name__ == '__main__':
    imageDir = r"C:\Study\test\bone\100-original"
    outputDir = r"C:\Study\test\bone\100-original-crop-dbscan"
    process(imageDir, outputDir)