# coding:UTF-8
# 2018-10-25
# 计算误差的标准均方

from api import handleHistogram, loadData, getPredictionErrorRate
from regression import ridgeRegression



if __name__ == '__main__':
    print("loading data ...")
    feature, label = loadData("new_data.txt")
    feature = handleHistogram(feature)

    w0 = ridgeRegression(feature, label, 0.5)
    r = getPredictionErrorRate(feature, label, w0)
    print(r)


