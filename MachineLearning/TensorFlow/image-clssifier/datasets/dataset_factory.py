# coding:utf-8
# 2019-1-6
# dataset factory
# 数据读取入口

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datasets import bone

datasets_map = {
	'bone' : bone,
	'datasets' : bone,
}

def get_dataset(name, split_name, dataset_dir, file_pattern=None, reader=None):
	"""
	name : 指定数据读取函数, datasets_map中的key
	split_name : 读取TFRecord时分隔训练数据与测试数据
	dataset_dir : 数据路径
	file_pattern : 数据匹配模式
	reader : 数据读取方法

	return: dataset class
	"""
	if name not in datasets_map:
		raise ValueError("不存在该数据读取方法, 查看datasets文件中是否存在 %s 方法的文件" % name)
	return datasets_map[name].get_split(
		split_name,
      	dataset_dir,
      	file_pattern,
      	reader)