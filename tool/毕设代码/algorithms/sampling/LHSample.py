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

def main():
    D = 5   # 控制点数量
    N = 30
    bounds = [
                [-300, 300],    # side y
                [-300, 300],    # side z
                [-300, 100],    # bottom z
                [-300, 300],    # bottom x
                [-200, 200],    # front x

             ]
    dataSavePath = "../../data/samples-data.data"
    samples = LHSample(D,bounds,N)
    X = np.array(samples)
    io.saveData(X, dataSavePath)

    labelsFilePath = "../../data/samples-data-labels.data"
    Y = np.array([[float('%.4f' % random.random())] for x in range(N)])
    io.saveData(Y, labelsFilePath)

    print("   side-y  side-z bottom-z bottom-x front-x")
    print("{} \n\n {}".format(X, Y))
    
def test():
    dataSavePath = "../../data/samples-data.data"
    X = io.getData(dataSavePath)
    print(X)
if __name__ =='__main__':
    test()

"""
# [[  54.04   40.68 -290.76 -111.42   80.6 ]


   side-y  side-z bottom-z bottom-x front-x
[[  42.18 -142.08 -130.84  233.82  124.2 ]  # FFD1
 [ -60.    168.3  -121.16  -56.34  -77.  ]
 [ 285.96 -285.3   -98.88 -228.72   69.96]
 [ 144.66 -222.36 -160.4   290.82  -10.96]
 [ -61.56 -117.66 -111.24  153.24  -84.12]
 [  37.92  -66.42   27.56 -154.2   110.8 ]
 [-169.74  243.78   16.8  -269.46 -116.92]
 [  12.96   20.46 -194.68  175.86  181.8 ]
 [ 263.04  281.76  -30.56   -3.6  -105.56]
 [ 195.42 -167.76 -216.36  242.16   15.8 ]
 [ -82.92   46.44 -260.96  200.1   144.08]
 [ 231.18 -240.72   69.2   -21.6   173.08]
 [-126.12  114.06   49.44 -126.54   59.92]
 [ 125.82  -81.54  -17.92 -112.38 -134.52]
 [-267.48   -7.14   -3.48   91.8  -132.68]
 [  96.6   -47.22 -237.88  134.16  195.88]
 [ -26.88 -128.88  -36.6  -252.84  -46.92]
 [ 219.18  239.7  -286.04   15.66 -174.8 ]
 [ 259.86 -216.6  -171.24 -197.46  -61.72]
 [-208.86  274.26 -224.88  -64.14  -34.32]
 [-235.32  193.14  -60.64   52.32 -167.36]
 [-111.42 -276.54   94.44  -91.5    36.84]
 [-150.72  210.72   36.08 -211.32 -189.4 ]
 [-189.    138.6    81.92 -179.82   48.4 ]
 [ 105.84   70.8  -297.72   69.66  101.32]
 [-282.6   -28.8  -256.24  103.38  150.16]
 [  78.   -199.32  -53.28  187.08   86.  ]
 [ 163.5   159.24 -191.28 -290.88  -20.48]
 [-255.24   90.06  -82.36  266.34   12.24]
 [  -5.7     0.48 -143.08   29.34 -158.04]] 
    
 [0.3196 0.249  0.8346 0.5642 0.8656 0.808  0.6422 0.0079 0.6294 0.5425
 0.9502 0.1746 0.9957 0.1497 0.3364 0.834  0.2516 0.2456 0.4399 0.2136
 0.7416 0.2459 0.1966 0.8094 0.283  0.3763 0.2281 0.1688 0.152  0.5457]
"""
