# coding:UTF-8
import os
# from tensorflow.python import pywrap_tensorflow
# import tensorflow as tf
import numpy as np
 
# # code for finall ckpt
# # checkpoint_path = os.path.join('~/tensorflowTraining/ResNet/model', "model.ckpt")
 
# # # code for designated ckpt, change 3890 to your num
# checkpoint_path = r'C:\Study\github\others\finetuning\nasnet-a_large_04_10_2017\model.ckpt'
# # Read data from checkpoint file
# with tf.Session() as sess:
#     reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
#     var_to_shape_map = reader.get_variable_to_shape_map()
#     # Print tensor name and values
#     for key in var_to_shape_map:
#         print("tensor_name: ", key)
#         # try:
#         #     tensor = sess.graph.get_tensor_by_name(key + ":0")
#         #     print(tensor)
#         # except:
#         #     pass


#########################
# model_path = 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/vgg_16_inf_graph.pb'
# with tf.gfile.FastGFile(model_path, 'rb') as f:
#     graph_def = tf.GraphDef()
#     graph_def.ParseFromString(f.read())
#     _ = tf.import_graph_def(graph_def, name='')

# with tf.Session() as sess:
#     var_to_shape_map = sess.graph.get_variable_to_shape_map()
#     for key in var_to_shape_map:
#         print("tensor_name: ", key)


"""
tensor_name:  vgg_16/conv5/conv5_1/biases/RMSProp_1
tensor_name:  vgg_16/conv5/conv5_1/biases/RMSProp
tensor_name:  vgg_16/conv1/conv1_1/weights/RMSProp_1
tensor_name:  vgg_16/conv1/conv1_1/weights/RMSProp
tensor_name:  vgg_16/conv1/conv1_1/biases/RMSProp
tensor_name:  vgg_16/conv1/conv1_1/biases/RMSProp_1
...
"""

# ret = np.load(r'C:\Study\test\tensorflow-bone\vgg_16.npy')
# print(ret)
"""
'2_m-1-1.9.png': array([[ 2.05507520e+07,  1.94889760e+07,  7.13783300e+06,
         1.11738584e+08,  1.14213176e+08,  1.93517440e+07,
         3.29394900e+07,  1.47754850e+07,  2.06201880e+07,
         8.36995200e+07,  6.26028800e+07, -6.73418560e+07,
         7.42099200e+07,  2.64569460e+07,  6.01207280e+07,
         8.01406640e+07,  7.80726000e+07,  6.82800960e+07]], dtype=float32)
"""


#########################
# p = 'C:/Study/github/test'
# r = os.path.join(p, '0', 'dd' , 'fff' '3.np', 't.txt')
# with open(r, 'w') as f:
#     f.write('ddd')


#########################
# # r = os.path.join()
# print(os.listdir(r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\data'))
# file_list = os.listdir(r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir_pnasnet_large')
# print(file_list)
# least_f, max_iter = '', 0
# for f in file_list:
#     if '.meta' in f:
#         tmp_iter = int(f.split('-')[-1].split('.')[0])
#         if tmp_iter > max_iter:
#             least_f = f

# print(least_f)


#########################
# nums = [1,20,3,4]
# nums_2 = [10,20,30,40]
# nums_1 = np.array(nums)
# nums_2 = np.array(nums_2)
# dicts = {'nums_1':nums_1, 'nums_2':nums_2}
# for k,v in dicts.items():
#     dicts[k] = v / 2

# # print(dicts)
# empty = np.array([])
# r = np.append(empty, nums_1)
# # print(r)


#########################
# # n = []
# # for i in nums:
# #     n.append(i)
# # print(n)


#########################
# ret = [nums_1 == nums_2] 
# ret = np.array(ret)  + 0
# print(ret.sum())

#########################
# print(int('12'))

########################
# # 查看图像年龄分布
# lable_path = r'C:\Study\test\kaggle-bonage\validation-male\labels.txt'
# with open(lable_path) as f:
#     data = f.readlines()
#     count = {}
#     for d in data:
#         age = d[:-1].split(' ')[-1]
#         count[age] = count.get(age, 0) + 1
# sort_count = sorted(count.items(), key=lambda x:int(x[0]))
# for a,c in sort_count:
#     if c < 5:
#         print(a, c)
# print(sort_count)


#######################
# nums = [1,2,3,4,5,6]
# thresh = len(nums)
# print(nums[thresh:])
# print(nums[:thresh])
# import datetime
# t = datetime.datetime.now()
# print(str(t).split(' ')[-1].replace('.', '_').replace(':', '_'))


####################
# nums_1 = []
# nums_2 = []
# nums_3 = []
# nums_4 = []
# group = [[nums_1, nums_2], [nums_3, nums_4]]
# for g in group:
#     n_1, n_2 = g
#     n_1.append([[1]])
#     n_2.append(2)

# print(nums_1)


##################
# nums = []

# def test(nums):
#     nums.append(1)


# def test_1(nums):
#     nums = []
#     test(nums)
#     print(nums)

# test_1(nums)


#######################
nums_1 = [1,2,3]
nums_2 = [4,5,6]
nums_1.extend(nums_2)
print(nums_1)