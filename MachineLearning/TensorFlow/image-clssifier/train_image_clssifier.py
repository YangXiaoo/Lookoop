# coding:UTF-8
# 2019-1-6
# image clssifier

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from datasets import dataset_factory
from deployment import model_deploy
from nets import nets_factory
from preprocessing import preprocessing_factory

slim = tf.contrib.slim 

# parameters
input_para = {
	'master' : '',
	'train+dir' : '', # 存放节点和日志

	'num_clones' : 1 # 部署平台个数
	'clone_on_cpu' : True, # 是否部署在CPU上
	'worker_replicas' : 1,
	'num_ps_tasks' : 0,
	'num_readers' : 4, 
	'num_preprocessing_threads' : 4,
	'log_every_n_steps' : 10,
	'save_summaries_secs' : 600,
	'task' : 0, 


	# Optimization
	'weight_decay' : 0.00004,
	'opt_epsilon', 1.0, # Epsilon term for the optimizer

	# 'The name of the optimizer, one of 
	# "adadelta", "adagrad", "adam", "ftrl", "momentum", "sgd" or "rmsprop".'
	'optimizer' : 'rmsprop', 

	'adadelta_rho' : 0.95, # The decay rate for adadelta
	'adagrad_initial_accumulator_value' : 0.1, # 'Starting value for the AdaGrad accumulators
	'adam_beta1' : 0.9, # The exponential decay rate for the 2nd moment estimates.

	'ftrl_learning_rate_power' : -0.5, # The learning rate power
	'ftrl_initial_accumulator_value' : 0.1, # Starting value for the FTRL accumulators
	'ftrl_l1' : 0.0, # The FTRL l1 regularization strength
	'ftrl_l2' : 0.0, # The FTRL l2 regularization strength

	'momentum' : 0.9, # The momentum for the MomentumOptimizer and RMSPropOptimizer
	'rmsprop_decay' : 0.9, # Decay term for RMSProp


	# Learning Rate
	# Specifies how the learning rate is decayed. 
	# One of "fixed", "exponential",  or "polynomial"
	'learning_rate_decay_type' : 'exponential', 
	'learning_rate' : 0.01, # Initial learning rate
	'end_learning_rate' : 0.0001, # The minimal end learning rate used by a polynomial decay learning rate
	'label_smoothing' : 0.0, # The amount of label smoothing
	'learning_rate_decay_factor' : 0.94, # Learning rate decay factor
	'num_epochs_per_decay' : 2.0, # Number of epochs after which learning rate decays
    'sync_replicas' : False, # Whether or not to synchronize the replicas during training
    'replicas_to_aggregate' : 1, # The Number of gradients to collect before updating params
    'moving_average_decay' : None, # The decay to use for the moving average. If left as None, then moving averages are not used


    # Dataset
    'dataset_name' : 'bone', # The name of the dataset to load
    'dataset_split_name' : 'train', # The name of the train/test split
    'dataset_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/data', # The directory where the dataset files are stored
    'labels_offset' : 0,  # An offset for the labels in the dataset. This flag is primarily used to  evaluate the VGG and ResNet architectures which do not use a background
    'model_name' : 'vgg_16', # The name of the architecture to train
    'preprocessing_name' : None, # The name of the preprocessing to use. If left as `None`, then the model_name flag is used
    'batch_size' : 2, # The number of samples in each batch
    'train_image_size' : 224, # 训练图片大小, None使用默认大小
    'max_number_of_steps' : None, # The maximum number of training steps


    # Fine-Tuning
    'checkpoint_path' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/pretrained/vgg_16.ckpt',
    'checkpoint_exclude_scopes' : 'fc6,fc7,fc8', #Comma-separated list of scopes of variables to exclude when restoring from a checkpoint
    'trainable_scopes' : None, # Comma-separated list of scopes to filter the set of variables to train. By default, None would train all the variables
    'ignore_missing_vars' : True, # When restoring a checkpoint would ignore missing variables
}


def main():
	"""
	训练入口
	"""
	tf.logging.set_verbosity(tf.logging.INFO) # 日志设置开始入口

	with tf.Graph().as_default(): # 实例化一个图

		# 部署环境初始化
		deploy_config = model_deploy.DeploymentConfig(
			num_clones=input_para['num_clones'],
			clone_on_cpu=input_para['clone_on_cpu'],
	        replica_id=input_para['task'],
	        num_replicas=input_para['num_replicas'],
	        num_ps_tasks=input_para['num_ps_tasks'])

    	# 设置运行的设备
    	with tf.device(deploy_config.variables_device()):
      		global_step = slim.create_global_step() # 迭代计数器


      	# 初始化训练数据
      	dataset = dataset_factory.get_dataset(
      		input_para['dataset_name'],
      		input_para['dataset_split_name'],
      		input_para['dataset_dir'])

      	# 选择训练模型
      	network_fn = nets_factory.get_network_fn(
        	input_para['model_name'],
        	num_classes=(dataset.num_classes - input_para['labels_offset']),
        	weight_decay=input_para['weight_decay'],
        	is_training=True)

      	# 选择预处理函数
    	preprocessing_name = input_para['preprocessing_name'] or input_para['model_name']
    	image_preprocessing_fn = preprocessing_factory.get_preprocessing(
        	preprocessing_name,
        	is_training=True)

    	# 设置数据加载, 主机加载数据
	    with tf.device(deploy_config.inputs_device()):
	      	provider = slim.dataset_data_provider.DatasetDataProvider(
	          	dataset,
	          	num_readers=input_para['num_readers'],
	          	common_queue_capacity=20 * input_para['batch_size'],
	          	common_queue_min=10 * input_para['batch_size'])
	      	# 获得图像数据和标签
	      	[image, label] = provider.get(['image', 'label'])
	      	label -= input_para['labels_offset']

	      	# 获得训练输入尺寸
	      	train_image_size = input_para['train_image_size'] or network_fn.default_image_size
	      	# 数据扩充
	      	image = image_preprocessing_fn(image, train_image_size, train_image_size)
	      	images, labels = tf.train.batch(
          		[image, label],
          		batch_size=input_para['batch_size'],
          		num_threads=input_para['num_preprocessing_thread']s,
          		capacity=5 * input_para['batch_size'])

	      	# 独热编码
	      	labels = slim.one_hot_encoding(
	          	labels, 
	          	dataset.num_classes - input_para['labels_offset'])
	      	batch_queue = slim.prefetch_queue.prefetch_queue(
	          	[images, labels], 
	          	capacity=2 * deploy_config.num_clones)


	    def clone_fn(batch_queue):
	      	"""
	      	在多个平台运行数据
	      	"""
	      	with tf.device(deploy_config.inputs_device()):
	        	images, labels = batch_queue.dequeue()
	      	logits, end_points = network_fn(images) # 模型训练输出网络和输出节点

	      	# 定义损失函数
	      	if 'AuxLogits' in end_points:
	        	tf.losses.softmax_cross_entropy(
	            	logits=end_points['AuxLogits'], 
	            	onehot_labels=labels,
	            	label_smoothing=input_para['label_smoothing'],
	            	weights=0.4, 
	            	scope='aux_loss')
	      	tf.losses.softmax_cross_entropy(
	          	logits=logits, 
	          	onehot_labels=labels,
	          	label_smoothing=input_para['label_smoothing'], 
	          	weights=1.0)
	      	return end_points


	    summaries = set(tf.get_collection(tf.GraphKeys.SUMMARIES))

