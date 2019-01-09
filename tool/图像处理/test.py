# coding:utf-8
# import numpy as np 
# lists = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
# it = [[1], [2], [3], [4], [5]]
# for i in lists:
# 	for j in it:
# 		

# print(float('1.4_1'))

# input_file = r'C:\Users\Yauno\Documents\Tencent Files\1270009836\FileRecv\T-male.txt'
# output_lable = 'lable.txt'

# correct = []
# with open(input_file) as f:
# 	data = f.readlines()
# 	for d in data:
# 		split = d[:-1].split(' ')
# 		print(split)
# 		if int(split[-1]) > 19:
# 			correct.append(split[0] + ' ' + split[-1][:-1] + '\n')
# 		else:
# 			correct.append(d)

# correct[-1] = correct[-1][:-1]
# with open(output_lable, 'w') as f:
# 	for i in correct:
# 		f.write(i)

import random
import time
import os

a,b = os.path.split(r'C:\Study\test\kaggle-bonage\train-male\train.txt')
print(a, b)


# os.rename(r'C:\Users\Yauno\Documents\Tencent Files\1270009836\FileRecv\lable.txt', r'C:\Study\test\kaggle-bonage\lable.txt')

# file = r'C:\Users\Yauno\Documents\Tencent Files\1270009836\FileRecv\lable(1).txt'
# with open(file) as f:
# 	data = f.readlines()
# 	dicts = []
# 	for d in  data:
# 		if d in dicts:
# 			print(d)
# 		else:
# 			dicts.append(d)
