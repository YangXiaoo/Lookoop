# 2018-8-19
# test
# C:\Study\github\Lookoop\Image\Python神经网络\test.py
import numpy
import matplotlib.pyplot
import scipy.special
import os
data_file = open("C:/Study/github/Lookoop/Image/Python神经网络/mnist_dataset/mnist_train_100.csv", "r")
data_list = data_file.readlines()
data_file.close()
value = data_list[0].split(',')
image_array = numpy.asfarray(value[1:]).reshape((28, 28))

matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation="None")
matplotlib.pyplot.show()