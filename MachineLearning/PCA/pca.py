# coding:UTF-8
# 2018-11-9
# PCA

# https://blog.csdn.net/cherrylvlei/article/details/81430447
# 解释为什么除以n-1:  https://blog.csdn.net/Hearthougan/article/details/77859173
import numpy as np 


def pac(data, k):
	"""
	得到前k个特征向量，通过前k个特征向量重建原矩阵
	"""
	# 获得均值
	data_mean = np.mean(data, axis=0)
	# 去均值
	mean_moved = data - data_mean
	# 获得协方差
	data_cov = np.cov(mean_moved, rowvar=0)
	# 计算协方差的特征值，特征向量
	eig_val, eig_vec = np.linalg.eig(np.mat(data_cov))
	# 对特征值进行排序,从小到大
	egi_val_sort = np.argsort(eig_val)
	egi_val_ind = egi_val_sort[:-(k + 1):-1]
	egi_val_cut = egi_val[:, egi_val_ind]
	# 获得新的维度数据
	low_data = mean_moved * egi_val_cut
	recon_data = (low_data * egi_val_cut.T) + data_mean
	return low_data, recon_data

