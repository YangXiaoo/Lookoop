# coding:utf-8
# 2019-1-15

import numpy as np
import os


def mkdirs(file_list):
    """
    创建文件目录
    """
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 


def get_checkpoint(train_dir):
    """
    获得最新的ckpt文件

    Args:
        train_dir: 模型保存路径

    Returns:
        ckpt文件路径
    """
    file_list = os.listdir(train_dir)
    least_f, max_iter = '', 0
    for f in file_list:
        if '.meta' in f:
            tmp_iter = int(f.split('-')[-1].split('.')[0])
            if tmp_iter > max_iter:
                least_f = f
                max_iter = tmp_iter
    least_f = ".".join(least_f.split('.')[:-1])
    ret = os.path.join(train_dir, least_f)

    return ret


def get_files(dirpath, suffix=["png"]):
    """
    获得指定目录下的图片

    Args:
        dirpath: 需要遍历的目录
        suffix: 文件后缀格式

    Returns:
        type(list), 指定目录下所有指定后缀文件的全路径
    """
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in suffix:
                file.append(path)
    return file
    

def pre_process(data, alpha=0.99, is_total=False):
    """离差标准化(0, 1)"""
    m, n = np.shape(data)
    ret = np.zeros((m, n))
    for i in range(m):
        total = np.sum(data[i, :])
        max_value = np.max(data[i, :])
        for j in range(n):
            if is_total:
                ret[i, j] = data[i, j] / total * alpha
            else:
                ret[i, j] = [data[i, j], 1][data[i, j] == 0] / max_value * alpha
    return ret


def predictionTopK(pdt, k):
    """预测值中topk
    @param pdt 预测结果，nupmy数组格式
    @param k 前k个结果

    @return topk结果，numpy数组格式
    """
    m, n = np.shape(pdt)
    ret = []
    for i in range(m):
        curNums = pdt[i]
        tmp = topK(curNums.tolist()[0], k)
        ret.append(tmp)

    return np.mat(ret)

def topK(inputNums, k):
    """获得数组中值前k大的索引
    @param inputNums python列表一维
    @param k 前k大

    @param ret 前k大的索引
    """
    import copy
    nums = copy.deepcopy(inputNums)
    ret = []
    for i in range(k):
        tmpMaxIndex, tmpMaxVal = 0, float('-inf')
        for index, val in enumerate(nums):
            if tmpMaxVal < val:
                tmpMaxVal = val
                tmpMaxIndex = index 
        nums[tmpMaxIndex] = float('-inf')
        ret.append(tmpMaxIndex)

    return ret 

# test!
# def topKTest():
#     pdt = np.mat([[1,3,5,2,9,11,6, 10], [5,1,78,4,345,67,23,11]])
#     k = 5

#     ret = predictionTopK(pdt, k)
#     print(ret)

# topKTest()
# """
# [[5 7 4 6 2]
#  [4 2 5 6 7]]
#  """