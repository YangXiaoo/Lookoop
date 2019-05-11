# coding:utf-8
# 2019-5-9
# 根据切边信息裁剪图片
import os
import pickle
import cv2

import api
import util
import cropImgUsingCluster as crop


def cropImgUsingMarginInfo(marginInfoPath, imageDir, outputDir):
    """切边, 需保证待切边图片与marginInfo中的图片名称一致"""
    files = api.getFiles(imageDir)
    total = len(files)
    marginInfo = pickle.load(open(marginInfoPath,'rb'))
    util.mkdirs(outputDir)

    for i, f in enumerat  e(files):
        basename = os.path.basename(f)
        print("process {} / {}: {}".format(i+1, total, basename))

        img = cv2.imread(f, 0)

        if basename not in marginInfo:
            print("process {} / {}: {}, skip cause current pic name does not find in marginInfo".format(i+1, total, basename))
            continue

        margin = marginInfo[basename]
        retImg = crop.cropImage(img, margin)
        cv2.imwrite(os.path.join(outputDir, basename), retImg)


if __name__ == '__main__':
    marginInfoPath = "marginInfo.txt"
    imageDir = r"C:\Study\test\bone\100-original"
    outputDir = r"C:\Study\test\bone\100-original-newCrop"
    cropImgUsingMarginInfo(marginInfoPath, imageDir, outputDir)