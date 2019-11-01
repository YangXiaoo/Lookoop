# coding=utf-8
# 2019/10/15
import sys
sys.path.append('../../')

import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter
import pickle
from util import io
import random

def LHSample(D, bounds, N):
    '''超拉丁立方抽样
    步骤：
    1. 将[0, 1]分为 n 等份，每个小区间内[i/n, (i+1)/n]内根据均匀分布随机产生一个数
    2. 将这 n 个随机数的顺序打乱
    3. 这 n 各数即为每个随机样本的概率，按照概率分布函数的反函数生成随机分布的值

    @param D 参数个数
    @param bounds 参数对应范围（list）
    @param N 拉丁超立方层数
    @return 样本数据
    '''
    result = np.empty([N, D])
    tmp = np.empty([N])
    d = 1.0 / N

    for i in range(D):
        for j in range(N):
            tmp[j] = float('%.4f' % np.random.uniform(low=j * d, high=(j + 1) * d, size=1)[0])
        np.random.shuffle(tmp)
        for j in range(N):
            result[j, i] = tmp[j]
    # 对样本数据进行拉伸
    b = np.array(bounds)
    lowerBounds = b[:,0]
    upperBounds = b[:,1]
    if np.any(lowerBounds > upperBounds):
        print('范围出错')
        return None

    np.add(np.multiply(result, (upperBounds - lowerBounds), out=result),
           lowerBounds,
           out=result)

    return result

if __name__ =='__main__':
    D = 3
    N = 30
    bounds = [
                [0, 100],       # side y
                [-200, 200],    # front x
                [-300, 100],    # bottom z
             ]
    dataSavePath = "../../data/samples-data.data"
    samples = LHSample(D,bounds,N)
    X = np.array(samples)
    io.saveData(X, dataSavePath)

    labelsFilePath = "../../data/samples-data-labels.data"
    Y = np.array([float('%.4f' % random.random()) for x in range(N)])
    io.saveData(Y, labelsFilePath)

    print("X: {} \n\n Y:{}".format(X, Y))

"""
    side-y  front-x bottom-z
X: [[  59.85  160.6  -185.36]
 [  54.11   -8.88 -111.32]
 [  96.79  -43.08  -29.92]
 [  83.13   90.48  -51.24]
 [  92.99  -96.24   71.68]
 [  14.45 -136.68 -140.04]
 [  72.88  -27.36   18.84]
 [  47.47  143.28  -69.48]
 [  75.91  195.2  -164.28]
 [  66.13 -198.64  -16.12]

 [  94.29 -172.12 -264.36]
 [  42.71 -147.96 -207.24]
 [  79.54   70.2   -38.16]
 [  87.01   45.68   -2.44]
 [  20.69  -24.68 -293.84]
 [  35.29  113.24 -197.44]
 [   5.95   11.12 -284.96]
 [  19.53   19.    -80.32]
 [  39.79  151.64 -241.88]
 [  27.85 -127.8   -99.4 ]
 [  62.12   39.4  -115.88]
 [  69.59  -64.08 -178.48]
 [  32.26  124.36 -222.72]
 [  45.57  -83.6    56.36]
 [  25.32   56.96   23.96]
 [   2.31  -73.4    86.68]
 [   7.55  178.08   98.04]
 [  83.96 -109.56 -126.68]
 [  53.14 -177.6  -251.16]
 [  10.56  100.92   40.32]] 

 Y:[0.8207 0.7578 0.0924 0.5272 0.0694 0.9827 0.3111 0.0806 0.6875 0.83
 0.9674 0.2839 0.4047 0.1608 0.8665 0.007  0.9625 0.8032 0.1994 0.5618
 0.0571 0.524  0.462  0.0259 0.6481 0.8806 0.2479 0.5475 0.6872 0.2969]
"""