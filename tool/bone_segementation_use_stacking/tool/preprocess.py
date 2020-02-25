# coding:utf-8
import os 
import math

import cv2
import numpy as np

import api
import util
from cropImgUsingCluster import process as crop


def PmDenoise(img, k=5, lmb=0.15, iter=10):
	"""去噪
	@param img 图片矩阵
	"""
	m, n = img.shape
	imgMask = np.zeros((m, n))
	for i in range(iter):
		print("[info] pm denoise processing, iter: {} / {}".format(i+1, iter))
		for p in range(2, m-1):
			for q in range(2, n-1):
				ni = img[p-1, q] - img[p, q]
				si = img[p+1, q] - img[p, q]
				ei = img[p, q-1] - img[p, q]
				wi = img[p, q+1] - img[p, q]

				# cn = round(math.exp(-(ni**2) / (k**2)), 4)
				# cs = round(math.exp(-(si**2) / (k**2)), 4)
				# ce = round(math.exp(-(ei**2) / (k**2)), 4)
				# cw = round(math.exp(-(wi**2) / (k**2)), 4)
				# imgMask[p, q] = round(img[p, q] + lmb*(cn*ni + cs*si + ce*ei + cw*wi), 4)

				cn = math.exp(-(ni**2) / (k**2))
				cs = math.exp(-(si**2) / (k**2))
				ce = math.exp(-(ei**2) / (k**2))
				cw = math.exp(-(wi**2) / (k**2))

				imgMask[p, q] = img[p, q] + lmb*(cn*ni + cs*si + ce*ei + cw*wi)
		img = imgMask

	return imgMask


def CLAHE(img):
	"""增强"""
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

	return clahe.apply(img)

def sizeNormalization(img):
	"""尺寸归一化"""
	pass

def testPM():
	imageDir = r"C:\Study\test\bone\pic-test"
	outputDir = r"C:\Study\test\bone\pm-results"
	util.mkdirs(outputDir)

	picFiles = api.getFiles(imageDir)
	total = len(picFiles)
	for it, file in enumerate(picFiles):
		print("[info] process {} / {}.".format(it+1, total))
		img = cv2.imread(file, 0)
		retPic = PmDenoise(img, iter=2)
		savePath = os.path.join(outputDir, os.path.basename(file))
		# print(savePath)
		cv2.imwrite(savePath, retPic)

def main():
	imageDir = r"C:\Study\test\bone\pic-test"
	pmSavingDir = r"C:\Study\test\bone\preprocess\pm-results"
	claheSavingDir = r"C:\Study\test\bone\preprocess\clahe-results"
	cropSavigDir = r"C:\Study\test\bone\preprocess\crop-results"
	util.mkdirs([pmSavingDir, claheSavingDir, cropSavigDir])

	picFiles = api.getFiles(imageDir)
	total = len(picFiles)

	for i, f in enumerate(picFiles):
		imgFileName = os.path.basename(f)
		print("[info] process {} / {}, img: {}".format(i+1, total, imgFileName))
		img = cv2.imread(f, 0)

		# # 去噪
		denoiseImg = PmDenoise(img)
		denoiseSavingPath = os.path.join(pmSavingDir, imgFileName)
		cv2.imwrite(denoiseSavingPath, denoiseImg)

		# 增强
		denoiseImg = cv2.imread(denoiseSavingPath, cv2.IMREAD_GRAYSCALE)
		claheImg = CLAHE(denoiseImg)
		cv2.imwrite(os.path.join(claheSavingDir, imgFileName), claheImg)

	# 为方便函数调用，最后统一裁剪
	crop(claheSavingDir, cropSavigDir)

if __name__ == '__main__':
	# testPM()
	main()
    

