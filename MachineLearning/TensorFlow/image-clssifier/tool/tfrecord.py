# coding:utf-8
# 2019-1-10
# tf-record tool

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
import os
import random
import sys
import threading


import numpy as np
import tensorflow as tf
import logging

__all__ = ['main']


def check_and_set_default_args(input_para):
    assert not (input_para['train_shards'] % input_para['num_threads'] and input_para['validation_shards'] % input_para['num_threads']), ("train_shards 和 validation_shards 必须是 num_threads 的公约数")


def _find_image_files(data_dir, 
                    labels_file, 
                    class_label_base):
    """
    return：
        filenames : list, data_dir下所有图片名
        texts : list, 父文件名
        labels : list, 每张图片对应的分类索引，下标从class_label_base开始
    """
    logging.info('处理的数据来源于 %s.' % data_dir)
    unique_labels = [l.strip() for l in tf.gfile.FastGFile(
        labels_file, 'r').readlines()] # 获得需要处理的文件列表

    labels, filenames, texts = [], [], []

    label_index = class_label_base

    # 各个文件夹下的图片
    for text in unique_labels:
        pic_file_pattern = '%s/%s/*' % (data_dir, text) # 匹配格式 `*` 通配符
        matching_files = []
        try:
            matching_files = tf.gfile.Glob(pic_file_pattern)
        except:
            pass
        labels.extend([label_index] * len(matching_files)) # 分类索引
        texts.extend([text] * len(matching_files)) # 父文件夹名
        filenames.extend(matching_files) # 图片名

        logging.info("第 %s 个分类，共处理文件 %s 个" % (
                label_index, len(labels)))
        label_index += 1


    # 打乱列表
    shuffled_index = [i for i in range(len(filenames))]
    random.seed(12345)
    random.shuffle(shuffled_index)

    filenames = [filenames[i] for i in shuffled_index]
    texts = [texts[i] for i in shuffled_index]
    labels = [labels[i] for i in shuffled_index]

    logging.info('在 %s 内, 共找到 %d 张图片,  %d 个标签' %
                 (data_dir, len(filenames), len(unique_labels)))

    return filenames, texts, labels


class ImageCoder(object):
    """
    将TensorFlow图像读取转换
    """
    def __init__(self):
        self._sess = tf.Session() # 创建Session处理图像

        # 将PNG转换为JPEG
        self._png_data = tf.placeholder(dtype=tf.string) # 读取图片未经过解码为字符串
        image = tf.image.decode_png(self._png_data, channels=3)
        self._png_to_jpeg = tf.image.encode_jpeg(image, format='rgb', quality=100)

        # JPEG解码
        self._decode_jpeg_data = tf.placeholder(dtype=tf.string)
        self._decode_jpeg = tf.image.decode_jpeg(self._decode_jpeg_data, channels=3)


    def png_to_jpeg(self, image_data):
        return self._sess.run(self._png_to_jpeg,
                              feed_dict={self._png_data: image_data}) 


    def decode_jpeg(self, image_data):
        image = self._sess.run(self._decode_jpeg,
                               feed_dict={self._decode_jpeg_data: image_data})
        assert len(image.shape) == 3
        assert image.shape[2] == 3, '图片不是三通道'
        return image


def _is_png(filename):
    """
    return bool
    """
    return '.png' in filename

    
def _process_image(filename, coder):
    """
    读取图片
    return:
        image_buffer: string, JPEG
        height: int
        width: int
    """
    with open(filename, 'rb') as f:
        image_data = f.read()

    if _is_png(filename):
        logging.info('%s 转换为JPEG格式' % filename)
        image_data = coder.png_to_jpeg(image_data)

    image = coder.decode_jpeg(image_data) # JPEG解码,解码后可获得图像属性
    assert len(image.shape) == 3
    assert image.shape[2] == 3, '图像不是三通道'

    height, width = image.shape[0], image.shape[1]

    return image_data, height, width


def _int64_feature(value):
    """
    转换为int64格式
    """
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def _bytes_feature(value):
    """
    转换为bytes
    """
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _convert_to_example(filename, 
                        image_buffer, 
                        label,
                        text, 
                        height,
                        width):
    """
    使用tf.train.Example生成 Example proto
    """
    colorspace = b'RGB'
    channels = 3
    image_format = b'JPEG'

    example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': _int64_feature(height),
        'image/width': _int64_feature(width),
        'image/colorspace': _bytes_feature(colorspace),
        'image/channels': _int64_feature(channels),
        'image/class/label': _int64_feature(label),
        'image/class/text': _bytes_feature(str.encode(text)),
        'image/format': _bytes_feature(image_format),
        'image/filename': _bytes_feature(os.path.basename(str.encode(filename))),
        'image/encoded': _bytes_feature(image_buffer)}))

    return example


def _process_image_files_batch(coder, 
                                thread_index, 
                                ranges, 
                                name, 
                                filenames,
                                texts, 
                                labels, 
                                num_shards, 
                                output_dir,
                                dataset_name):
    """
    每个线程的call函数
    """
    num_threads = len(ranges) # 计算线程数
    assert not num_shards % num_threads, 'num_shars必须能整除num_threads'
    num_shards_per_batch = int(num_shards / num_threads) # 每个线程需要处理的数据

    shard_ranges = np.linspace(
        ranges[thread_index][0],
        ranges[thread_index][1],
        num_shards_per_batch + 1).astype(int)
    num_files_in_thread = ranges[thread_index][1] - ranges[thread_index][0] # 计算当前线程需要处理的图像数量

    counter = 0
    for s in range(num_shards_per_batch):
        shard = thread_index * num_shards_per_batch + s # 计算当前图像处理批次
        output_filename = '%s_%s_%.5d-of-%.5d.tfrecord' % (dataset_name, name, shard, num_shards)

        output_file = os.path.join(output_dir, output_filename)

        writer = tf.python_io.TFRecordWriter(output_file)

        shard_counter = 0
        files_in_shard = np.arange(shard_ranges[s], shard_ranges[s + 1], dtype=int) # 获得当前处理的文件索引

        for i in files_in_shard:
            filename = filenames[i]
            label = labels[i]
            text = texts[i]

            image_buffer, height, width = _process_image(filename, coder)
            example = _convert_to_example(
                filename, 
                image_buffer, 
                label,
                text, 
                height,
                width) # tf.train.Features 格式化数据
            writer.write(example.SerializeToString())
            shard_counter += 1
            counter += 1

            if not counter % 300:
                logging.info('%s [thread %d]: Processed %d of %d images in thread batch.' %
                             (datetime.now(), thread_index, counter, num_files_in_thread))
                sys.stdout.flush()
        writer.close()
        logging.info('%s [thread %d]: Wrote %d images to %s' %
                     (datetime.now(), thread_index, shard_counter, output_file))
        sys.stdout.flush()
        shard_counter = 0
    logging.info('%s [thread %d]: Wrote %d images to %d shards.' %
                 (datetime.now(), thread_index, counter, num_files_in_thread))
    sys.stdout.flush()


def _process_image_files(name,
                        filenames,
                        texts,
                        labels,
                        num_shards,
                        num_threads,
                        output_dir,
                        dataset_name):
    
    # 判断图片是否对应标签
    assert len(filenames) == len(texts)
    assert len(filenames) == len(labels)

    # 将列表分割为num_threads份
    # np.linspace(0, 20, 4 + 1).astype(np.int)
    # [ 0  5 10 15 20]
    spacing = np.linspace(0, len(filenames), num_threads + 1).astype(np.int) 

    # 组合索引
    ranges = []
    for i in range(len(spacing) - 1):
        ranges.append([spacing[i], spacing[i + 1]])

    logging.info('开启 %s 个线程' % num_threads)
    sys.stdout.flush() # 刷新输出

    coord = tf.train.Coordinator() # 监控线程

    coder = ImageCoder() # 初始化图像处理类

    # 线程入队
    threads = []
    for thread_index in range(len(ranges)): # range(num_threads)
        args = (coder, thread_index, ranges, name, filenames, texts, labels, num_shards, output_dir, dataset_name)
        t = threading.Thread(target=_process_image_files_batch, args=args)
        t.start()
        threads.append(t)

    coord.join(threads)
    logging.info('%s : 完成 %d 图像的数据转换.' % 
                (datetime.now(), len(filenames)))
    sys.stdout.flush()


def _process_dataset(name,
                    directory,
                    num_shards,
                    labels_file,
                    input_para):
    filenames, texts, labels = _find_image_files(directory, labels_file, input_para['class_label_base'])
    _process_image_files(name, filenames, texts, labels, num_shards, input_para['num_threads'], input_para['output_dir'], input_para['dataset_name'])


def main(input_para):
    logging.info('Saving results to %s' % input_para['output_dir'])
    _process_dataset(
        'validation', 
        input_para['validation_dir'],
        input_para['validation_shards'],
        input_para['labels_file'],
        input_para)

    _process_dataset(
        'train', 
        input_para['train_dir'],
        input_para['train_shards'],
        input_para['labels_file'],
        input_para)

    logging.info('%s : Finish!' % datetime.now())

if __name__ == '__main__':
    input_para = {

    }
    main(input_para)