# coding:utf-8
import numpy as np 
import pandas as pd
from tool.util import pre_process

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


from sklearn.model_selection import cross_val_score, GridSearchCV, KFold
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import Imputer 

def cv_rmse(model, X, y):
    """获得均差"""
    rmse = np.sqrt(-cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=5))
    return rmse


def _get_model_name():
    names = ["KNeighbors", 
             "SVC", 
             "DecisionTree", 
             "RandomForest", 
             "ExtraTrees", 
             "AdaBoost", 
             "GradientBoosting", 
             "Bagging",
             "GaussianNB",
             "LogisticRegression",
             "XGB"]

    train_models = [
        KNeighborsClassifier(leaf_size=200, n_neighbors=1),
        SVC(degree=2, gamma=5, kernel='poly'),
        DecisionTreeClassifier(class_weight='balanced', max_depth=50, max_features='sqrt', random_state=20),
        RandomForestClassifier(),
        ExtraTreesClassifier(),
        AdaBoostClassifier(learning_rate=0.1, n_estimators=50, random_state=50),
        GradientBoostingClassifier (),
        BaggingClassifier(max_features=0.5, max_samples=0.5, n_estimators=100, oob_score=True, random_state=40),
        GaussianNB(),
        LogisticRegression(),
        XGBClassifier(gamma=0.1, learning_rate=0.1, max_depth=10, min_child_weight=0.5, n_estimators=200, objective='multi:softmax', subsample=0.8),
    ]

    return names, train_models



class grid():
    """网格搜索"""
    def __init__(self, model):
        self.model = model
        
    def grid_train(self, X, y, train_para):
        grid_search = GridSearchCV(self.model, train_para, cv=5, scoring="neg_mean_squared_error")
        grid_search.fit(X, y)
        print(grid_search.best_params_, np.sqrt(-grid_search.best_score_)) # 打印最好的结果
        grid_search.cv_results_['mean_test_score'] = np.sqrt(-grid_search.cv_results_['mean_test_score'])
        print(pd.DataFrame(grid_search.cv_results_)[['params','mean_test_score','std_test_score']])


class stacking(BaseEstimator, RegressorMixin, TransformerMixin):
    """stacking集成学习"""
    def __init__(self, model, fusion_model):
        self.model = model
        self.fusion_model = fusion_model
        self.kf = KFold(n_splits=5, random_state=50, shuffle=True)
        
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


def train_model(_train_raw, _labels):
    """训练模型
    @param _train_raw type(Mat), mxn, 训练数据集
    @param _labels type(Mat), mx1, 训练数据标签
    @return 训练模型
    """
    train_raw = pre_process(_train_raw)
    train_dataset = pd.DataFrame(train_raw)
    labels = pd.DataFrame(_labels)

    """标签与数据组合"""
    _train = np.hstack((train_dataset,labels))
    train = pd.DataFrame(_train)
    _y = train[256] # 另一种格式的标签

    """数据清理"""
    X = Imputer().fit_transform(train_dataset)
    y = Imputer().fit_transform(_y.values.reshape(-1,1)).ravel()

    """训练模型"""
    _, train_models = _get_model_name()
    stack_model = stacking(train_models, LogisticRegression())
    stack_model.fit(X, y)

    return stack_model

def _test_train_model(_train_raw, _labels):
    """测试用"""
    train_raw = pre_process(_train_raw)
    train_dataset = pd.DataFrame(train_raw)
    labels = pd.DataFrame(_labels)

    """标签与数据组合"""
    _train = np.hstack((train_dataset, labels))
    train = pd.DataFrame(_train)
    _y = train[256] # 另一种格式的标签

    """训练模型"""
    model = LogisticRegression()
    model.fit(train_dataset, _y)

    return model

def train_by_model(model_name, _train_raw, _labels):
    """使用一种模型进行训练"""
    train_raw = pre_process(_train_raw)
    train_dataset = pd.DataFrame(train_raw)
    labels = pd.DataFrame(_labels)

    """标签与数据组合"""
    _train = np.hstack((train_dataset, labels))
    train = pd.DataFrame(_train)
    _y = train[256] # 另一种格式的标签

    """训练模型"""
    names, models = _get_model_name()
    model = models[names.index(model_name)]
    model.fit(train_dataset, _y)

    return model

