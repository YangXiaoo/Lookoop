# coding:utf-8
import os
import logging
import logging.handlers
import datetime
import time

import numpy as np
from sklearn.model_selection import KFold

def getLogger(logger_path):
    """设置日志"""
    if logger_path:
        mkdirs(logger_path)
        
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    all_log = os.path.join(logger_path, "all.log")
    error_log = os.path.join(logger_path, "error.log")


    rf_handler = logging.handlers.TimedRotatingFileHandler(all_log, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(error_log)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    logger.addHandler(console)

    return logger

def computeMSE(data1, data2):
    """计算平均绝对误差MSE"""
    if np.shape(data1)[0] != 1:
        data1 = data1.reshape(1, len(data1))[0]
    try:
        if np.shape(data2)[0] != 1:
            data2 = data2.reshape(1, len(data2))[0]
    except Exception as e:
        print("[ERROR] catch exception : {}".format(str(e)))
    m = np.shape(data1)[0]
    tmpSum = 0
    for i in range(m):
        tmpSum += abs(data1[i] - data2[i])

    return tmpSum / m

def sequeceInArray(nums, seqIndex):
    ret = np.array([])
    for index in seqIndex:
        ret = np.append(ret, nums[index], axis=0)

    return ret


def crossValueScore(model, X, y, cv=5):
    """交叉验证模型性能"""
    fold = KFold(n_splits=cv, random_state=2, shuffle=True)

    pdtMSE = []
    for trainIndex, valueIndex in fold.split(X, y):
        _x, _y = np.array([]), []
        for index in trainIndex:
            _x = np.concatenate([_x, X[index]], axis=0)
            _y.append(y[index])
        _x = np.array(_x).reshape(len(trainIndex),len(X[0]))
        model.fit(_x, np.array(_y))

        testX, testY = np.array([]), []
        for index in valueIndex:
            testX = np.concatenate([testX, X[index]], axis=0)
            testY.append(y[index])
        testX = np.array(testX).reshape(len(valueIndex),len(X[0]))
        tmpPdt = model.predict(testX)
        pdtMSE.append(computeMSE(tmpPdt, testY))

    return sum(pdtMSE) / cv