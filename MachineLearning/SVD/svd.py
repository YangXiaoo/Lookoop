# coding:UTF-8
# 2018-11-2
# SVD
# https://www.cnblogs.com/pinard/p/6251584.html

import numpy as np 
def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i,k]) > thresh:
                print(1)
            else:
            	print(0)
        print('')


def imgCompress(numSV=3, thresh=0.8):
	"""
	使用SVD压缩图片
	"""
	img = []
	for line in open("0.txt").readlines():
		tmp = []
		for i in range(32):
			tmp.append(int(line[i]))
		img.append(tmp)
	img = np.mat(img)

	U, S, V = np.linalg.svd(img)
	S_re = np.mat(np.zeros((numSV, numSV)))
	for k in range(numSV):
		S_re[k, k] = S[k]
	re_mat = U[:, :numSV] * S_re * V[:numSV, :]
	print(re_mat)

if __name__ == '__main__':
	imgCompress()