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

    'train_labels_file' : r'C:\Study\test\kaggle-bonage\tf_record\0\train_label.txt',
    'validation_labels_file' : r'C:\Study\test\kaggle-bonage\tf_record\0\validation_label.txt',

    'output_dir' : r'C:\Study\test\kaggle-bonage\tf_record\0',
    'dataset_name' : 'datatset',

    'train_shards' : 2,
    'validation_shards' : 2,
    'num_threads' : 2,
    'class_label_base' : 0,
}


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    group = [[input_para['train_labels_file'], input_para['train_dir']], 
        [input_para['validation_labels_file'], input_para['validation_dir']]]
    for g in group:
        label, dirs = g
        if os.path.exists(label) is False:
            logging.warning('Can\'t find label.txt. Now create it.')
            all_entries = os.listdir(dirs)
            dirnames = []
            for entry in all_entries:
                if os.path.isdir(os.path.join(dirs, entry)):
                    dirnames.append(entry)
            label_dir = os.path.split(label)[0]
            if not os.path.isdir(label_dir):
                os.makedirs(label_dir)
            with open(label, 'w') as f:
                for dirname in dirnames:
                    f.write(dirname + '\n')
    main(input_para)