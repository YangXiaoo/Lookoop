# 2018-9-10
# 检测器
import cv2
import numpy as np
import os
# 1. 取一个数据样本
# 2. 创建BOW训练容器，提前需要检测器与匹配器
# 3. 创建BOW类
# 4. 对数据集中的每幅图像提取描述符(SIFT, SURF)
# 5. 将每个描述符都添加到BOW训练器中
# 6. 将描述符聚类到k簇中(从可视化角度来看，K-means就是这个簇中点的几何中心)
# 7. 基于训练容器得到BOW词袋 
# 8. 创建SVM并基于BOW词袋训练SVM
def get_flann_matrcher(alg=1, trs=5):
	"""
	FLANN特征检测
	"""
	flann = dict(algorithm = alg, tress = trs)
	return cv2.FlannBasedMatcher(flann, {}) # {checks = 50}


def get_extract_detect():
	"""
	获取特抽取和检测方法
	"""
	return cv2.xfeatures2d.SIFT_create(), cv2.xfeatures2d.SIFT_create()


def get_bow(size, extract, matcher):
	"""
	size: 训练容器大小
	extract: 特征检测方法
	matcher : 特征匹配方法
	创建BOW训练容器，BOW方法
	"""
	return cv2.BOWKMeansTrainer(size), cv2.BOWImgDescriptorExtractor(extract, matcher)


def extract_feature(image_path, extractor, detector):
	"""
	获取图像特征，并返回特征描述符
	"""
	img = cv2.imread(image_path, 0) 
	return extractor.compute(img, detector.detect(img))[1]


def bow_feature(img, extractor_bow, detector):
	"""
	根绝BOW获得图像描述符
	extractor_bow: 词袋方法
	detector: 特征检测方法
	"""
	return extractor_bow.compute(img, detector.detect(img))


def get_picture(data_path):
	"""
	得到训练数据
	"""
	data = []
	suffix = ["bmp","jpg","png","tif","pcx","tga","exif","fpx","svg","psd","jpeg ","pcd","dxf","ufo","eps","ai","raw","WMF","webp", "pgm"]
	for root, dirs, files in os.walk(data_path):
		for i in files:
			suf = i.split(".")[-1]
			if suf.lower() not in suffix:
				continue
			path = os.path.join(root, i)
			data.append(path)

	return data


def car_detector(data_path, data_path2, simple_size, label):
	# n = 12
	# s = n.zfill(5) # "00012"

	# 得到特征检测器
	detector, extractor = get_extract_detect()
	# 得到特征篇匹配器
	matcher = get_flann_matrcher()

	# 获得训练容器与BOW
	bow_kmeans_trainer, extract_bow = get_bow(12, extractor, matcher)

	print("Extracting features...")
	data = get_picture(data_path)
	dummy = get_picture(data_path2)
	for i in range(simple_size):
		print("Extract features from %s" % data[i])
		# 提取图片特征加入到训练容器
		bow_kmeans_trainer.add(extract_feature(data[i], extractor, detector))

	print("Computing k-mean...")
	# 得到簇类均值
	voc = bow_kmeans_trainer.cluster()
	# 得到BOW 
	extract_bow.setVocabulary(voc)

	print("Adding to train data...")
	traindata = [] # 数据集
	trainlabels = [] # 标签集
	for i in range(simple_size):
		print("Add  %s" % data[i])
		img = cv2.imread(data[i], 0)
		# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		traindata.extend(bow_feature(img, extract_bow, detector))
		trainlabels.append(1)
		print("Add  %s" % dummy[i])
		img2 = cv2.imread(dummy[i], 0)
		traindata.extend(bow_feature(img2, extract_bow, detector))
		trainlabels.append(-1)
	# if os.path.isfile("svm.xml"):
	# 	return "svm.xml", extract_bow, True
	svm = cv2.ml.SVM_create()
	svm.setType(cv2.ml.SVM_C_SVC)
	svm.setGamma(1)
	svm.setC(35)
	svm.setKernel(cv2.ml.SVM_RBF)

	print("Training svm...")
	svm.train(np.array(traindata), cv2.ml.ROW_SAMPLE, np.array(trainlabels))

	try:
	 	svm.save("svm.xml")
	except:
		print("fail save")

	return svm, extract_bow, False

	