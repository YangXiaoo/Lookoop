# coding:utf-8
import os
import logging
import logging.handlers
import configparser # 读写配置
import datetime
import time
from copy import deepcopy

import numpy as np
from sklearn.model_selection import KFold

def mkdirs(file_list):
    """创建文件目录"""
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 
    
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

def getConfig(configPath):
    """获取配置方法"""
    conf = configparser.ConfigParser() # import ConfigParser
    conf.read(configPath)

    return conf

def dataAdapter(data1, data2):
    """数据转换"""
    try:
        _ = data1.shape
    except:
        data1 = np.array(data1)
    try:
        _ = data2.shape
    except:
        data2 = np.array(data2)
    try:
        if np.shape(data1)[0] != 1:
            data1 = data1.reshape(1, len(data1))[0]
        if np.shape(data2)[0] != 1:
            data2 = data2.reshape(1, len(data2))[0]
    except Exception as e:
        print("[ERROR] catch exception : {}".format(str(e)))

    return data1, data2

def computeMAE(data1, data2):
    """计算平均绝对误差MSE"""
    data1, data2 = dataAdapter(data1, data2)
    m = np.shape(data1)[0]
    tmpSum = 0
    for i in range(m):
        tmpSum += abs(data1[i] - data2[i])

    return tmpSum / m

def computeRMAE(data1, data2):
    """计算相对平均误差"""
    data1, data2 = dataAdapter(data1, data2)
    m = np.shape(data1)[0]
    tmpSum = 0
    for i in range(m):
        tmpSum += abs(data1[i] - data2[i]) / data1[i]

    return tmpSum / m

def computeMSE(data1, data2):
    """计算平均绝对误差MSE"""
    data1, data2 = dataAdapter(data1, data2)
    m = np.shape(data1)[0]
    tmpSum = 0
    for i in range(m):
        tmpSum += (data1[i] - data2[i])**2

    return tmpSum / m

def computeRMSE(data1, data2):
    """计算RMSE"""
    return computeMSE(data1, data2)

def sequeceInArray(nums, seqIndex):
    ret = np.array([])
    for index in seqIndex:
        ret = np.append(ret, nums[index], axis=0)

    return ret

def crossValueScore(inputModel, X, y, agent=computeMSE, cv=5):
    """交叉验证模型性能"""
    fold = KFold(n_splits=cv, random_state=2, shuffle=True)

    pdtMSE = []
    for trainIndex, valueIndex in fold.split(X, y):
        model = deepcopy(inputModel)
        _x, _y = np.array([]), []
        for index in trainIndex:
            _x = np.concatenate([_x, X[index]], axis=0)
            _y.append(y[index])
        _x = np.array(_x).reshape(len(trainIndex),len(X[0]))
        model.fit(_x, np.ravel(_y))

        testX, testY = np.array([]), []
        for index in valueIndex:
            testX = np.concatenate([testX, X[index]], axis=0)
            testY.append(y[index])
        testX = np.array(testX).reshape(len(valueIndex),len(X[0]))
        tmpPdt = model.predict(testX)
        pdtMSE.append(agent(testY, tmpPdt))

    return sum(pdtMSE) / cv