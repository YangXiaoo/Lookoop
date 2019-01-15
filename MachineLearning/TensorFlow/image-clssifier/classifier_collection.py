# coding:UTF-8
# 2019-1-15

from export_interference_graph import main as export_graph_main
from freeze_graph import main as freeze_graph_main
from train_image_classifier import main as train_main

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
    'tfrecord_output' :  r'C:\Study\test\kaggle-bonage\tf_record',
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

    # vgg_16
    # 'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\vgg_16.ckpt', # None
    # 'checkpoint_exclude_scopes' : 'vgg_16/fc6,vgg_16/fc7,vgg_16/fc8', # 不加载的节点


    # mobilenet_v2_1.4_224
    # 'checkpoint_path' : r'C:\Study\github\others\finetuning\mobilenet_v2_1.4_224\mobilenet_v2_1.4_224.ckpt',
    # 'checkpoint_exclude_scopes' :  '',

    # # nasnet
    # 'checkpoint_path' : r'C:\Study\github\others\finetuning\nasnet-a_large_04_10_2017\model.ckpt',
    # 'checkpoint_exclude_scopes' :  'cell_17/', # finetuning

    # # pnasnet
    # 'checkpoint_path' : r'C:\Study\github\others\finetuning\pnasnet-5_large_2017_12_13\model.ckpt',
    # 'checkpoint_exclude_scopes' : '',


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

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\vgg_16.ckpt', # None
	    'checkpoint_exclude_scopes' : 'vgg_16/fc6,vgg_16/fc7,vgg_16/fc8', # 不加载的节点
	},

	# inception_v3
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_inception_v3',
		'model_name' : 'inception_v3',
		'train_image_size' : 229,

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\inception_v3.ckpt',
	    'checkpoint_exclude_scopes' : '',
	},

	# nasnet_large
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_nasnet_large',
		'model_name' : 'nasnet_large',
		'train_image_size' : 331,

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\nasnet_large.ckpt',
	    'checkpoint_exclude_scopes' : 'cell_17/',
	},

	# pnasnet_large
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_pnasnet_large',
		'model_name' : 'pnasnet_large',
		'train_image_size' : 331,

	    # Fine-Tuning
	    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\pretrained\pnasnet_large.ckpt',
	    'checkpoint_exclude_scopes' : '',
	},

	# resnet_v2_200
	{
		'train_dir' : r'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/train_resnet_v2_200',
		'model_name' : 'resnet_v2_200',
		'train_image_size' : 224,

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
        'output_node_names' : 'resnet_v2_200/predictions/Reshape_1', # resnet

        'input_saver' : '',
        'input_binary' : True, # bool

        'restore_op_name' : "save/restore_all",
        'filename_tensor_name' : "save/Const:0",
        'clear_devices' : True,
        'initializer_nodes' : '',
        'variable_names_blacklist' : '',
	}


def get_data(input_para):
	"""
	数据处理
	"""
	# 图片抽取整理并生成标签
    getlabels.main(input_para['pic_path'], 
			        input_para['csv_path'], 
			        input_para['train_male_output'],
			        input_para['train_female_output'], 
			        input_para['validation_male_output'],
			        input_para['validation_female_output'], 
			        input_para['lables_output'])




def data_augumentation(input_para):
    # 数据扩充
    # male
    male_label_path = os.path.join(input_para['train_male_output'], 'train.txt')
    male_labels = pic_data_augumentation.getLablesDict(male_label_path)
    pic_data_augumentation.augmentation(input_para['train_male_output'], 
								        input_para['augumentation_male_output'], 
								        male_labels, 
								        input_para['augumentation_male_lable_output'],
								        batch_size=1,
								        save_prefix='bone',
								        save_format='png')

    # female
    female_label_path = os.path.join(input_para['train_female_output'], 'train.txt')
    female_labels = pic_data_augumentation.getLablesDict(female_label_path)
    pic_data_augumentation.augmentation(input_para['train_female_output'], 
								        input_para['augumentation_female_output'], 
								        female_labels, 
								        input_para['augumentation_female_lable_output'],
								        batch_size=1,
								        save_prefix='bone',
								        save_format='png')



def data_split(input_para):
    # 划分训练集
    # male
    male_label_path = os.path.join(input_para['augumentation_male_label_output'], 'labels.txt') # 若数据没有扩充这里的路径需要修改
    male_labels_dict = disposal_data.getLabelsDict(male_label_path)
    disposal_data.disposal(input_para['augumentation_male_output'], 
    						input_para['male_split_output'], 
    						male_labels_dict,
    						k_fold=input_para['male_k_fold'])

    # female
    male_label_path = os.path.join(input_para['augumentation_female_label_output'], 'labels.txt')
    male_labels_dict = disposal_data.getLabelsDict(male_label_path)
    disposal_data.disposal(input_para['augumentation_female_output'], 
    						input_para['female_split_output'], 
    						male_labels_dict,
    						k_fold=input_para['female_k_fold'])



def data_convert_to_tfrecord(input_para):
    # 数据格式转换
    # male
    male_train_dir = input_para['male_split_output']
    tfrecord_output = input_para['tfrecord_output']
    split_entries = os.listdir(male_train_dir)

    tfrecord_files = [] # tfrecord数据路径 [tfrecord, train_data_dir, validation_data_dir]
    for s in split_entries:
    	sub_dir = os.path.join(male_train_dir, str(s))
    	sub_tfrecord = os.path.join(tfrecord_output, str(s))
    	api.mkdirs(sub_tfrecord)
    	
    	train_data_dir = os.path.join(sub_dir, 'train')
    	labels_file = os.path.join(sub_tfrecord, 'labels.txt')
    	data_convert.get_class_labels(train_data_dir, labels_file)
    	validation_data_dir = os.path.join(sub_dir, 'test')
    	tfrecord_files.append([s, sub_tfrecord, train_data_dir, validation_data_dir])

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
    	
    np.save('tfrecord_files.npy', tfrecord_files) # 存储数据到本地




def run_model(input_para, network_setting):
	input_para = input_para.copy()
	tfrecord_files = np.load('tfrecord_files.npy')
	for k,v in network_setting.items():
		input_para[k] = v

	model_index = []  # [dst_train_dir, data_split_name, tfrecord, validation_data_dir]
	tmp_train_dir = os.path.join(input_para['train_dir'], network_setting['model_name'])
	for x in tfrecord_files:
		input_para['dataset_dir'] = x[1]
		input_para['train_dir'] = os.path.join(tmp_train_dir, str(x[0]))
		model_index.append([input_para['train_dir'], x[0], x[1], x[3]])
		train_main(input_para)

	np.save(os.path.join(tmp_train_dir,'model_index.npy'), model_index) # train_dir/model_name/data_split_name



def convert_model(network_setting, model_save_para, input_para):
	model_save_para = model_save_para.copy()
	model_save_para['model_name'] = network_setting['model_name']
	model_save_para['default_image_size'] = network_setting['train_image_size']
	model_save_para['dataset_name'] = input_para['dataset_name']
	model_save_para['labels_offset'] = input_para['labels_offset']
	model_save_para['data_split'] = input_para['test_split_name']

	model_dir = os.path.join(input_para['train_dir'], network_setting['model_name'],'model_index.npy')
	model_index = np.load(model_dir)
	for v in model_index:
		tmp_train_dir = os.path.join(model_save_para['graph_dir'], network_setting['model_name'], v[0])
		model_save_para['graph_dir'] = os.path.join(tmp_train_dir, 'inf_graph.pb')
		model_save_para['dataset_dir'] = v[2]

		export_graph_main(model_save_para)
		
		model_save_para['input_checkpoint'] = api.get_checkpoint(tmp_train_dir)
		model_save_para['frozen_graph'] = os.path.join(tmp_train_dir, 'frozen_graph.pb')



