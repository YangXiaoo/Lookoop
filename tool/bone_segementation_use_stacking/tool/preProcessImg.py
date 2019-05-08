# coding:UTF-8
# 使用特征检测获得特征点，然后用聚类获得ROI, 并进行裁剪
import os

import cv2
import numpy as np


import DBSCAN
import api
import util


def getROIPoint(img, f="SIFT"):
	"""使用SIFT,SURF,ORB获得拐点"""
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
	"""使用DBSAN获得最大聚类"""
	eps = DBSCAN.epsilon(points, minPoints)
	# print(eps)

	types, sub_class = DBSCAN.dbscan(points, eps, minPoints)
	cluster = {}
	# print(np.shape(sub_class))
	sub_m, sub_n = np.shape(sub_class)
	for i in range(sub_m):
		for j in range(sub_n):
			cluster[sub_class[i, j]] = cluster.get(sub_class[i,j], 1) + sub_class[i,j]
	# print(cluster)
	max_cluster_class,max_total = 0, 0
	for k,v in cluster.items():
		if v > max_total:
			max_cluster_class, max_total = k, v

	max_cluster = [] # 存储簇类的坐标
	# print("key_point: ", np.shape(points))
	for i in range(sub_m):
		for j in range(sub_n):
			# print(sub_class[i, j], max_cluster_class)
			if sub_class[i, j] == max_cluster_class:
				max_cluster.append(points[j, :])

	return max_cluster


def savePointsImg(savePath, cluster, size):
	"""保存散点"""
	mask = np.zeros(size)
	for i in cluster:
		cv2.circle(mask, tuple(i), 3, (255, 255, 255), 2) # 33
	cv2.imwrite(savePath, mask)

	return None


def getMargin(cluster):
	"""获得散点的边界"""
	u, r, d, l = 9999, 0, 0, 9999
	for p in cluster:
		if p[1] < u:
			u = p[1]
		if p[1] > d:
			d = p[1]

		if p[0] < l:
			l = p[0]
		if p[0] > r:
			r = p[0]

	return [int(u), int(r), int(d), int(l)]


def cropImage(img, margin):
	"""根据边界裁剪图片"""
	u, r, d, l = margin

	return img[u:d, l:r]


def process(imageDir, outputDir):
	"""使用DBSACN裁剪图片"""
	files = api.getFiles(imageDir)
	total = len(files)

	pointsDir = os.path.join(outputDir, "points")
	cluserDir = os.path.join(outputDir, "cluster")
	cropDir = os.path.join(outputDir, "crop")
	util.mkdirs([cluserDir, cropDir, pointsDir])

	for i, f in enumerate(files):
		if i < 10:
			continue
		basename = os.path.basename(f)
		print("process {} / {}: {}".format(i+1, total, basename))
		img = cv2.imread(f)

		maxMargin = None
		method = ["SIFT", "SURF", "ORB"]
		for m in method:

			curpointsDir = os.path.join(pointsDir, m)
			curcluserDir = os.path.join(cluserDir, m)
			curcropDir = os.path.join(cropDir, m)
			util.mkdirs([curcluserDir, curcropDir, curpointsDir])


			points = getROIPoint(img)				# 获得ROI点

			# 保存ROI
			pointsSavePath = os.path.join(curpointsDir, basename)
			savePointsImg(pointsSavePath, points, img.shape)


			maxCluster = getMaxCluster(points, 40)	# 获得最大聚类

			# 保存关键点图像
			clusterSavePath = os.path.join(curcluserDir, basename)
			savePointsImg(clusterSavePath, maxCluster, img.shape)

			margin = getMargin(maxCluster)	# 获得边界点u, r, d, l
			if not maxMargin:
				maxMargin = margin
			else:
				u, r, d, l = margin
				maxMargin[0] = min(maxMargin[0], u) 
				maxMargin[1] = max(maxMargin[1], r) 
				maxMargin[2] = max(maxMargin[2], d) 
				maxMargin[3] = min(maxMargin[3], l) 

			retImg = cropImage(img, margin)	# 裁剪图片

			# 保存裁剪结果
			cropSavePath = os.path.join(curcropDir, basename)
			cv2.imwrite(cropSavePath, retImg)

		# 三种方法获得的最大边界
		h, w = img.shape[0], img.shape[1]
		print
		if maxMargin[0] - 50 < 0:
			maxMargin[0] = 0
		else:
			maxMargin[0] -= 50

		if maxMargin[1] + 50 > w:
			maxMargin[1] = w - 1
		else:
			maxMargin[1] += 50

		if maxMargin[3] - 50 < 0:
			maxMargin[3] = 0
		else:
			maxMargin[3] -= 50

		retImg = cropImage(img, maxMargin)	# 裁剪图片
		# 保存裁剪结果
		cropSavePath = os.path.join(cropDir, basename)
		cv2.imwrite(cropSavePath, retImg)




# dummy = np.zeros(gray.shape)
# for i in points:
# 	# print(i[0], i[1])
# 	cv2.circle(dummy, tuple(i), 2, (51, 163, 236), 1) #33

if __name__ == '__main__':
	imageDir = r"C:\Study\test\bone\100-original"
	outputDir = r"C:\Study\test\bone\100-original-crop"

	process(imageDir, outputDir)


 n m  