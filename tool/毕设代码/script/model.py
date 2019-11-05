# coding:utf-8
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
from xgboost import XGBRegressor


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
    names = [
            "LinearRegression",
            "Ridge",
            "Lasso",
            "RandomForestRegressor",
            "GradientBoostingRegressor",
            "SVR",
            "LinearSVR",
            "ElasticNet",
            "SGDRegressor",
            "BayesianRidge",
            "KernelRidge",
            "ExtraTreesRegressor",
            "XGBRegressor",
            "AdaBoostRegressor",
            "BaggingRegressor",
            "DecisionTreeRegressor",
            "KNeighborsRegressor",
        ]

    models = [
            LinearRegression(),
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

    return names, models


class stacking(BaseEstimator, RegressorMixin, TransformerMixin):
    """stacking集成学习"""
    def __init__(self, model, fusion_model):
        self.model = model
        self.fusion_model = fusion_model
        self.kf = KFold(n_splits=5, random_state=2, shuffle=True)
        
    def fit(self, X, y):
        self.model_saved = [list() for i in self.model] 
        train_pred = np.zeros((X.shape[0], len(self.model))) # 存储每个数据被预测的结果， 其结果使用融合模型进行训练
        
        for i,mod in enumerate(self.model):
            for train_index, value_index in self.kf.split(X, y):
                # print("[DEBUG] train_index: %s, value_index: %s" % (train_index, value_index))
                tmp_model = clone(mod)
                tmp_model.fit(X[train_index], y[train_index])
                self.model_saved[i].append(tmp_model)
                train_pred[value_index, i] = tmp_model.predict(X[value_index])
        self.fusion_model.fit(train_pred, y) # 将训练数据预测结果作为融合模型的输入训练数据
        
        return self
    
    def predict(self, X):
        test_mean = np.column_stack([np.column_stack(mod.predict(X) for mod in tmp_model).mean(axis=1) for tmp_model in self.model_saved]) # 对每个test数据进行预测并取平局值
        return self.fusion_model.predict(test_mean)


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