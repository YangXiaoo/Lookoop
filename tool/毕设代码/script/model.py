# coding:utf-8
# 模型
import numpy as np 
import pandas as pd

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
# from xgboost import XGBRegressor


from sklearn.model_selection import cross_val_score, GridSearchCV, KFold
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import Imputer 

def cv_rmse(model, X, y):
    """获得均差"""
    rmse = np.sqrt(-cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=5))
    return rmse


def getModel():
    """选择出来的最佳模型"""
    names = []  # 模型名
    models = [
                RandomForestRegressor(max_depth=1, n_estimators=60),
                SVR(epsilon=1000, gamma=0.005, kernel='rbf'),
                ElasticNet(), 
                BayesianRidge(),  
                ExtraTreesRegressor(min_samples_leaf=0.4, min_samples_split=0.9), 
                BaggingRegressor(n_estimators=30),
                KNeighborsRegressor(n_neighbors=19)
            ]
    for m in models:
        names.append(m.__class__.__name__)

    return names, models

def _getModel():
    """选择出来的最佳模型"""
    names = []  # 模型名
    models = [
                SVR(epsilon=1000, gamma=0.0001, kernel='rbf'),
                RandomForestRegressor(max_depth=1, n_estimators=20), 
                BayesianRidge(alpha_1=1e-6, alpha_2=1e-6, tol=0.0001),  
                ExtraTreesRegressor(min_samples_leaf=0.4, min_samples_split=0.7), 
                # BaggingRegressor(n_estimators=7),
                KNeighborsRegressor(n_neighbors=19)
            ]
    for m in models:
        names.append(m.__class__.__name__)

    return names, models


class stacking(BaseEstimator, RegressorMixin, TransformerMixin):
    """stacking集成学习"""
    def __init__(self, model, fusionModel):
        self.model = model
        self.fusionModel = fusionModel
        self.kf = KFold(n_splits=5, random_state=2, shuffle=True)
        self.modelSaved = None
        
    def fit(self, X, y):
        self.modelSaved = [list() for i in self.model] 
        trainPred = np.zeros((X.shape[0], len(self.model))) # 存储每个数据被预测的结果， 其结果使用融合模型进行训练
        
        for i,mod in enumerate(self.model):
            for trainIndex, valueIndex in self.kf.split(X, y):
                # print("[DEBUG] trainIndex: %s, valueIndex: %s" % (trainIndex, valueIndex))
                tmpModel = clone(mod)
                tmpModel.fit(X[trainIndex], y[trainIndex])
                self.modelSaved[i].append(tmpModel)
                trainPred[valueIndex, i] = tmpModel.predict(X[valueIndex])
        self.fusionModel.fit(trainPred, y) # 将训练数据预测结果作为融合模型的输入训练数据
        
        return self
    
    def predict(self, X):
        """预测"""
        testMean = []
        for model in self.modelSaved:
            tmpData = []
            for m in model:
                tmpData.append(np.ravel(m.predict(X)))
            resStack = np.column_stack(tmpData).mean(axis=1)
            testMean.append(resStack)
        testMean = np.column_stack(testMean)
        return self.fusionModel.predict(testMean)


def train_model(_train_raw, _labels, collectionModel=LinearRegression()):
    """训练模型
    @param _train_raw type(Mat), mxn, 训练数据集
    @param _labels type(Mat), mx1, 训练数据标签
    @return 训练模型
    """
    train_dataset = pd.DataFrame(_train_raw)
    labels = pd.DataFrame(_labels)
    X = Imputer().fit_transform(train_dataset)
    y = Imputer().fit_transform(labels.values.reshape(-1,1)).ravel()
    
    # 训练
    _, train_models = getModel()
    stack_model = stacking(train_models, collectionModel)
    stack_model.fit(X, y)

    return stack_model

def train_by_model(model_name, _train_raw, _labels):
    """使用一种模型进行训练"""
    train_dataset = pd.DataFrame(_train_raw)
    labels = pd.DataFrame(_labels)
    X = Imputer().fit_transform(train_dataset)
    y = Imputer().fit_transform(labels.values.reshape(-1,1)).ravel()

    # 根据模型名进行单个模型训练
    names, models = getModel()
    model = models[names.index(model_name)]
    model.fit(train_dataset, y)

    return model

def test():
    pass

if __name__ == '__main__':
    test()