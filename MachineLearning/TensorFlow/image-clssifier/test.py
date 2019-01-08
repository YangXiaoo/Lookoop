# coding:UTF-8
import os
from tensorflow.python import pywrap_tensorflow
 
# code for finall ckpt
# checkpoint_path = os.path.join('~/tensorflowTraining/ResNet/model', "model.ckpt")
 
# code for designated ckpt, change 3890 to your num
checkpoint_path = os.path.join(r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir_incept', "model.ckpt-162")
# Read data from checkpoint file
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()
# Print tensor name and values
for key in var_to_shape_map:
    print("tensor_name: ", key)
 
"""
tensor_name:  vgg_16/conv5/conv5_1/biases/RMSProp_1
tensor_name:  vgg_16/conv5/conv5_1/biases/RMSProp
tensor_name:  vgg_16/conv1/conv1_1/weights/RMSProp_1
tensor_name:  vgg_16/conv1/conv1_1/weights/RMSProp
tensor_name:  vgg_16/conv1/conv1_1/biases/RMSProp
tensor_name:  vgg_16/conv1/conv1_1/biases/RMSProp_1
tensor_name:  global_step
tensor_name:  vgg_16/conv5/conv5_1/biases
tensor_name:  vgg_16/conv4/conv4_1/weights/RMSProp_1
tensor_name:  vgg_16/conv4/conv4_1/biases/RMSProp_1
tensor_name:  vgg_16/conv1/conv1_1/weights
tensor_name:  vgg_16/conv2/conv2_1/weights/RMSProp_1
tensor_name:  vgg_16/conv2/conv2_1/biases/RMSProp_1
tensor_name:  vgg_16/conv1/conv1_1/biases
tensor_name:  vgg_16/fc7/weights/RMSProp_1
tensor_name:  vgg_16/conv1/conv1_2/biases/RMSProp_1
tensor_name:  vgg_16/fc7/weights/RMSProp
tensor_name:  vgg_16/conv1/conv1_2/biases/RMSProp
tensor_name:  vgg_16/fc7/weights
tensor_name:  vgg_16/conv1/conv1_2/biases
tensor_name:  vgg_16/conv1/conv1_2/weights
tensor_name:  vgg_16/conv4/conv4_2/weights/RMSProp_1
tensor_name:  vgg_16/conv2/conv2_2/weights
tensor_name:  vgg_16/conv1/conv1_2/weights/RMSProp
tensor_name:  vgg_16/conv4/conv4_2/weights/RMSProp
tensor_name:  vgg_16/conv1/conv1_2/weights/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_1/weights/RMSProp
tensor_name:  vgg_16/conv2/conv2_1/weights
tensor_name:  vgg_16/conv2/conv2_1/biases
tensor_name:  vgg_16/conv2/conv2_1/weights/RMSProp
tensor_name:  vgg_16/conv2/conv2_1/biases/RMSProp
tensor_name:  vgg_16/conv4/conv4_2/biases/RMSProp_1
tensor_name:  vgg_16/conv2/conv2_2/biases
tensor_name:  vgg_16/conv2/conv2_2/biases/RMSProp
tensor_name:  vgg_16/conv4/conv4_2/biases
tensor_name:  vgg_16/conv2/conv2_2/biases/RMSProp_1
tensor_name:  vgg_16/conv5/conv5_2/weights/RMSProp_1
tensor_name:  vgg_16/conv2/conv2_2/weights/RMSProp
tensor_name:  vgg_16/conv4/conv4_2/weights
tensor_name:  vgg_16/conv2/conv2_2/weights/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_1/biases
tensor_name:  vgg_16/conv4/conv4_1/weights
tensor_name:  vgg_16/conv4/conv4_1/biases
tensor_name:  vgg_16/conv3/conv3_1/weights/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_1/biases/RMSProp
tensor_name:  vgg_16/conv3/conv3_1/biases/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_1/weights
tensor_name:  vgg_16/conv3/conv3_2/biases
tensor_name:  vgg_16/conv3/conv3_2/biases/RMSProp
tensor_name:  vgg_16/conv3/conv3_2/biases/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_2/weights
tensor_name:  vgg_16/conv3/conv3_2/weights/RMSProp
tensor_name:  vgg_16/fc7/biases
tensor_name:  vgg_16/conv3/conv3_2/weights/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_3/biases
tensor_name:  vgg_16/conv3/conv3_3/biases/RMSProp
tensor_name:  vgg_16/conv3/conv3_3/weights
tensor_name:  vgg_16/conv3/conv3_3/biases/RMSProp_1
tensor_name:  vgg_16/conv4/conv4_3/weights/RMSProp_1
tensor_name:  vgg_16/conv3/conv3_3/weights/RMSProp
tensor_name:  vgg_16/conv4/conv4_3/weights/RMSProp
tensor_name:  vgg_16/conv5/conv5_3/biases
tensor_name:  vgg_16/conv3/conv3_3/weights/RMSProp_1
tensor_name:  vgg_16/conv4/conv4_1/weights/RMSProp
tensor_name:  vgg_16/conv4/conv4_1/biases/RMSProp
tensor_name:  vgg_16/conv4/conv4_2/biases/RMSProp
tensor_name:  vgg_16/conv4/conv4_3/biases
tensor_name:  vgg_16/conv4/conv4_3/biases/RMSProp
tensor_name:  vgg_16/conv4/conv4_3/biases/RMSProp_1
tensor_name:  vgg_16/conv4/conv4_3/weights
tensor_name:  vgg_16/conv5/conv5_1/weights
tensor_name:  vgg_16/conv5/conv5_1/weights/RMSProp
tensor_name:  vgg_16/conv5/conv5_1/weights/RMSProp_1
tensor_name:  vgg_16/conv5/conv5_2/biases
tensor_name:  vgg_16/conv5/conv5_2/biases/RMSProp
tensor_name:  vgg_16/conv5/conv5_2/biases/RMSProp_1
tensor_name:  vgg_16/conv5/conv5_2/weights
tensor_name:  vgg_16/conv5/conv5_2/weights/RMSProp
tensor_name:  vgg_16/conv5/conv5_3/biases/RMSProp
tensor_name:  vgg_16/conv5/conv5_3/biases/RMSProp_1
tensor_name:  vgg_16/conv5/conv5_3/weights
tensor_name:  vgg_16/conv5/conv5_3/weights/RMSProp
tensor_name:  vgg_16/conv5/conv5_3/weights/RMSProp_1
tensor_name:  vgg_16/fc6/biases
tensor_name:  vgg_16/fc6/biases/RMSProp
tensor_name:  vgg_16/fc6/biases/RMSProp_1
tensor_name:  vgg_16/fc6/weights
tensor_name:  vgg_16/fc6/weights/RMSProp
tensor_name:  vgg_16/fc6/weights/RMSProp_1
tensor_name:  vgg_16/fc7/biases/RMSProp
tensor_name:  vgg_16/fc7/biases/RMSProp_1
tensor_name:  vgg_16/fc8/biases
tensor_name:  vgg_16/fc8/biases/RMSProp
tensor_name:  vgg_16/fc8/biases/RMSProp_1
tensor_name:  vgg_16/fc8/weights
tensor_name:  vgg_16/fc8/weights/RMSProp
tensor_name:  vgg_16/fc8/weights/RMSProp_1
"""