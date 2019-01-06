# coding:UTF-8
# 2019-1-6
# kaggle-boneage 数据读区方法

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from six.moves import urllib
import tensorflow as tf

from datasets import dataset_utils

slim = tf.contrib.slim

_FILE_PATTERN = 'datasets_%s*'
LABELS_FILENAME = 'lable.txt'

_SPLITS_TO_SIZES = {
    'train': 680,
    'validation': 53,
}

_ITEMS_TO_DESCRIPTIONS = {
    'image': 'A color image of varying height and width.',
    'label': 'The label id of the image, integer between 1 and 18',
}

_NUM_CLASSES = 18


def read_label_file(dataset_dir, filename=LABELS_FILENAME):
  	"""
  	获得id对应的实际标签
  	"""
  	labels_filename = os.path.join(dataset_dir, filename)
  	with tf.gfile.Open(labels_filename, 'rb') as f:
    	lines = f.read().decode()
  	lines = lines.split('\n')
  	lines = filter(None, lines)

  	labels_to_class_names = {}
  	for line in lines:
    	labels_to_class_names[int(line)] = str(line) + '_years_old'
  	return labels_to_class_names


def get_split(split_name, dataset_dir, file_pattern=None, reader=None):
  """
  返回数据实例
  """
  	if split_name not in _SPLITS_TO_SIZES:
    	raise ValueError('split name %s was not recognized.' % split_name)

  	if not file_pattern:
    	file_pattern = _FILE_PATTERN
  	file_pattern = os.path.join(dataset_dir, file_pattern % split_name)

  	# Allowing None in the signature so that dataset_factory can use the default.
  	if reader is None:
    	reader = tf.TFRecordReader

  	keys_to_features = {
      	'image/encoded': tf.FixedLenFeature(
        	(), tf.string, default_value=''),
      	'image/format': tf.FixedLenFeature(
        	(), tf.string, default_value='jpeg'),
      	'image/class/label': tf.FixedLenFeature(
        	[], dtype=tf.int64, default_value=-1),
  	}

  	items_to_handlers = {
      	'image': slim.tfexample_decoder.Image('image/encoded', 'image/format'),
      	'label': slim.tfexample_decoder.Tensor('image/class/label'),
  	}

  	decoder = slim.tfexample_decoder.TFExampleDecoder(
      	keys_to_features, items_to_handlers)

  	labels_to_names = None
  	if tf.gfile.Exists(os.path.join(dataset_dir, LABELS_FILENAME)):
    	labels_to_names = read_label_file(dataset_dir)

  	return slim.dataset.Dataset(
      	data_sources=file_pattern,
      	reader=reader,
      	decoder=decoder,
      	num_samples=_SPLITS_TO_SIZES[split_name],
      	items_to_descriptions=_ITEMS_TO_DESCRIPTIONS,
      	num_classes=_NUM_CLASSES,
      	labels_to_names=labels_to_names)
