# coding:utf-8

def test_numsEmpty():
    nums = []
    if nums:
        print("pass")
    else:
        print("fail")

def test_strOps():
    str1 = 'a'
    str2 = 'c'
    print(str2 - str1)

# try:
#     for n in gsearch1.cv_results_['mean_test_socre']:
#         print("[INFO] details of gsearch1.cv_results_:{}".format(n))
# except Exception as e:
#     print("[ERROR] error info:{}".format(str(e)))

# print("[INFO] best parameters:{}".format(gsearch1.best_params_))
# print("[INFO] best scores:{}".format(gsearch1.best_score_))

import numpy as np

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

def topKTest():
    pdt = np.mat([[1,3,5,2,9,11,6, 10], [5,1,78,4,345,67,23,11]])
    k = 5

    ret = predictionTopK(pdt, k)
    print(ret)

topKTest()

"""
[[5 7 4 6 2]
 [4 2 5 6 7]]
"""