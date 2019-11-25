# coding:utf-8
# 2019/10/28

import sys

from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

# https://pykrige.readthedocs.io/en/latest/overview.html
from pykrige.rk import RegressionKriging
from pykrige.compat import train_test_split

svr_model = SVR(C=0.1)
rf_model = RandomForestRegressor(n_estimators=100)
lr_model = LinearRegression(normalize=True, copy_X=True, fit_intercept=False)

models = [svr_model, rf_model, lr_model]

try:
    housing = fetch_california_housing()
except PermissionError:
    # this dataset can occasionally fail to download on Windows
    sys.exit(0)

# take the first 5000 as Kriging is memory intensive
p = housing['data'][:5000, :-2] # 房屋的一些信息不包括经度和纬度
x = housing['data'][:5000, -2:] # 经度和维度
target = housing['target'][:5000]
print("[DEBUG] target[:10] : {}".format(target[:10]))

p_train, p_test, x_train, x_test, target_train, target_test \
    = train_test_split(p, x, target, test_size=0.3, random_state=42)
# print("[DEBUG] p_train[:10] : {}".format(p_train[:10]))
# print("[DEBUG] p_test[:10] : {}".format(p_test[:10]))
# print("[DEBUG] x_train[:10] : {}".format(x_train[:10]))
# print("[DEBUG] x_test[:10] : {}".format(x_test[:10]))
# print("[DEBUG] target_train[:10] : {}".format(target_train[:10]))
# print("[DEBUG] target_test[:10] : {}".format(target_test[:10]))
# assert False

for m in models:
    print('=' * 40)
    print('regression model:', m.__class__.__name__)
    m_rk = RegressionKriging(regression_model=m, n_closest_points=10)
    m_rk.fit(p_train, x_train, target_train)
    print('Regression Score: ', m_rk.regression_model.score(p_test, target_test))
    print('RK score: ', m_rk.score(p_test, x_test, target_test))

# fit(self, p, x, y)
#  |      fit the regression method and also Krige the residual
#  |      
#  |      Parameters
#  |      ----------
#  |      p: ndarray
#  |          (Ns, d) array of predictor variables (Ns samples, d dimensions)
#  |          for regression
#  |      x: ndarray
#  |          ndarray of (x, y) points. Needs to be a (Ns, 2) array
#  |          corresponding to the lon/lat, for example 2d regression kriging.
#  |          array of Points, (x, y, z) pairs of shape (N, 3) for 3d kriging
#  |      y: ndarray
#  |          array of targets (Ns, )
#  |  
#  |  krige_residual(self, x)
#  |      Parameters
#  |      ----------
#  |      x: ndarray
#  |          ndarray of (x, y) points. Needs to be a (Ns, 2) array
#  |          corresponding to the lon/lat, for example.
#  |      
#  |      Returns
#  |      -------
#  |      residual: ndarray
#  |          kriged residual values
#  |  
#  |  predict(self, p, x)
#  |      Parameters
#  |      ----------
#  |      p: ndarray
#  |          (Ns, d) array of predictor variables (Ns samples, d dimensions)
#  |          for regression
#  |      x: ndarray
#  |          ndarray of (x, y) points. Needs to be a (Ns, 2) array
#  |          corresponding to the lon/lat, for example.
#  |          array of Points, (x, y, z) pairs of shape (N, 3) for 3d kriging
#  |      
#  |      Returns
#  |      -------
#  |      pred: ndarray
#  |          The expected value of ys for the query inputs, of shape (Ns,).