# coding:utf-8
# 2019-1-6
# 图片转换为tfrecord数据格式

from __future__ import absolute_import
import argparse
import os
import logging
from tfrecord import main


input_para = {
    'train_dir' : r'C:\Study\test\kaggle-bonage\train-male_disposal_out\0\train',
    'validation_dir' : r'C:\Study\test\kaggle-bonage\train-male_disposal_out\0\test', # 也可以为test

    'labels_file' : r'C:\Study\test\kaggle-bonage\tf_record\0\label.txt',

    'output_dir' : r'C:\Study\test\kaggle-bonage\tf_record\0',
    'dataset_name' : 'datatset',
    'train_shards' : 2,
    'validation_shards' : 2,
    'num_threads' : 2,
    'class_label_base' : 0,
}

def get_class_labels(train_dir, labels_file):
    logging.basicConfig(level=logging.INFO)
    if os.path.exists(labels_file) is False:
        logging.warning('Can\'t find label.txt. Now create it.')
        all_entries = os.listdir(train_dir)
        dirnames = []
        for entry in all_entries:
            if os.path.isdir(os.path.join(train_dir, entry)):
                dirnames.append(entry)
        label_dir = os.path.split(labels_file)[0]
        if not os.path.isdir(label_dir):
            os.makedirs(label_dir)
        with open(labels_file, 'w') as f:
            for dirname in dirnames:
                f.write(dirname + '\n')

    labels_file
    return 
if __name__ == '__main__':
    get_class_labels(input_para['train_dir']), input_para['labels_file']
    main(input_para)