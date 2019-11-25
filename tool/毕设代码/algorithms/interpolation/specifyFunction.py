# coding:utf-8
# 2019/10/12

# 使用非线性最小二乘法拟合
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# 用指数形式来拟合
x = np.arange(1, 17, 1)
y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
def func(x,a,b, c, d, e):
    ret = a*np.exp(b/x) + c + d*x + e*x**2
    print("[DEBUG] func : {}".format(ret))
    return ret
popt, pcov = curve_fit(func, x, y)
print(popt)