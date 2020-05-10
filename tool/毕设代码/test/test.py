import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x = np.arange(-10,10,0.2)
y = np.arange(-10,10,0.2)
print(x)
#产生隔点矩阵
x,y = np.meshgrid(x,y)
print(x)
z = x**2 + y**2 + 2
print(z)
ax.plot_surface(x,y,z)
x1, y1, z1 = [], [], []
x1.append(x[1][0])
y1.append(y[1][0])
z1.append(z[1][0])
x1.append(x[10][0])
y1.append(y[10][0])
z1.append(z[10][0])
ax.scatter(x1,y1,z1,c='r',marker=".")
# plt.show()