# coding:UTF-8
# 2018-10-18
# Collaborative Filtering

import numpy as np 

def loadData(file_path):
    """
    加载数据，数据为矩阵
    """
    f = open(file_path)   
    data = []
    for line in f.readlines():
        lines = line.strip().split("\t")
        tmp = []
        for x in lines:
            if x != "-":
                tmp.append(float(x))
            else:
                # 未进行打分
                tmp.append(0)
        data.append(tmp)
    f.close()
    
    return np.mat(data)


def cosSimilary(x, y):
    """
    余弦相似度
    """
    numerator = x * y.T 
    denominator = np.sqrt(x * x.T) * np.sqrt(y * y.T)
    cos_sim = numerator / denominator
    return cos_sim[0, 0]


def similarity(data):
    """
    计算矩阵中任意两行之间的相似度
    """
    m = np.shape(data)[0]
    w = np.mat(np.zeros((m, m))) # 相似度矩阵
    for i in range(m):
        for j in range(m):
            if i != j:
                w[i, j] = cosSimilary(data[i, :], data[j, :])
                w[j, i] = w[i, j]
            else:
                w[i, j] = 0 # 自己和自己的相似度为0

    return w 


def userBasedRecommend(data, w, user):
    """
    基于用户相似度为用户推荐商品
    此时的data: 用户-商品矩阵
    a. 选出该用户没有标记过的商品
    b. 根据相似度对没有标记的商品进行打分
    c. 对结果进行排序
    """
    m, n = np.shape(data)
    interaction = data[user, :]

    # a. 选出该用户没有标记过的商品
    not_inter = []
    for i in range(n):
        if interaction[0, i] == 0:
            not_inter.append(i)

    # b. 根据相似度对没有标记的商品进行打分
    predict = {}
    for x in not_inter:
        item = np.copy(data[:, x]) # 所有用户对该商品的打分
        for i in range(m):
            if item[i, 0] != 0:
                if x not in predict:
                    predict[x] = w[user, i] * item[i, 0] # 该用户与其他用户对于商品i的相似度
                else:
                    predict[x] += w[user, i] * item[i, 0]

    sort_predict = sorted(predict.items(), key=lambda d:d[1], reverse=True)

    return sort_predict


def itemBasedRecommend(data, w, user):
    """
    基于商品为用户user推荐商品
    此时的data为 ： 商品-用户矩阵
    """
    m, n = np.shape(data)
    interaction = data[:, user].T

    # a. 选出该用户没有标记过的商品
    not_inter = []
    for i in range(n):
        if interaction[0, i] == 0:
            not_inter.append(i)

    # b. 根据相似度对没有标记的商品进行打分
    predict = {}
    for x in not_inter:
        item = np.copy(interaction) # 获取用户user对商品的互动信息
        for j in range(m): # 对每一个商品
            if item[0, j] != 0: # 利用互动过的商品预测
                if x not in predict:
                    predict[x] = w[x, j] * item[0, j]
                else:
                    predict[x] = predict[x] + w[x, j] * item[0, j]

    sort_predict = sorted(predict.items(), key=lambda d:d[1], reverse=True)

    return sort_predict


def topK(predict, k):
    """
    为用户推荐前K个商品
    """
    top_recommend = []
    len_predict = len(predict)
    if k >= len_predict:
        top_recommend = predict
    else:
        top_recommend = predict[ : k]
    return top_recommend


if __name__ == '__main__':
    print("loading data...")
    data_file = "data.txt"
    data = loadData(data_file)

    # 基于项的协同过滤数据处理
    # data = data.T

    print("calculate similarity between items...")
    w = similarity(data)

    print("predicting...")
    predict = userBasedRecommend(data, w, 0)

    print("top k recommend")
    top = topK(predict, 2)
    print(top)