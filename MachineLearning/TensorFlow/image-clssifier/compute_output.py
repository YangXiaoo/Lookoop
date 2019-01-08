# coding:UTF-8
# 2019-1-7
# test

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import re
import sys
import tarfile

import numpy as np
from six.moves import urllib
import tensorflow as tf


input_par = {
    'model_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir\model.ckpt-638.meta',
    'label_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\data\label.txt',
    'image_file' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\row_data\train\2',
    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir',
    'width' : 224,
    'height' : 224,
    'prediction_output' : '',
}

__suffix__ = ["png"]

def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix__:
                file.append(path)
    return file

class NodeLookup(object):
    """
    加载标签
    """
    def __init__(self, label_lookup_path=None):
        self.node_lookup = self.load(label_lookup_path)

    def load(self, label_lookup_path):
        node_id_to_name = {}
        with open(label_lookup_path) as f:
            data = f.readlines()
            for index, line in enumerate(data):
                node_id_to_name[index] = line.strip()
        print(node_id_to_name)
        return node_id_to_name

    def id_to_string(self, node_id):
        if node_id not in self.node_lookup:
            return ''
        return self.node_lookup[node_id]


def create_graph(sess, model_path, checkpoint_path):
    """
    从保存模型 xx_xx.pb  中加载图
    """
    # with tf.gfile.FastGFile(model_path, 'rb') as f:
    #     graph_def = tf.GraphDef()
    #     graph_def.ParseFromString(f.read())
    #     _ = tf.import_graph_def(graph_def, name='')

    saver = tf.train.import_meta_graph(model_path)
    saver.restore(sess, tf.train.latest_checkpoint(checkpoint_path))

    # 获取权重
    graph = tf.get_default_graph()
    return graph


def preprocess_for_eval(image, 
                        height, 
                        width,
                        central_fraction=False, # 0.875
                        scope=None):
    with tf.name_scope(scope, 'eval_image', [image, height, width]):
        if image.dtype != tf.float32:
            image = tf.image.convert_image_dtype(image, dtype=tf.float32)

        # 裁剪图片
        if central_fraction:
            image = tf.image.central_crop(image, central_fraction=central_fraction)

        if height and width:
            # Resize the image to the specified height and width.
            image = tf.expand_dims(image, 0)
            image = tf.image.resize_bilinear(
                image, 
                [height, width],
                align_corners=False)
            image = tf.squeeze(image, [0])

        image = tf.subtract(image, 0.5)
        image = tf.multiply(image, 2.0)

        return image


def run_inference_on_image(_):
    image_list = []
    file_list = getFiles(input_par['image_file'])
    with tf.Graph().as_default():
        for img in file_list:
            image_data = tf.gfile.FastGFile(img, 'rb').read()
            image_data = tf.image.decode_jpeg(image_data)
            image_data = preprocess_for_eval(image_data, input_par['width'], input_par['height'])
            image_data = tf.expand_dims(image_data, 0)
            with tf.Session() as sess:
                image_data = sess.run(image_data)
                image_list.append(image_data)

    input_images = tf.placeholder(dtype=tf.float32, shape = [None,224,224,3])
    with tf.Session() as sess:
        # 加载保存的模型
        graph = create_graph(sess, input_par['model_path'], input_par['checkpoint_path'])
        softmax_tensor = graph.get_tensor_by_name('vgg_16/fc8/weights/RMSProp_1:0')
        node_lookup = NodeLookup(input_par['label_path'])
        for image_data in image_list:
            predictions = sess.run(softmax_tensor,
                               {input_images: image_data})
            
            predictions = np.squeeze(predictions)
            pred = tf.argmax(predictions,axis=1)
            print(predictions.shape) # (4096, 18)
            print(sess.run(pred))
            # 测试输出前5个
            # top_k = predictions.argsort()[-5:][::-1]
            # print(top_k)
            # for node_id in top_k:
            #     human_string = node_lookup.id_to_string(node_id)
            #     score = predictions[node_id]
            #     print('%s (score = %.5f)\n' % (human_string, score))

"""
[[12 11 10  3  2 17  1 15 16  0  7  9  5 14  6 13  8  4]
 [13  6  5 15  1  2  4 11 14  3  0  7 10  9 16  8 17 12]
 [ 1 13 14  2 12  6 10  9 11  5  4 17  0 15  3 16  8  7]
 [16 10  4  3  6  5  2  0  9 13  1 17 11  8  7 15 14 12]
 [14 13  1  9  7  5  3  4  2 16  0  6 15 10  8 12 11 17]]
"""

if __name__ == '__main__':
    tf.app.run(main=run_inference_on_image)