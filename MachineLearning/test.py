import numpy as np

# m = 4
# kernel_matrix = np.mat(np.zeros((m, m)))
# kernel_matrix[: ,2] = np.mat(np.ones((m, 1)))
# # print(kernel_matrix[:, 2])
# # [[0. 0. 1. 0.]
# #  [0. 0. 1. 0.]
# #  [0. 0. 1. 0.]
# #  [0. 0. 1. 0.]]

# a = np.mat([[0,0,3],[0,0,9], [12,3,1]])
# print(a)
# k = 2
# # nums = [1,2,3,4,5,6]
# # print(nums[:-2:-1])
# eig_val, eig_vec = np.linalg.eig(np.mat(a))
# print(eig_val)
# egi_val_sort = np.argsort(eig_val)
# egi_val_ind = egi_val_sort[:-(k + 1):-1]
# print(egi_val_ind)
# egi_val_cut = eig_val[:egi_val_ind]

# nums1  = [1,2]
# nums2 = [1,2]
# print(nums1.pop())
# print(nums1)

# import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')  #初始化一个TensorFlow的常量
# sess = tf.Session()  #启动一个会话
# print(sess.run(hello))
#  


import matplotlib.pyplot as plt
import numpy as np

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 9))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()