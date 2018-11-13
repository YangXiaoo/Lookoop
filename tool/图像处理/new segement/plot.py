# coding:UTF-8
# 2018-10-25
# https://blog.csdn.net/zchshhh/article/details/78215087

from api import handleHistogram, plotScatter, loadData
from regression import ridgeRegression



if __name__ == '__main__':
    print("loading data ...")
    feature, label = loadData("data.txt")
    feature = handleHistogram(feature, alpha=20000, is_total=True)
    # feature = handleHistogram(feature)

    w0 = ridgeRegression(feature, label, 0.5)
    plotScatter(feature, label, w0, [(0,150), (0,150)], "regression")


