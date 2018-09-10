# 2018-9-10
import numpy as np
import os
import cv2
from func import *
from detector import *

def main(test_image, data_path, data_path2, simple_size, label):
	svm, extractor, exist = car_detector(data_path, data_path2, simple_size, label)
	# if exist:
	# 	svms = cv2.ml.SVM_create()
	# 	svms.load(svm)
	# 	svm = svms

	detector = cv2.xfeatures2d.SIFT_create()


	img = cv2.imread(test_image)
	w , h, d = img.shape
	w, h = w//2, h//4
	rectangles = [] # 记录标识结果的矩形数据
	counter = 1
	scale_factor = 1.25 # 金字塔缩小比例
	scale = 1 # 记录缩小比例
	step = 20

	print("Starting test...")
	for resized in pyramid(img, scale_factor):
		scale = float(img.shape[1]) / float(resized.shape[1])

		for x,y,roi in slidingWindow(resized, step, (w, h)):
			print("pyraid layer: %d" % counter)
			if roi.shape[1] != w or roi.shape[0] != h:
				continue
			try:
				bf = bow_feature(roi, extractor, detector)
				_, result = svm.predict(bf)
				a, res = svm.predict(bf, flags=cv2.ml.STAT_MODEL_RAW_OUTPUT | cv2.ml.STAT_MODEL_UPDATE_MODEL)
				print("Class %d, Score: %f, a: %s" % (result[0][0], res[0][0], res))
				score = res[0][0]
				if result[0][0] == 1:
					# 所有小于-1.0的窗口被认为是好的窗口
					if score < -1.0:
						# 根据比例值scale获得矩形坐标
						rx, ry, rw, rh = int(x * scale), int(y * scale), int((x + w) * sacle), int((y + h) * scale)
						rectangles.append([rx, ry, rw, rh, abs(score)])
			except:
				pass
			counter += 1


	label_window = np.array(rectangles)

	# 非最大抑制。
	# 图像中可能包含被检测多次的对象, 若将这些检测作为结果则不准确, 这时需要采取非最大抑制来解决。
	boxes = nonMaxSuppressionFast(label_window, 0.25)

	print("boxes: ", boxes)
	for x, y, w, h, score in boxes:
		cv2.rectangle(img, x, y, w, h, (0, 255, 0), 2)
		cv2.putText(img, "%f" % score, x, y, 2, 1, (0, 255, 0))

	cv2.imshow("test result", img)
	cv2.waitKey()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	test_image = "C:\\Study\\ImageHandle\\data\\cars_test\\00248.jpg"#  "C:\\Study\\ImageHandle\\data\\CarData\\TestImages\\test-161.pgm" # "C:\\Study\\ImageHandle\\data\\cars_test\\00248.jpg"
	data_path = "C:\\Study\\ImageHandle\\data\\cars_test"  # "C:\\Study\\ImageHandle\\data\\CarData\\TrainImages" # "C:\\Study\\ImageHandle\\data\\cars_test"
	data_path2 = "C:\\Study\\ImageHandle\\re\\train\\3"
	simple_size = 10
	label = 1
	main(test_image, data_path, data_path2, simple_size, label)
