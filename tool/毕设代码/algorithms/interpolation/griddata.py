# coding:utf-8
# 2019/10/15
# http://liao.cpython.org/scipytutorial11/
# 多元插值

import numpy as np
def func(x, y):
    return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
    
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
points = np.random.rand(1000, 2)
values = func(points[:,0], points[:,1])

from scipy.interpolate import griddata
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
plt.figure()

ax1 = plt.subplot2grid((2,2), (0,0), projection='3d')
ax1.plot_surface(grid_x, grid_y, grid_z0, color = "c")
ax1.set_xlim3d(0, 1)
ax1.set_ylim3d(0, 1)
ax1.set_zlim3d(-0.25, 0.25)
ax1.set_title('nearest')

ax2 = plt.subplot2grid((2,2), (0,1), projection='3d')
ax2.plot_surface(grid_x, grid_y, grid_z1, color = "c")
ax2.set_xlim3d(0, 1)
ax2.set_ylim3d(0, 1)
ax2.set_zlim3d(-0.25, 0.25)
ax2.set_title('linear')

ax3 = plt.subplot2grid((2,2), (1,0), projection='3d')
ax3.plot_surface(grid_x, grid_y, grid_z2, color = "r")
ax3.set_xlim3d(0, 1)
ax3.set_ylim3d(0, 1)
ax3.set_zlim3d(-0.25, 0.25)
ax3.set_title('cubic')

ax4 = plt.subplot2grid((2,2), (1,1), projection='3d')
ax4.scatter(points[:,0], points[:,1], values,  c= "b")
ax4.set_xlim3d(0, 1)
ax4.set_ylim3d(0, 1)
ax4.set_zlim3d(-0.25, 0.25)
ax4.set_title('org_points')

plt.tight_layout()
plt.show()

print "*" * 20

ax1 = plt.subplot2grid((2,2), (0,0), projection='3d')
ax1.plot_surface(grid_x, grid_y, grid_z1, color = "c")
ax1.scatter(points[:,0][:100], points[:,1][:100], values[:100],  c= "r", s = 20)
ax1.set_xlim3d(0, 1)
ax1.set_ylim3d(0, 1)
ax1.set_zlim3d(-0.25, 0.25)
ax1.set_title('org_points')

x = np.linspace(0, 1.00, num = 10, endpoint=True)
y = np.linspace(0, 0.5, num = 10, endpoint=True)
x,y = np.meshgrid(x, y)
ax2 = plt.subplot2grid((2,2), (0,1), projection='3d')
ax2.plot_surface(grid_x, grid_y, grid_z1, color = "c")
ax2.scatter(x, y, func(x, y),  c= "b", s = 20)
y = np.linspace(0.5, 1.0, num = 10, endpoint=True)
x,y2 = np.meshgrid(x, y)
ax2.scatter(x, y2, func(x, y2),  c= "b", s = 20)
ax2.set_xlim3d(0, 1)
ax2.set_ylim3d(0, 1)
ax2.set_zlim3d(-0.25, 0.25)
ax2.set_title('meshgrid')


x = np.linspace(0, 1.00, num = 10, endpoint=True)
y = np.linspace(0, 0.5, num = 10, endpoint=True)
x,y = np.meshgrid(x, y)
ax3 = plt.subplot2grid((2,2), (1,0), projection='3d')
ax3.scatter(points[:,0][:100], points[:,1][:100], values[:100],  c= "r", s = 20)
ax3.scatter(x, y, func(x, y),  c= "b", s = 20)
y = np.linspace(0.5, 1.0, num = 10, endpoint=True)
x,y2 = np.meshgrid(x, y)
ax3.scatter(x, y2, func(x, y2),  c= "b", s = 20)
#ax3.plot_wireframe
ax3.plot_surface(grid_x, grid_y, grid_z1, color = "c",alpha=0.5)
ax3.set_xlim3d(0, 1)
ax3.set_ylim3d(0, 1)
ax3.set_zlim3d(-0.25, 0.25)
ax3.set_title('org_point and meshgrid')

plt.tight_layout()
plt.show()