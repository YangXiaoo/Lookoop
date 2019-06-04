# coding:UTF-8
# 2019-1-8
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

from preprocessing import vgg_preprocessing

__all__ = [
    ''
]

input_par = {
    'model_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\resnet_frozen_graph.pb',

    'label_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\data\label.txt',

    'image_file' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\row_data\train\2',

    'test_label_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\row_data\train\2\2.txt',

    # 'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir',


    # 'tensor_name' :  'vgg_16/fc8/squeezed:0', 
    # 'tensor_name' : 'InceptionV3/Logits/SpatialSqueeze:0',
    # 'tensor_name' : 'final_layer/predictions:0', # pnasnet, nasnet
    'tensor_name' : 'resnet_v2_200/predictions/Reshape_1:0', # resnet
    'is_save' : True,

    'width' : 224, # vgg:224, inception3:299, nasnet:331, resnet:224, pnasnet:331, resnet:224
    'height' : 224,
    'prediction_output' : r'C:\Study\test\tensorflow-bone\resnet.npy' # r'C:\Study\test\tensorflow-bone\InceptionV3.npy',
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


def getlabelsDict(lable_path, is_handle=False):
    """
    对图像m-3-3.4.png
    return:
        {pic_0:class_0, pic_1:class_1, ...}
    """
    lable = open(lable_path)
    data = lable.readlines()
    ret = {}
    for line in data:
        # print(line[:-1].split(' ')) # ['mm', '(2).png', '10']
        tmp = line[:-1].split(' ')
        if is_handle:
            key, value = ''.join(tmp[:-1]), tmp[-1]
            if int(value) > 19:
                value = value[:-1]
        else:
            key, value = tmp
        ret[key] = value
    lable.close()
    return ret


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


def create_graph(sess, model_path):
    """
    从保存模型 xx_xx.pb  中加载图
    """
    with tf.gfile.FastGFile(model_path, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')



def preprocess_for_eval(image, 
                        height, 
                        width,
                        central_fraction=False, # 0.875
                        scope=None):
    with tf.name_scope(scope, 'eval_image', [image, height, width]):
        if image.dtype != tf.float32:
            image = tf.image.convert_image_dtype(image, dtype=tf.float32)

        if height and width:
            # Resize the image to the specified height and width.
            image = tf.expand_dims(image, 0)
            image = tf.image.resize_bilinear(image, 
                                            [height, width],
                                            align_corners=False)
            image = tf.squeeze(image, [0])

        return image


def run_inference_on_image(input_par):
    print("predcition..")
    image_list = {}
    file_list = getFiles(input_par['image_file'])
    # with tf.Graph().as_default():
    #     print("[INFO] loading picture.")
    #     for k,img in enumerate(file_list):
    #         base_name = os.path.basename(img)
    #         image_data = tf.gfile.FastGFile(img, 'rb').read()
    #         image_data = tf.image.decode_jpeg(image_data)
    #         image_data = preprocess_for_eval(image_data, input_par['width'], input_par['height'])
    #         image_data = tf.expand_dims(image_data, 0)
    #         with tf.Session() as sess:
    #             image_data = sess.run(image_data)
    #             image_list[base_name] = image_data
    #         if k == 100:
    #             break
    create_graph(None, input_par['model_path'])
    label_dict = getlabelsDict(input_par['label_path'])
    with tf.Session() as sess:
        # init = tf.global_variables_initializer()
        # sess.run(init)
        # 加载保存的模型
        prediction_output = {} # {'2_m-1-1.9.png': data}
        tensor = sess.graph.get_tensor_by_name(input_par['tensor_name'])
        print("[INFO] predicting image data...")
        # for k,image_data in image_list.items():
        for k,img in enumerate(file_list):
            base_name = os.path.basename(img)
            print("[INFO] Predicting %s" % base_name)
            image_data = tf.gfile.FastGFile(img, 'rb').read()
            image_data = tf.image.decode_jpeg(image_data, channels=3)
            # print(image_data.shape)
            image_data = vgg_preprocessing.preprocess_for_eval(image_data, input_par['height'], input_par['width'], 256)
            image_data = tf.expand_dims(image_data, 0)
            image_data = sess.run(image_data)
            try:
                prediction = sess.run(tensor, {'input:0': image_data})
                prediction = np.squeeze(prediction)
                print("[Temp INFO] ", prediction)
                label = label_dict[base_name]
                prediction_output[label + '_' + base_name] = prediction
            except Exception as e:
                print("[Error] %s" % str(e))
            # 测试
            if k == 5:
                break
        if input_par['is_save']:
            print("[INFO] Saving predictions.")
            np.save(input_par['prediction_output'], prediction_output)
            print("[INFO] Saved in %s" % input_par['prediction_output'])

        return prediction_output


if __name__ == '__main__':
    run_inference_on_image(input_par)