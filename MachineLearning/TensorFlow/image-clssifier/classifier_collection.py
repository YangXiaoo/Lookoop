# coding:UTF-8
# 2019-1-15

from export_interference_graph import main as export_graph_main
from freeze_graph import main as freeze_graph_main
from train_image_classifier import main as train_main
from test_image_classifier import run_inference_on_image

from tool import data_convert
from tool import disposal_data
from tool import getlabels
from tool import pic_data_augumentation
from tool import tfrecord
from tool import api

input_para = {

	# 数据抽取参数
    'pic_path' : r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset', # 原图像路径
    'csv_path' : r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset.csv', # csv数据
    'train_male_output' : r'C:\Study\test\kaggle-bonage\train-male', # 图片, '\train.txt'
    'train_female_output' : r'C:\Study\test\kaggle-bonage\train-female',
    'validation_male_output' : r'C:\Study\test\kaggle-bonage\validation-male', # 图片, '\validation.txt'
    'validation_female_output' : r'C:\Study\test\kaggle-bonage\validation-female',
    'lables_output' : r'C:\Study\test\kaggle-bonage', # '\male_lables.txt', '\female_lables.txt'


    # 数据扩充参数
    # male
    'augumentation_male_output' : r'C:\Study\test\kaggle-bonage\test', # picture files
    'augumentation_male_label_output' : r'C:\Study\test\kaggle-bonage\test', # '\labels.txt'

    # female
    'augumentation_female_output' : r'C:\Study\test\kaggle-bonage\test',
    'augumentation_female_label_output' : r'C:\Study\test\kaggle-bonage\test',


    # k-fold 划分训练集
    # male
    'male_split_output' : r'C:\Study\test\kaggle-bonage\train-male_disposal_out',
    'male_k_fold' : 5, # default 5
    # female 
    'female_split_output' : r'C:\Study\test\kaggle-bonage\train-female_disposal_out', 
    'female_k_fold' : 5, # default 5
    # .*_split_output 文件下的结构: 
    # '\0\train\pic.png'
    # '\0\test\pic.png'
    # ...
    # '\1\train\pic.png'
    # '\1\test\pic.png'
    # ...

    # data convert
    # male
    'male_tfrecord_output' :  r'C:\Study\test\kaggle-bonage\tf_record',
    'female_tfrecord_output' :  r'C:\Study\test\kaggle-bonage\tf_record',
    'train_split_name' : 'train',
    'test_split_name' : 'test', # 'validation'
    'tf_num_shards' : 2,
    'tf_num_threads' : 2,
    'dataset_name' : 'datasets',
    'tf_class_label_base' : 0,



    # 训练
    'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_dir_resnet', # 存放节点和日志

    'master' : '',
    'num_clones' : 1, # 部署平台个数
    'clone_on_cpu' : True, # 是否部署在CPU上
    'worker_replicas' : 1,
    'num_ps_tasks' : 0,
    'num_readers' : 4, 
    'num_preprocessing_threads' : 4,
    'log_every_n_steps' : 10,
    'save_summaries_secs' : 600,
    'save_interval_secs':600,
    'task' : 0, 


    # 优化设置
    'weight_decay' : 0.00004,
    'opt_epsilon' : 1.0,


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


    # 数据设置
    # 'dataset_name' : 'bone', # 加载数据集的模块名，上面数据集已经设置
    'dataset_split_name' : 'train', # 划分数据集的名称
    'dataset_dir' : '',
    'labels_offset' : 0,  # 标签偏移

    'model_name' : '',
    'preprocessing_name' : None, # 预处理
    'batch_size' : 2, # batch size
    'train_image_size' : 224, # default



    'max_number_of_steps' : 10000, # 最大迭代次数


    # Fine-Tuning
    # default
    'checkpoint_path' : None,
    'checkpoint_exclude_scopes' :  '',
    'trainable_scopes' : None, # 默认训练所有节点
    'ignore_missing_vars' : True, # W检查节点的时候忽略缺失值
}



train_para = [
	# vgg_16
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_vgg_16', # 存放节点和日志
		'model_name' : 'vgg_16', # vgg
		'train_image_size' : 244, # vgg_16
		'output_tensor_name' : 'vgg_16/fc8/squeezed',

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\vgg_16.ckpt', # None
	    'checkpoint_exclude_scopes' : 'vgg_16/fc6,vgg_16/fc7,vgg_16/fc8', # 不加载的节点
	},

	# inception_v3
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_inception_v3',
		'model_name' : 'inception_v3',
		'train_image_size' : 229,
		'output_tensor_name' : 'InceptionV3/Predictions/Reshape_1',

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\inception_v3.ckpt',
	    'checkpoint_exclude_scopes' : '',
	},

	# nasnet_large
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_nasnet_large',
		'model_name' : 'nasnet_large',
		'train_image_size' : 331,
		'output_tensor_name' : 'final_layer/predictions',

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\nasnet_large.ckpt',
	    'checkpoint_exclude_scopes' : 'cell_17/',
	},

	# pnasnet_large
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_pnasnet_large',
		'model_name' : 'pnasnet_large',
		'train_image_size' : 331,
		'output_tensor_name' : 'final_layer/predictions',

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\pnasnet_large.ckpt',
	    'checkpoint_exclude_scopes' : '',
	},

	# resnet_v2_200
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_resnet_v2_200',
		'model_name' : 'resnet_v2_200',
		'train_image_size' : 224,
		'output_tensor_name' : 'resnet_v2_200/predictions/Reshape_1',

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\resnet_v2_200.ckpt',
	    'checkpoint_exclude_scopes' : '',
	},
]

model_save_para = {
	    'is_training' : False,
	    'default_image_size' : 224, 
	    'dataset_name' : '',
	    'labels_offset' : 0,
	    'graph_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/graph', # resnet
	    'data_split' : 'test',
	    'dataset_dir' : '', # 处理后TF格式的数据集

        'input_checkpoint' : '', # ckpt模型
        'frozen_graph' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\graph', # resnet
        'output_node_names' : '', # resnet

        'input_saver' : '',
        'input_binary' : True, # bool

        'restore_op_name' : "save/restore_all",
        'filename_tensor_name' : "save/Const:0",
        'clear_devices' : True,
        'initializer_nodes' : '',
        'variable_names_blacklist' : '',
	}


prediction_para = {
    'model_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\resnet_frozen_graph.pb', # graph_dir
    'label_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\data\label.txt', # 所有训练数据的标签
    'image_file' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\row_data\train\2',
    'tensor_name' : 'resnet_v2_200/predictions/Reshape_1:0',
    'width' : 224,
    'height' : 224,
    'prediction_output' : r'C:\Study\test\tensorflow-bone\prediction_output'
}


def get_data(pic_path, 
	        csv_path, 
	        train_male_output,
	        train_female_output, 
	        validation_male_output,
	        validation_female_output, 
	        lables_output):
	"""
	数据处理
	"""
	# 图片抽取整理并生成标签
	getlabels.main(pic_path, 
			        csv_path, 
			        train_male_output,
			        train_female_output, 
			        validation_male_output,
			        validation_female_output, 
			        lables_output)


def data_augumentation(input_path, 
		                output_path, 
		                lable_path, 
		                lable_output_path,
		                batch_size=1,
		                save_prefix='bone',
		                save_format='png')
    # 数据扩充
    lables = pic_data_augumentation.getLablesDict(lable_path)
    pic_data_augumentation.augmentation(input_path, 
						                output_path, 
						                lables, 
						                lable_output_path,
						                batch_size=1,
						                save_prefix='bone',
						                save_format='png')



def data_split(input_dir, output_dir, label_path, k_fold=5):
    # 划分训练集
    labels_dict = disposal_data.getLabelsDict(label_path)
    disposal_data.disposal(input_dir, 
					    	output_dir, 
					    	labels_dict
					    	k_fold=k_fold)



def data_convert_to_tfrecord(train_dir, 
							tfrecord_output,
							**input_para):
    # 数据格式转换

    split_entries = os.listdir(train_dir)

    # tfrecord_files = [] # tfrecord数据路径 [calss_name, tfrecord, train_data_dir, validation_data_dir]
    for s in split_entries:
    	sub_dir = os.path.join(train_dir, str(s))
    	sub_tfrecord = os.path.join(tfrecord_output, str(s))
    	api.mkdirs(sub_tfrecord)
    	
    	train_data_dir = os.path.join(sub_dir, 'train')
    	labels_file = os.path.join(sub_tfrecord, 'labels.txt')
    	data_convert.get_class_labels(train_data_dir, labels_file)
    	validation_data_dir = os.path.join(sub_dir, 'test')
    	# tfrecord_files.append([s, sub_tfrecord, train_data_dir, validation_data_dir])

    	tfrecord.process_dataset(input_para['train_split_name'], 
    							train_data_dir,
    							input_para['tf_num_shards'],
    							labels_file,
    							input_para['tf_num_threads'],
    							sub_tfrecord,
    							input_para['dataset_name'],
    							input_para['tf_class_label_base'])


    	tfrecord.process_dataset(input_para['test_split_name'], 
    							validation_data_dir,
    							input_para['tf_num_shards'],
    							labels_file,
    							input_para['tf_num_threads'],
    							sub_tfrecord,
    							input_para['dataset_name'],
    							input_para['tf_class_label_base'])
    	
    # np.save('tfrecord_files.npy', tfrecord_files) # 存储数据到本地




def run_model(tfrecord_output, **input_para, **network_setting):
	input_para = input_para.copy()
	tfrecord_files = os.listdir(tfrecord_output)
	for k,v in network_setting.items():
		input_para[k] = v

	tmp_train_dir = os.path.join(input_para['train_dir'], network_setting['model_name'])
	for s in tfrecord_files:
		input_para['dataset_dir'] = os.path.join(tfrecord_output, str(s))
		input_para['train_dir'] = os.path.join(tmp_train_dir, str(s))


def convert_model(train_dir,
				tfrecord_output,
				network_setting, 
				model_save_para, 
				input_para):
	model_save_para = model_save_para.copy()
	model_save_para['model_name'] = network_setting['model_name']
	model_save_para['default_image_size'] = network_setting['train_image_size']
	model_save_para['dataset_name'] = input_para['dataset_name']
	model_save_para['labels_offset'] = input_para['labels_offset']
	model_save_para['data_split'] = input_para['test_split_name']

	tmp_train_dir = os.path.join(train_dir, network_setting['model_name'])
	model_index = os.listdir(tmp_train_dir)

	graph_dir = os.path.join(model_save_para['graph_dir'], network_setting['model_name'])


	for s in model_index:
		tmp_graph_dir = os.path.join(graph_dir, str(s))
		model_save_para['graph_dir'] = os.path.join(tmp_graph_dir, 'inf_graph.pb')
		model_save_para['dataset_dir'] = os.path.join(tfrecord_output, str(s))

		export_graph_main(model_save_para)

		tmp_model_ckpt = os.path.join(train_dir, )
		model_save_para['input_checkpoint'] = api.get_checkpoint(v[0])
		model_save_para['frozen_graph'] = os.path.join(tmp_train_dir, 'frozen_graph.pb')

		model_save_para['output_node_names'] = network_setting['output_tensor_name']

		freeze_graph_main(model_save_para)
		graph_index.append([v[1], v[3], model_save_para['frozen_graph'], output_node_names + ":0"])
	np.save(os.path.join(graph_dir, 'graph_index.npy'), graph_index)


def prediction_data(prediction_para, 
					network_setting, 
					graph_dir,
					test_data,
					label_path):
	"""
	graph_dir: 所有graph的路径
	"""
	prediction_para = prediction_para.copy()
	graph_index_dir = os.path.join(graph_dir, network_setting['model_name'])
	class_labels = os.listdir(graph_index_dir)
	prediction_para['label_path'] = label_path
	for c in class_labels:
		test_data_dir = os.path.join(test_data, c, 'test')
		prediction_para['image_file'] = test_data_dir
		model_path = os.path.join(graph_index_dir, c, 'frozen_graph.pb')
		prediction_para['model_path'] = model_path
		prediction_para['tensor_name'] = network_setting['output_tensor_name']
		prediction_para['width'] = network_setting['train_image_size']
		prediction_para['height'] = network_setting['train_image_size']
		prediction_para['prediction_output'] = os.path.join(prediction_para['prediction_output'], network_setting['model_name'], c)

		run_inference_on_image(prediction_para)



if __name__ == '__main__':
	# 抽取数据
	get_data(input_para['pic_path'], 
	        input_para['csv_path'], 
	        input_para['train_male_output'],
	        input_para['train_female_output'], 
	        input_para['validation_male_output'],
	        input_para['validation_female_output'], 
	        input_para['lables_output'])

	# 数据扩充
	label_path = os.path.join(input_para['train_male_output'], 'labels.txt')
	data_augumentation(input_para['train_male_output'], 
		                input_para['augumentation_male_output'], 
		                lable_path, 
		                input_para['augumentation_male_label_output'],
		                batch_size=1,
		                save_prefix='bone',
		                save_format='png')

	# 数据划分
	label_path = os.path.join(input_para['augumentation_male_label_output'], 'labels.txt')
	data_split(input_para['augumentation_male_output'], 
		input_para['male_split_output'], 
		label_path, 
		k_fold=input_para['male_k_fold'])

	# 数据格式转换
    # male
    train_dir = input_para['male_split_output']
    tfrecord_output = input_para['male_tfrecord_output']
	data_convert_to_tfrecord(train_dir, 
							tfrecord_output,
							**input_para):