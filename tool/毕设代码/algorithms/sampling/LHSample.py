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
    D = 5   # 控制点数量
    N = 30
    bounds = [
                [0, 100],       # side y
                [-300, 300],    # side z
                [-300, 100],    # bottom z
                [-300, 300],    # bottom x
                [-200, 200],    # front x

             ]
    # dataSavePath = "../../data/samples-data.data"
    # samples = LHSample(D,bounds,N)
    # X = np.array(samples)
    # io.saveData(X, dataSavePath)

    labelsFilePath = "../../data/samples-data-labels.data"
    Y = np.array([[float('%.4f' % random.random())] for x in range(N)])
    io.saveData(Y, labelsFilePath)

    print("   side-y  side-z bottom-z bottom-x front-x")
    print("{} \n\n {}".format(X, Y))

"""
   side-y  side-z bottom-z bottom-x front-x
[[  54.04   40.68 -290.76 -111.42   80.6 ]
 [  30.83  151.74 -278.2  -193.92  -72.36]
 [   7.61 -179.82 -258.52  129.66 -178.8 ]
 [  16.44  139.5  -269.48   88.38 -141.84]
 [  42.7   -64.44  -11.52   21.9   -45.56]
 [  45.6  -298.5    12.68  -26.88  -61.04]
 [   2.68  106.8    96.52 -288.78  -11.72]
 [  10.11   18.96  -30.32  172.32  172.48]
 [  20.41 -187.26   65.72  -75.42  137.6 ]
 [  69.63 -239.82   77.8   223.02 -159.76]
 [  61.05  230.94 -169.84 -267.96  101.04]
 [  65.79   39.78  -85.48   69.    190.08]
 [  70.33  187.86  -49.2   213.6  -167.44]
 [  97.66  255.24  -61.56 -156.36   22.08]
 [  18.22 -138.42 -108.2   295.8    72.24]
 [   5.68 -118.56 -241.92  256.38 -128.52]
 [  27.62  289.44   59.96   14.58 -192.36]
 [  94.88  168.54   29.8  -246.24 -100.4 ]
 [  36.84   63.6  -147.04  -99.3   108.96]
 [  83.7  -211.14 -207.36   -5.7   -30.12]
 [  47.38  -57.06 -129.   -124.44   65.72]
 [  89.31  -31.26  -35.76  118.32  126.92]
 [  33.87  211.44    4.76  -48.48   33.32]
 [  76.51   90.6  -231.96   43.62  158.56]
 [  59.93 -152.7  -189.56 -220.08 -115.76]
 [  77.92 -242.58   34.44  151.86  176.36]
 [  25.66   -2.16 -155.04 -168.48    0.64]
 [  82.81 -260.22 -114.04  189.24  -82.92]
 [  93.22  274.98  -98.96 -206.52  -14.88]
 [  52.59  -81.54 -200.68  269.7    46.52]] 

 [0.3196 0.249  0.8346 0.5642 0.8656 0.808  0.6422 0.0079 0.6294 0.5425
 0.9502 0.1746 0.9957 0.1497 0.3364 0.834  0.2516 0.2456 0.4399 0.2136
 0.7416 0.2459 0.1966 0.8094 0.283  0.3763 0.2281 0.1688 0.152  0.5457]
"""