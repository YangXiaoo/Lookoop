# coding:utf-8
# 2019-1-15

import numpy
import os


def mkdirs(file_list):
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 

def get_checkpoint(train_dir):
	file_list = os.listdir(train_dir)
	least_f, max_iter = '', 0
	for f in file_list:
		if '.meta' in f:
			tmp_iter = int(f.split('-')[-1].split('.')[0])
			if tmp_iter > max_iter:
				least_f = f

	ret = os.path.join(train_dir, least_f)

	return ret



def get_files(dirpath, suffix=["png"]):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in suffix:
                file.append(path)
    return file
	

