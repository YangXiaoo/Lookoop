# coding:UTF-8
# 2019-1-15

import os
import numpy as np 
import pickle

from export_inference_graph import main as export_graph_main
from freeze_graph import main as freeze_graph_main
from train_image_classifier import main as train_main
from test_image_classifier import run_inference_on_image

from tool import data_convert
from tool import disposal_data
from tool import get_data
from tool import pic_data_augmentation
from tool import tfrecord
from tool import api
from tool import regression


# tensorboard --logdir train_dir --port 8080

input_para = {
    # 数据抽取参数
    'pic_path' : r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset', # 原图像路径
    'csv_path' : r'C:\Users\Yauno\Downloads\rsna-bone-age\boneage-training-dataset.csv', # csv数据
    'train_male_output' : r'C:\Study\test\kaggle-bonage\train-male', # 图片, '\labels.txt'
    'train_female_output' : r'C:\Study\test\kaggle-bonage\train-female',
    'validation_male_output' : r'C:\Study\test\kaggle-bonage\validation-male', # 图片, '\labels.txt'
    'validation_female_output' : r'C:\Study\test\kaggle-bonage\validation-female',
    'lables_output' : r'C:\Study\test\kaggle-bonage', # '\male_lables.txt', '\female_lables.txt'


    # 数据扩充参数
    # male
    'augumentation_male_output' : r'C:\Study\test\kaggle-bonage\male_augument', # 扩充图像输出路径
    'augumentation_male_label_output' : r'C:\Study\test\kaggle-bonage\male_augument', # '\labels.txt'

    # female
    'augumentation_female_output' : r'C:\Study\test\kaggle-bonage\female_augument',
    'augumentation_female_label_output' : r'C:\Study\test\kaggle-bonage\female_augument',

    'aug_threshed' : 10, # 每个年龄图片数量超过这个值则不会扩充
    'aug_max_gen' : 5, # 默认单张图片扩充数量
    'distribution_ignore' : False, # 默认不忽略数据分布



    # k-fold 划分训练集
    # male
    'male_split_output' : r'C:\Study\test\kaggle-bonage\train-male_disposal_out', # K-fold输出路径
    'male_k_fold' : 5, # default 5
    # female 
    'female_split_output' : r'C:\Study\test\kaggle-bonage\train-female_disposal_out', 
    'female_k_fold' : 5, # default 5


    # data convert
    # male
    'male_tfrecord_output' :  r'C:\Study\test\kaggle-bonage\male_tf_record', # tfrecord输出路径
    'female_tfrecord_output' :  r'C:\Study\test\kaggle-bonage\male_tf_record',
    'train_split_name' : 'train',
    'test_split_name' : 'test', # 'validation'
    'tf_num_shards' : 2,
    'tf_num_threads' : 2,
    'dataset_name' : 'datasets', # 由此值在`\datasets`下找到对应数据解析函数
    'tf_class_label_base' : 0,



    # 训练
    'train_dir' : r'C:\Study\test\kaggle-bonage\train_dir_test', # 存放节点和日志

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
    'labels_offset' : 0,  # 标签偏移

    'num_classes' : 131, # 分类数量
    'split_to_size' : {'train': 5894, # 训练图片个数，自动更改该值
                        'test': 1407},

    # 'model_name' : '', # 使用时自动设置
    'preprocessing_name' : None, # 预处理函数名
    'batch_size' : 2, # batch size


    'max_number_of_steps' : 20, # 最大迭代次数


    # Fine-Tuning
    'ignore_missing_vars' : True, # W检查节点的时候忽略缺失值
}



net_factory = [
    # vgg_16
    {
        'model_name' : 'vgg_16', # 模型名称
        'train_image_size' : 224, # 训练尺寸
        'output_tensor_name' : 'vgg_16/fc8/squeezed', # 最后一层节点名称

        # Fine-Tuning
        'checkpoint_path' : None, # .ckpt微调文件路径
        'checkpoint_exclude_scopes' : 'vgg_16/fc6,vgg_16/fc7,vgg_16/fc8', # 不加载的节点
        'trainable_scopes' : None, # 微调模型重新训练范围
    },

    # inception_v3
    {
        'model_name' : 'inception_v3',
        'train_image_size' : 299,
        'output_tensor_name' : 'InceptionV3/Predictions/Reshape_1',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
        'trainable_scopes' : None,
    },


    # pnasnet_large
    {

        'model_name' : 'pnasnet_large',
        'train_image_size' : 331,
        'output_tensor_name' : 'final_layer/predictions',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
        'trainable_scopes' : None,
    },

    # resnet_v2_200
    {
        'model_name' : 'resnet_v2_200',
        'train_image_size' : 224,
        'output_tensor_name' : 'resnet_v2_200/predictions/Reshape_1',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
        'trainable_scopes' : None,
    },

    # nasnet_large
    {
        'model_name' : 'inception_resnet_v2',
        'train_image_size' : 299,
        'output_tensor_name' : 'InceptionResnetV2/Logits/Predictions',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : 'cell_17/',
        'trainable_scopes' : None,
    }
]

model_save_para = {
        'is_training' : False, #default
        'labels_offset' : 0,
        'graph_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/graph', # C:\Study\test\kaggle-bonage\graph
        'data_split' : 'test',
        'num_classes' : 131, # 分类数量
        'split_to_size' : {'train': 5894, # 训练图片个数，自动更改该值
                            'test': 1407},


        'input_checkpoint' : '', # default
        'frozen_graph' : '', # default
        'output_node_names' : '', # default

        'input_saver' : '', # default
        'input_binary' : True, # bool

        'restore_op_name' : "save/restore_all",
        'filename_tensor_name' : "save/Const:0",
        'clear_devices' : True,
        'initializer_nodes' : '', # default
        'variable_names_blacklist' : '', # default
    }


prediction_para = {
    'model_path' : '', # default
    'label_path' : '', # 所有训练数据的标签, default
    'image_file' : '', # auto
    'is_save' : True,
    'width' : 224, # auto
    'height' : 224, # auto
    'prediction_output' : r'C:\Study\test\kaggle-bonage\prediction_output' # C:\Study\test\kaggle-bonage\prediction_output
}


 