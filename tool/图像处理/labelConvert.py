# coding:utf-8
# 将分割灰度图转换为二值图
# 2019-4-18

import os
import cv2
import numpy as np 

from collections import deque
from copy import deepcopy


SUFFIX = ["tif", "png"] # 图片后缀

def mkdirs(fileList):
    """创建目录"""
    if isinstance(fileList, list):
        for f in fileList:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(fileList):
            os.makedirs(fileList)
    return None

def getFiles(dirpath):
    """获取文件"""
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in SUFFIX:
                file.append(path)
    return file


def convertHelper(imgGray):
    """转换为二值图
    @param imgGray 灰度图
    @return img 二值图
    """
    img = deepcopy(imgGray)
    h, w = np.shape(img)
    mask = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append([0, 0])
    while len(queue):
        size = len(queue)
        for _ in range(size):
            row, col = queue.pop()
            if row >= 1 and not mask[row - 1][col] and img[row - 1][col] == 0:
                queue.appendleft([row - 1, col])
                mask[row - 1][col] = True
            if row + 1 < h and not mask[row + 1][col] and img[row + 1][col] == 0:
                queue.appendleft([row + 1, col])
                mask[row + 1][col] = True
            if col - 1 >= 0 and not mask[row][col - 1] and img[row][col - 1] == 0:
                queue.appendleft([row, col -1])
                mask[row][col - 1] = True
            if col + 1 < w and not mask[row][col + 1] and img[row][col + 1] == 0:
                queue.appendleft([row, col + 1])
                mask[row][col + 1] = True
    # print(mask)
    count = 0
    for i in range(h):
        for j in range(w):
            if not mask[i][j]:
                imgGray[i][j] = 255 # 错误：256
                count += 1

    return imgGray


def normlization(img, img_size=(512, 512)):
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

    img_new = cv2.resize(img, img_size, interpolation=cv2.INTER_LINEAR)
    return img_new


def convert(picDir, outDir, norm=True, size=(512, 512)):
    """转换入口函数
    @param picPath 图片路径
    @param outDir 保存路径
    @param norm 归一化
    @param size 归一化尺寸
    """
    mkdirs(outDir)
    files = sorted(getFiles(picDir))

    for i, f in enumerate(files):
        basename = os.path.basename(f)
        outPath = os.path.join(outDir, str(i) + "." + basename.split('.')[-1])
        print("[INFO] processing {}".format(basename))
        imgGray = cv2.imread(f, 0)
        imgNew = convertHelper(imgGray)
        if norm:
            imgNew = normlization(imgNew, size)
        cv2.imwrite(outPath, imgNew)

    os.startfile(outDir)


if __name__ == '__main__':
    picDir = r"C:\Study\test\bone\100-gt"
    outDir = r"C:\Study\test\bone\100-gt-convert"
    norm = True
    size = (512, 512)
    convert(picDir, outDir, norm=norm, size=size)
