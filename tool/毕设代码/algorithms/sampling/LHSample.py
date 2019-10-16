# coding=utf-8
# 2019/10/15
import sys
sys.path.append('../../')

import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter
import pickle
from util import io

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
            tmp[j] = np.random.uniform(low=j * d, high=(j + 1) * d, size=1)[0]
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
    D = 18
    N = 30
    bounds = [[-100, 100], [-100, 100], [-100, 100], 
              [-100, 100], [-100, 100], [-100, 100],
              [-100, 100], [-100, 100], [-100, 100],
              [-100, 100], [-100, 100], [-100, 100],
              [-100, 100], [-100, 100], [-100, 100],
              [-100, 100], [-100, 100], [-100, 100],
              ]
    dataSavePath = "../../data/samples-data.data"
    samples = LHSample(D,bounds,N)
    XY = np.array(samples)
    io.saveData(XY, dataSavePath)

    labelsFilePath = "../../data/samples-data-labels.data"
    Y = np.array([x for x in range(N)])
    io.saveData(Y, labelsFilePath)

    print("X: {}, Y:{}".format(XY, Y))
