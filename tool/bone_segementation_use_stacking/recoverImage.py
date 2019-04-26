# coding:utf-8
# 2019-4-20
"""根据二值分割将原图进行分割
解决原因：对图像进行分割前对原图进行了增强处理，进行分割时是对增强图片进行分割，而不是基于原图分割。
		现在根据对增强图片进行分割保存的二值图对原图进行分割，保存原图的分割图。
"""

import numpy as np
import os
import cv2

from tool import util
from tool import api


def getImageDict(originalFiles, binaryFiles):
	"""获得原图对应的分割图路径
	@param originalFiles 原图文件路径列表
	@param binaryFiles 二值文件列表
	@returns dict {"originalPicName":"binaryImagePath"}
	"""
	ret = {}
	for f in originalFiles:
		originalPicName = os.path.basename(f)
		for binaryImagePath in binaryFiles:
			picName = os.path.basename(binaryImagePath)
			preffix = os.path.splitext(originalPicName)[0] # 原图文件名前缀
			"""将匹配的文件添加到字典"""
			if preffix in picName:	
				ret[originalPicName] = binaryImagePath

	return ret


def segBasedBinaryImage(originalIamgePath, binaryImagePath):
	"""使用二值图对原图进行分割"""
	originalIamge = cv2.imread(originalIamgePath, 0)
	binaryImage = cv2.imread(binaryImagePath, 0)
	if np.shape(originalIamge) != np.shape(binaryImage):
		print("[WARNING] original iamge size does not equal bianry image size!")
		return 
	h,w = np.shape(binaryImage)
	for i in range(h):
		for j in range(w):
			if binaryImage[i][j] == 0:
				originalIamge[i][j] = 0

	return originalIamge


def imagePattern(binaryFiles, imageNamepattern):
	"""匹配图片文件名
	@param binaryFiles 带匹配文件路径列表
	@param imageNamePattern 匹配字符串
	@returns list 文件路径列表
	"""
	ret = []
	for f in binaryFiles:
		basename = os.path.basename(f)
		if imageNamepattern in basename:
			ret.append(f)
	return ret


def recover(originalIamgeDir, binaryIamgeDir, outputDir, imageNamepattern):
	"""入口函数,前提条件为原图与二值图大小相同
	不相同的话需要进行切边，切边函数见api.standardPicClip
	@param OriginalIamgeDir 原图目录
	@param binaryIamgeDir 二值图目录
	@param outputDir 保存路径
	@param imageNamepattern 二值图匹配字符
	@returns None
	"""
	originalFiles = api.getFiles(originalIamgeDir)
	rawbinaryFiles = api.getFiles(binaryIamgeDir)
	binaryFiles = imagePattern(rawbinaryFiles, imageNamepattern)
	binaryImageDict = getImageDict(originalFiles, binaryFiles)

	util.mkdirs(outputDir)
	failed = []

	for f in originalFiles:
		originalPicName = os.path.basename(f)				# 原图文件名
		print("[INFO] processing {}".format(originalPicName))
		binaryImagePath = binaryImageDict.get(originalPicName, None)	# 获得二值图路径
		if not binaryImagePath:
			print("[WARNING] image {} dose not map in {}".format(originalPicName, binaryIamgeDir))
			failed.append(originalPicName)
			continue

		segImage = segBasedBinaryImage(f, binaryImagePath)		# 获得分割图

		outputPath = os.path.join(outputDir, originalPicName)	# 获得保存图像路径
		cv2.imwrite(outputPath, segImage)

	print("[WARNING] failed to recover: {}".format(failed))

if __name__ == '__main__':
	original = r"C:\Study\test\bone\cc\cc\old"				# 未切边的原图目录
	originalIamgeDir = r"C:\Study\test\bone\cc\cc\old_clip"	# 切边后原图目录
	binaryIamgeDir = r"C:\Study\test\bone\cc\cc\new"		# 二值图所在目录
	outputDir = r"C:\Study\test\bone\cc\ret"				# 保存路径
	imageNamepattern = "_thrshed_img_seg"					# 二值图匹配字符串

	# 切边
	api.standardPicClip(original, originalIamgeDir, midName="")


	recover(originalIamgeDir, binaryIamgeDir, outputDir, imageNamepattern)




