# coding:utf-8
# 2019/10/15
# 线性回归

import sys
sys.path.append('../../')

from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, AdaBoostRegressor, BaggingRegressor
from sklearn.svm import SVR, LinearSVR
from sklearn.kernel_ridge import KernelRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

import numpy as np
import pickle 

from util import io

def getModel(modelName):
    """选择模型"""
    modelDict = {
        "Linear" : linear_model.LinearRegression(),
        "Ridge": linear_model.Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
            normalize=False, random_state=None, solver='auto', tol=0.001),
        "Lasso" : linear_model.Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
            normalize=False, positive=False, precompute=False, random_state=None,
            selection='cyclic', tol=0.0001, warm_start=False),
        "ElasticNet" : linear_model.ElasticNet(alpha=0.001,max_iter=10000),
        "GradientBoosting" : GradientBoostingRegressor(),
        "SVR" : SVR(),
        "XGB" : XGBRegressor(), 
        "AdaBoost" : AdaBoostRegressor(n_estimators=50),
        "Bagging" : BaggingRegressor(),
    }

    return modelDict[modelName]

def train(reg, X, Y):
    """
    @param reg 训练模型
    @param X 训练数据
    @param Y 标签
    """
    # reg = linear_model.Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
    #       normalize=False, random_state=None, solver='auto', tol=0.001)
    reg.fit(X, Y) 
    print("w: {}\n, b: {}".format(reg.coef_, reg.intercept_))

    return reg

def main():
    dataFilePath = "../../data/samples-data.data"
    labelsFilePath = "../../data/samples-data-labels.data"
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)
    modelNames = ["Linear", "Ridge", "Lasso", "ElasticNet", "GradientBoosting"]
    for modelName in modelNames:
        reg = getModel(modelName)

        model = train(reg, X, Y)
        io.saveData(model, "../../data/{}.model".format(modelName))

if __name__ == '__main__':
    main()