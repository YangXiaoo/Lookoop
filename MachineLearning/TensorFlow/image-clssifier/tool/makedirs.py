# coding:UTF-8
# 2018-12-24
# 将图片整理成标准格式：
# From:
# m-1-0.4.png
# m-1-1.3.png 
# ...
# To:
# xxx
# │  ├─0/m-1-0.4.png
# │  ├─1/m-1-1.3.png 
# │  ├─.../...
# │  ├─18/...

import os
import cv2

__suffix = ["png", "jpg"]

def get_files(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def make_dir(input_dir, output_dir, size=(224, 224)):
	files = get_files(input_dir)
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
	for f in files:
		print(f)
		dir_name = str(int(round(float(os.path.splitext(os.path.basename(f))[0].split('(')[0].split('-')[-1]))))
		cur_f_dir = os.path.join(output_dir, dir_name)
		if not os.path.isdir(cur_f_dir):
			os.mkdir(cur_f_dir)

		# 原图不是RGB
		# os.system("copy %s %s" % (f, os.path.join(cur_f_dir, f.split("\\")[-1])))
		# 转换为RGB
		img = cv2.imread(f)
		img = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		cv2.imwrite(os.path.join(cur_f_dir, f.split("\\")[-1]), img)

	print("total: %d" % len(files))
	os.startfile(output_dir)


if __name__ == '__main__':
	input_dir = "C:\\Study\\test\\male\\male\\V-male"
	output_dir = "C:\\Study\\test\\male\\male\\validation"
	make_dir(input_dir, output_dir)


