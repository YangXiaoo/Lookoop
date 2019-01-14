# coding:UTF-8
# 2019-1-8
# export_inference_graph

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorflow.python.platform import gfile
from datasets import dataset_factory
from nets import nets_factory


slim = tf.contrib.slim

input_para = {
    'model_name' : 'vgg_16', # inception3
    'is_training' : False,
    'default_image_size' : 224, # vgg:224, inception:299
    'dataset_name' : 'bone',
    'labels_offset' : 0,

    'output_file' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/vgg_16_inf_graph.pb', # vgg

    # 'output_file' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/inception_v3_inf_graph.pb', # inception3

    'data_split' : 'validation',

    
    'dataset_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/data', # 处理后TF格式的数据集
}


def main(input_para):
    tf.logging.set_verbosity(tf.logging.INFO)
    with tf.Graph().as_default() as graph:
        dataset = dataset_factory.get_dataset(
            input_para['dataset_name'], 
            input_para['data_split'],
            input_para['dataset_dir'])
        network_fn = nets_factory.get_network_fn(
            input_para['model_name'],
            num_classes=(dataset.num_classes - input_para['labels_offset']),
            is_training=input_para['is_training'])
        if hasattr(network_fn, 'default_image_size'):
            image_size = network_fn.default_image_size
        else:
            image_size = input_para['default_image_size']
        placeholder = tf.placeholder(
            name='input', 
            dtype=tf.float32,
            shape=[1, image_size, image_size, 3])
        network_fn(placeholder)
        graph_def = graph.as_graph_def()
        with gfile.GFile(input_para['output_file'], 'wb') as f:
            f.write(graph_def.SerializeToString())


if __name__ == '__main__':
  main(input_para)