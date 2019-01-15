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

p = 'C:/Study/github/others/finetuning/nasnet-a_large_04_10_2017'
r = os.path.join(p, '0', '3.np')
print(r)


# # r = os.path.join()
# print(os.listdir(r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\data'))
file_list = os.listdir(r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir_pnasnet_large')
print(file_list)
least_f, max_iter = '', 0
for f in file_list:
    if '.meta' in f:
        tmp_iter = int(f.split('-')[-1].split('.')[0])
        if tmp_iter > max_iter:
            least_f = f

print(least_f)