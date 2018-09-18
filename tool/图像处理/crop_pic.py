# 2018-9-18
# 轮廓检测并裁剪图片
# import numpy as np
# import matplotlib.pyplot as plt
import os
import cv2


__suffix = ["png", "jpg"]

def file(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
            	file.append(path)
    return file

def main(dirs, out_dir):
	if not os.path.isdir(out_dir):
		os.mkdir(out_dir)
	files = file(dirs)

	for f in files:
		print(f)
		img = cv2.imread(f)
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		image, contours, hier = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		max_contour = None
		max_area = 0
		for c in contours:
			if cv2.contourArea(c) > max_area:
				max_area = cv2.contourArea(c)
				max_contour = c

		x, y, w, h = cv2.boundingRect(max_contour)
		x -= 10
		y -= 10
		w += 20
		h += 20
		img_new = img_gray[y:y+h, x:x+w]
		# print(img_new)
		# 灰度图像保存
		save_path = os.path.join(out_dir, f.split("\\")[-1])
		cv2.imwrite(save_path, img_new)


if __name__ == '__main__':
	dirs = "C:\\Study\\test\\image" 
	out_dir = "C:\\Study\\test\\out_pic" # 存储路径
	main(dirs, out_dir)