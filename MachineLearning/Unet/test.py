# coding:utf-8

import numpy as np 
b = np.array([[1, 2], [3, 4]])
np.tile(b, 2) #沿X轴复制2倍
ret_b = np.tile(b, (1, 1, 3))


# image = np.expand_dims(b, axis=2)
# image = np.concatenate((image, image, image), axis=-1)
b=b[:,:,np.newaxis]
b= b.repeat([3],axis=2)
print(b.shape, b)