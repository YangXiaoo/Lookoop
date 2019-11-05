# coding:utf-8
# 2019/10/12

import matplotlib.pyplot as plt
import numpy as np

x = np.array([[1,2,3], [3,0.5,1.4], [4.6,6,2.1]])
y = np.array([4.00, 6.40, 8.00])
z1 = np.polyfit(x, y, 2) # 用3次多项式拟合
p1 = np.poly1d(z1)	
print(p1) # 在屏幕上打印拟合多项式
# yvals = p1(x) # 也可以使用yvals=np.polyval(z1,x)
# plot1 = plt.plot(x, y, '*',label='original values')
# plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc=4) # 指定legend的位置,读者可以自己help它的用法
# plt.title('polyfitting')
# plt.show()

