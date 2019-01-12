# coding:utf-8
import os
# file_dir = r'C:\Study\test\kaggle-bonage\train-male_disposal_out'
# ret = os.listdir(file_dir)
# print(ret)
dicts = {'4': '0', '6': '1', '9': '2', '10': '3'}
ret = sorted(dicts.keys(), key=lambda x : int(x))
print(ret)