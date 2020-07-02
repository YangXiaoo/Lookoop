# coding: utf-8
# 
import sys
sys.path.append("../")

from sklearn.model_selection import cross_val_score, GridSearchCV, KFold
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, AdaBoostRegressor, BaggingRegressor
from sklearn.svm import SVR, LinearSVR
from sklearn.linear_model import ElasticNet, SGDRegressor, BayesianRidge
from sklearn.kernel_ridge import KernelRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

import numpy as np
import pandas as pd
import logging

from util import io 
from util import tool

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)

def getTrainData():
    """获取训练数据"""
    dataFilePath = "../data/samples-data.data"
    labelsFilePath = "../data/samples-data-labels.data"
    X = io.getData(dataFilePath)
    Y = io.getData(labelsFilePath)

    return X, Y

X, y = getTrainData()
Y = y.reshape(1, len(y))[0]

def cv_rmse(model, X, y):
    # cross_val_score函数用法：https://www.cnblogs.com/lzhc/p/9175707.html
    rmse = np.sqrt(-cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=5))
    return rmse

def cv_mae(model, X, y):
    ret = tool.crossValueScore(model, X, y, tool.computeMAE)

    return ret

class grid():
    """网格搜索策略寻找最佳参数"""
    def __init__(self, model):
        self.model = model
        logger.info("{}-grid-model-{}-{}".format('*'*25, model.__class__.__name__,'*'*25))
        
    def grid_train(self, X, y, train_para):
        grid_search = GridSearchCV(self.model, train_para, cv=5, scoring="neg_mean_squared_error", return_train_score=True)
        grid_search.fit(X, y)
        logger.info("best_params: {}, best_score: {}".format(grid_search.best_params_, np.sqrt(-grid_search.best_score_))) # 打印最好的结果
        grid_search.cv_results_['mean_test_score'] = np.mean(-grid_search.cv_results_['mean_test_score'])
        # logger.info(pd.DataFrame(grid_search.cv_results_)[['params','mean_test_score','std_test_score']])


models = [LinearRegression(),
          Ridge(), # http://www.cnblogs.com/pinard/p/6023000.html
          Lasso(alpha=0.01,max_iter=10000), # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html
          RandomForestRegressor(), # https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestRegressor.html
          GradientBoostingRegressor(), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html
          SVR(), # https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR
          LinearSVR(), # https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html
          ElasticNet(alpha=0.001,max_iter=10000), # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html
          SGDRegressor(max_iter=10000,tol=1e-3), # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
          BayesianRidge(), # 
          KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5), # https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html
         ExtraTreesRegressor(), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html
          XGBRegressor(), 
          AdaBoostRegressor(n_estimators=50), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html
          BaggingRegressor(), # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html
          DecisionTreeRegressor(), #https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
          KNeighborsRegressor()] # https://scikit-learn.org/0.18/modules/generated/sklearn.neighbors.KNeighborsRegressor.html


def getRawTrainResults():
    """估计模型的训练能力"""
    names = ["LR", "Ridge", "Lasso", "RF", "GBR", "SVR", "LinSVR", "Ela","SGD","Bay","Ker","Extra","Xgb", "AdaBoost", "Bagging", "DT", "KN"]
    for name, model in zip(names, models):
        score = cv_rmse(model, X, Y)
        logger.info("{}: {:.6f}, {:.4f}".format(name,score.mean(),score.std()))


def getRawTrainResultsUsingMAE():
    """估计模型的训练能力"""
    logger.info("{}-getRawTrainResultsUsingMAE-{}".format('*'*25, '*'*25))
    names = ["LR", "Ridge", "Lasso", "RF", "GBR", "SVR", "LinSVR", "Ela","SGD","Bay","Ker","Extra","Xgb", "AdaBoost", "Bagging", "DT", "KN"]
    for name, model in zip(names, models):
        score = cv_mae(model, X, Y)
        logger.info("{}: {}".format(name, score))

def gridSearch():
    grid(Lasso()).grid_train(X,Y,{'alpha': [0.002, 0.0003, 0.00035, 0.0004,0.0005,0.0007,0.0006,0.0009,0.0008], 'max_iter':[10000]})

    grid(Ridge()).grid_train(X,Y,{'alpha':[i for i in range(10, 20)]})

    grid(GradientBoostingRegressor()).grid_train(X,Y,{'learning_rate':[float(i/10) for i in range(1, 10)]})

    grid(SVR()).grid_train(X,Y,
                           {
                               'kernel':['rbf'], 
                               'gamma':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5],
                               'epsilon':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5, 1, 10]
                           })

    grid(LinearSVR()).grid_train(X,Y,{'epsilon':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5], 'loss':['epsilon_insensitive', 'squared_epsilon_insensitive']})

    grid(GradientBoostingRegressor()).grid_train(X,Y,{'learning_rate':[float(i/10) for i in range(1, 10)]})

    grid(LinearSVR()).grid_train(X,Y,{'epsilon':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5], 'loss':['epsilon_insensitive', 'squared_epsilon_insensitive']})

    grid(ElasticNet()).grid_train(X,Y,{'alpha':[0.0005, 0.001,0.005, 0.01, 0.05, 0.1, 0.5],'l1_ratio':[0.08,0.1,0.3,0.5,0.7],'max_iter':[10000]})

    grid(SGDRegressor()).grid_train(X,Y,{'alpha':[0.005, 0.01, 0.05, 0.1,0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 5],'l1_ratio':[0.08,0.1,0.3,0.5,0.7, 0.8, 0.9, 1]})

    grid(KernelRidge()).grid_train(X,Y,{'alpha':[0.05, 0.1, 0.3,0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 5], 'kernel':['polynomial'], 'coef0':[1, 1.2, 1.5, 1.6, 1.8, 1.9, 2, 2.2, 2.5, 3]})

if __name__ == '__main__':
    # getRawTrainResultsUsingMAE()
    gridSearch()