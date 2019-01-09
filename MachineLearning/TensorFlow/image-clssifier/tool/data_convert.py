# coding:utf-8
# 2019-1-6
# 图片转换为tfrecord数据格式

from __future__ import absolute_import
import argparse
import os
import logging
from tfrecord import main


input_para = {
    'train_dir' : '',
    'test_dir' : '',
    'output_dir' : '',
    'label_output' : '',
    'train-shards' : 2,
    'validation-shards' : 2,
    'num-threads' : 2,
    'dataset-name' : 'datatset'
}


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    labels_file = os.path.join(input_para['label_output'], 'label.txt')
    if os.path.exists(labels_file) is False:
        logging.warning('Can\'t find label.txt. Now create it.')
        all_entries = os.listdir(input_para['train_dir'])
        dirnames = []
        for entry in all_entries:
            if os.path.isdir(os.path.join(input_para['train_dir'], entry)):
                dirnames.append(entry)
        with open(labels_file, 'w') as f:
            for dirname in dirnames:
                f.write(dirname + '\n')
    main(input_para)