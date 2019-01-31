# coding:utf-8
# 2019-1-20

import numpy as np 
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                           'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                           'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                   	'D' : np.random.randn(8)})

grouped = df.groupby(['A', 'B'])
print(grouped.head())

# LR: 26854370467.122700, 28450644931.7619
# Ridge: 0.117050, 0.0081
# Lasso: 0.139493, 0.0060
# RF: 0.158286, 0.0069
# GBR: 0.138816, 0.0058
# SVR: 0.115757, 0.0057
# LinSVR: 0.119993, 0.0092
# Ela: 0.113419, 0.0060
# SGD: 0.173172, 0.0199
# Bay: 0.112142, 0.0062
# Ker: 0.111944, 0.0057
# Extra: 0.155343, 0.0051
# Xgb: 0.138958, 0.0069
# AdaBoost: 0.163489, 0.0061
# Bagging: 0.157092, 0.0077
# DT: 0.215556, 0.0041
# KN: 0.166435, 0.0096

models = [
          Ridge(alpha=17),
          Lasso(alpha=0.0003,max_iter=10000),
          RandomForestRegressor(),
          GradientBoostingRegressor(learning_rate=0.2),
          SVR(epsilon=0.01, gamma=0.005, kernel="rbf"), 
          LinearSVR(epsilon=0.001, loss="epsilon_insensitive"), 
          ElasticNet(alpha=0.0005, l1_ratio=0.5, max_iter=10000), 
          SGDRegressor(alpha=0.3, l1_ratio=0.3),
          BayesianRidge(), 
          KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5),
          XGBRegressor(), 
          AdaBoostRegressor(n_estimators=50),
          BaggingRegressor(),
          KNeighborsRegressor()]