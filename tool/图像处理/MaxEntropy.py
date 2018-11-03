# coding:UTF-8
# 2018-11-3
# 最大熵分割
# https://blog.csdn.net/robin__chou/article/details/53931442

import numpy as np 

def maxEntrop(img):
    histogram = [0] * 256
    m, n = np.shape(img)

    max_entropy = -1
    threshed = 0
    total_pixel = m * n 
    # 计算阈值
    for i in range(m):
        for j in range(n):
            histogram[img[i, j]] += 1

    for i in range(256):
        # 计算Pt
        p_t = 0
        for x in range(i):
            p_t += histogram[x]

        # 计算背景熵
        H_B = 0
        for x in range(i):
            if histogram[x] != 0:
                pi_pt = histogram[x] / p_t
                H_B += - pi_pt * np.log(pi_pt)


        # 计算物体熵
        H_O = 0
        for x in range(i, 250):
            if histogram[x] != 0:
                pi_1_pt = histogram[x] / (total_pixel - p_t)
                H_O += - pi_1_pt * np.log(pi_1_pt)


        total_entrop = H_O + H_B
        if total_entrop > max_entropy:
            max_entropy = total_entrop
            threshed  = i 

    print(threshed)
    return threshed