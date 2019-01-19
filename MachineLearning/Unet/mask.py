# coding:utf-8
# 2019-1-19
# mask

import os
import cv2
import numpy as np

from data_factory import *


def preprocessing(img):
	"""
	读预处理图像进行处理
	使用聚类, 阈值判断, 最大连通区域
	Args:
		img : type(mat or array),image
	Returns:
		img : type(mat or array),image
	"""
	threshed = 1
	img[img > threshed] = 1
	img[img < threshed] = 0

	return img


def mian(original_pic_dir,
		prediction_pic_dir,
		output_dir,
		img_size=224):
	"""
	使用预测的结果对原图像进行处理

	Args:
		original_pic_dir : 经过归一化后原图像路径
		prediction_pic_dir ： 由unet预测保存的图像路径
		output_dir ： 保存图像路径
		img_size : 输出图像尺寸

	Retures: None
	"""
	# original_pic = get_files(original_pic_path)
	# original_pic = get_files(original_pic_path)

	pic_name_list = os.listdir(original_pic_dir)

	for k,f in enumerate(pic_name_list):
		print("[INFO] processing %s" % f)
		original_pic_path = os.path.join(original_pic_dir, f)
		prediction_pic_path = os.path.join(prediction_pic_dir, f)

		original_img = cv2.imread(original_pic_path)
		prediction_img = cv2.imread(prediction_pic_path)

		prediction_img = preprocessing(prediction_img) # 暂时未完成

		new_img = np.multiply(original_img, prediction_img)

		new_img_path = os.path.join(output_dir, f)
		cv2.imwrite(new_img_path, new_img)


		# test
		# if k == 10:
		# 	break




if __name__ == '__main__':
	original_pic_dir = r'C:\Study\test\unet\100-test_norm'
	prediction_pic_dir = r'C:\Study\test\unet\image_prediction_test'
	output_dir = r'C:\Study\test\unet\image_result'
	img_size = 224

	mkdir(output_dir)

	mian(original_pic_dir,
		prediction_pic_dir,
		output_dir,
		img_size)