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


    'max_number_of_steps' : 100, # 最大迭代次数


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
        'train_image_size' : 229,
        'output_tensor_name' : 'InceptionV3/Predictions/Reshape_1',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
        'trainable_scopes' : None,
    },

    # nasnet_large
    {
        'model_name' : 'nasnet_large',
        'train_image_size' : 331,
        'output_tensor_name' : 'final_layer/predictions',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : 'cell_17/',
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


def data_split(input_dir, 
                output_dir, 
                label_path, 
                k_fold=5):
    """
    划分训练集
    Args:
        input_dir: 待划分的数据集路径
        output_dir: 划分保存目录,按照k-fold数量生成不同文件夹, 并在每个文件夹下面生成train和test文件夹
        label_path: 带划分数据集对应标签
                    pic.jpeg class_name
                    pic.jpeg class_name
                    ...
        k_fold: 划分数量

    Returns:
        input_dir/0/train/pic_0.jpeg
                 /0/train/pic_1.jpeg
                 /0/test/pic_2.jpeg
                 /0/test/pic_3.jpeg
                 ...
                 /1/train/pic_0.jpeg
                 /1/train/pic_1.jpeg
                 /1/test/pic_0.jpeg
                 /1/test/pic_1.jpeg
                 ...
                 /k_fold/train/jpeg
                 /k_fold/test/jpeg
    """
    # 划分训练集
    print("split data...")
    api.mkdirs(output_dir)
    labels_dict = disposal_data.getLabelsDict(label_path)
    disposal_data.disposal(input_dir, 
                            output_dir, 
                            labels_dict,
                            k_fold=k_fold)



def data_convert_to_tfrecord(train_dir, 
                            tfrecord_output,
                            input_para):
    """
    数据转换为TFRecord格式
    Args:
        train_dir: 需要转换的数据集路径
        tfrecord_output: 输出路径
        input_para: type(dict)

    Returns:
        tfrecod_dir/`input_para['dataset_name']`_`input_para['train_split_name']`_\
                    `range(input_para['tf_num_shards'])`_of_\
                    `input_para['tf_num_shards']`.tfrecord
    """
    split_entries = os.listdir(train_dir)

    for s in split_entries:
        sub_dir = os.path.join(train_dir, str(s))
        sub_tfrecord = os.path.join(tfrecord_output, str(s))
        api.mkdirs(sub_tfrecord)
        
        train_data_dir = os.path.join(sub_dir, 'train')
        labels_file = os.path.join(sub_tfrecord, 'labels.txt')
        data_convert.get_class_labels(train_data_dir, labels_file)
        validation_data_dir = os.path.join(sub_dir, 'test')

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


def run_model(tfrecord_output, 
                original_dir,
                input_para, 
                network_setting):
    """
    训练模型使用`train_image_classifier.py`中的main()函数进行训练
    使用一个模型对tfrecord_ouput下所有待训练数据进行训练，有多少个不同的tfrecord数据就训练多少次,
    模型保存在input_para['train_dir']下
    Args:
        tfrecord_output: 待训练的tfrecord格式文件
        original_dir: tfrecord数据的原目录
        input_para: typr(dict)
        network_setting: type(dict), 一个模型的信息

    Returns:
        None
    """
    input_para = input_para.copy()
    tfrecord_files = os.listdir(tfrecord_output)
    for k,v in network_setting.items():
        input_para[k] = v

    tmp_train_dir = os.path.join(input_para['train_dir'], network_setting['model_name'])
    api.mkdirs(tmp_train_dir)
    lower = 4
    for k, s in enumerate(tfrecord_files):
        if k < lower:
            print("[INFO] skip model %s, training on data %s" % (network_setting['model_name'], s))
            continue
        print("[INFO] Use model %s, training on data %s" % (network_setting['model_name'], s))
        tmp_data_original = os.path.join(original_dir, str(s), 'train')
        train_size = len(api.get_files(tmp_data_original))
        tmp_dataset_dir = os.path.join(tfrecord_output, str(s))
        tmp_class_train_dir = os.path.join(tmp_train_dir, str(s))
        api.mkdirs([tmp_dataset_dir, tmp_class_train_dir])
        input_para['dataset_dir'] = tmp_dataset_dir
        input_para['train_dir'] = tmp_class_train_dir
        input_para['split_to_size']['train'] = train_size
        train_main(input_para)


def convert_model(train_dir,
                    test_data_dir,
                    tfrecord_output,
                    network_setting, 
                    model_save_para, 
                    input_para): 
    """
    将训练好的模型转换为graph文件，方便数据预测
    `export_inference_graph.py`中的main()函数定义输出输入接口
    `freeze_graph.py`中的main保存最终的graph文件. 保存目录 mpdele_save_para['graph_dir']/network_setting['model_name']
    Args:
        train_dir: 保存训练模型的总路径
        test_dsat_dir: 原格式的待预测数据路径
        tfrecord_output: tfrecord格式的待预测数据路径
        network_setting: type(dict)
        model_save_para: type(dict)
        input_para: typr(dict)
    Returns: None
    """
    model_save_para = model_save_para.copy()
    model_save_para['model_name'] = network_setting['model_name']
    model_save_para['default_image_size'] = network_setting['train_image_size']
    model_save_para['dataset_name'] = input_para['dataset_name']
    model_save_para['labels_offset'] = input_para['labels_offset']
    model_save_para['data_split'] = input_para['test_split_name']

    tmp_train_dir = os.path.join(train_dir, network_setting['model_name'])
    model_index = os.listdir(tmp_train_dir)

    tmp_test_data_dir = os.path.join(test_data_dir, network_setting['model_name'])

    graph_dir = os.path.join(model_save_para['graph_dir'], network_setting['model_name'])
    api.mkdirs(graph_dir)

    for s in model_index:
        tmp_test_class_dir = os.path.join(tmp_test_data_dir, str(s), 'test')
        tmp_test_data_size = len(api.get_files(tmp_test_class_dir))
        model_save_para['split_to_size']['test'] = tmp_test_data_size
        tmp_graph_dir = os.path.join(graph_dir, str(s))
        api.mkdirs(tmp_graph_dir)
        model_save_para['graph_dir'] = os.path.join(tmp_graph_dir, 'inf_graph.pb')
        model_save_para['dataset_dir'] = os.path.join(tfrecord_output, str(s))

        export_graph_main(model_save_para)

        tmp_model_ckpt = os.path.join(tmp_train_dir, str(s))
        model_save_para['input_checkpoint'] = api.get_checkpoint(tmp_model_ckpt)

        model_save_para['frozen_graph'] = os.path.join(tmp_graph_dir, 'frozen_graph.pb')

        model_save_para['output_node_names'] = network_setting['output_tensor_name']

        freeze_graph_main(model_save_para)



def prediction_train_data(graph_dir,
                            test_dir,
                            label_path,
                            prediction_para, 
                            network_setting):
    """
    对test_dir下的所有数据进行预测并将结果保存在 prediction_para['prediction_output']/network_setting['model_name']下
    Args:
        graph_dir: 所有graph的路径
        test_dir: 待预测数据路径
        label_path: 待预测数据的标签路径
        prediction_para: type(dict)
        network_setting: type(dict)

    Returns: None
    """
    prediction_ret = {}
    prediction_para = prediction_para.copy()
    graph_index_dir = os.path.join(graph_dir, network_setting['model_name'])
    class_labels = os.listdir(graph_index_dir)
    prediction_para['label_path'] = label_path
    tmp_model_prediction = os.path.join(prediction_para['prediction_output'], network_setting['model_name'])
    for c in class_labels:
        test_data_dir = os.path.join(test_dir, c, 'test')
        prediction_para['image_file'] = test_data_dir
        model_path = os.path.join(graph_index_dir, c, 'frozen_graph.pb')
        prediction_para['model_path'] = model_path
        prediction_para['tensor_name'] = network_setting['output_tensor_name'] + ":0"
        prediction_para['width'] = network_setting['train_image_size']
        prediction_para['height'] = network_setting['train_image_size']
        prediction_dir = os.path.join(tmp_model_prediction, c)
        api.mkdirs(prediction_dir)
        prediction_para['prediction_output'] = os.path.join(prediction_dir, 'prediction.npy') # 创建文件夹.

        tmp_prediction = run_inference_on_image(prediction_para)
        prediction_ret = dict(prediction_ret, **tmp_prediction)
    return prediction_ret


def get_prediction_data(prediction_output):
    """
    获得所有预测数据和对应标签
    Args:
        prediction_output:所有预测数据的路径

    Returns:
        train_data: type(list)
        labels: type(list)
    """
    model_name = os.listdir(prediction_output)
    split_name = os.listdir(os.path.join(prediction_output, model_name[0]))

    train_data, labels = [], []
    for s in split_name:
        tmp_test_data, tmp_test_labels = {}, []
        for m in model_name:
            tmp_data_path = os.path.join(prediction_output, m, s, 'prediction.npy')
            print("[INFO] Loading %s" % tmp_data_path)
            tmp_data = np.load(tmp_data_path) # {class_pic, data}
            for k,v in tmp_data[()].items():
                if k not in tmp_test_data:
                    tmp_test_data[k] = []

                tmp_test_data[k].extend(v) # {pic:[prediction_1, prediction_2, ]}
        for k,v in tmp_test_data.items():
            train_data.append(v)
            try:
                label = int(k.split('_')[0])
            except:
                label = int(k.split('_')[1])
            labels.append(label)

    return train_data, labels


def train_model(train_data, labels):
    """
    基于stacking, 训练融合模型, 使用softmax训练数据
    Args:
        train_data：type(list)训练数据
        labels: type(list) 训练标签

    Returns:
        model: 训练好的模型
    """
    # num_classes = len(set(labels))
    feature = np.mat(train_data)
    num_classes = feature.shape[1]
    labels = np.mat(labels).T
    print(feature.shape, labels.shape)
    # print(feature, labels)
    softmax = regression.softmax_classifier(feature, labels, num_classes, 10000, 0.2)
    softmax.train()
    np.save("weights.npy", softmax.weights)
    np.save("train_model.npy", softmax)

    return softmax


def model_single_prediction(test_data, 
                            label_path,
                            graph_dir, 
                            model_name, 
                            tensor_name,
                            image_size):
    """
    同一个模型对数据进行测试并取均值

    Args:
        test_data : 待测试数据路径
        label_path ： 待测试数据标签路径
        graph_dir ： 模型graph目录
        model_name ： 当前使用的模型名
        tensor_name : 当前模型输出节点的张量名
        image_size : 当前模型需要的输入尺寸
    Returns:
        predition: type(dict), {'pic':[prediction], ...}
    """
    model_graph_dir = os.path.join(graph_dir, model_name)
    class_list = os.listdir(model_graph_dir)
    prediction_para['label_path'] = label_path
    prediction_para['image_file'] = test_data
    prediction = {} # '{pic:array(prediction_data)}'
    for s in class_list:
        model_path = os.path.join(model_graph_dir, s, 'frozen_graph.pb')
        prediction_para['model_path'] = model_path
        prediction_para['tensor_name'] = tensor_name
        prediction_para['width'] = image_size
        prediction_para['height'] = image_size
        prediction_para['is_save'] = False
        tmp_model_prediction = run_inference_on_image(prediction_para)
        for k,v in tmp_model_prediction.items():
            if k not in prediction:
                prediction[k] = []
            try:
                prediction[k] = prediction[k].extend(v)
            except Exception as e:
                print("[Error] %s" % str(e))
                print("[INFO] Currur value: ", prediction )

    count = len(class_list)
    for k,v in prediction.items():
        prediction[k] = v / count

    return prediction


def model_collection_prediction(prediction_model, 
                                test_data, 
                                label_path,
                                graph_dir, 
                                model_list):
    """
    对测试集进行预测

    Args: 
        prediction_model : 训练好的模型
        test_data：待测试数据路径
        label_path ： 待测试数据标签
        graph_dir ： 模型graph文件目录
        model_list : type(list), [[model_name, tensor_name, image_size], [model_name, tensor_name, image_size],...]

    Returns: None
    """
    prediction_collection = {}
    for model_name, tensor_name, image_size in model_list:
        tmp_model_prediction = model_single_prediction(test_data, 
                                                        label_path,
                                                        graph_dir, 
                                                        model_name, 
                                                        tensor_name,
                                                        image_size)
        for k,v in tmp_model_prediction.items():
            if k not in prediction_collection:
                prediction_collection[k] = np.array([])
            prediction_collection[k] = np.append(prediction_collection[k], v)


    test_feature, test_labels = [], []
    for k,v in prediction_collection.items():
        test_feature.append(v) 
        test_labels.append(int(k.split('_')[0]))

    test_feature, test_labels = np.mat(test_feature), np.mat(test_labels).T
    prediction_model.prediction(test_feature, test_labels) # 打印出结果



if __name__ == '__main__':
    # 抽取数据
    threshed = input_para['male_k_fold']
    train_size = 0.9
    # male_ret, female_ret = get_data.main(input_para['pic_path'], 
    #                                      input_para['csv_path'], 
    #                                      input_para['train_male_output'],
    #                                      input_para['train_female_output'], 
    #                                      input_para['validation_male_output'],
    #                                      input_para['validation_female_output'], 
    #                                      input_para['lables_output'],
    #                                      train_size=train_size,
    #                                      threshed=threshed,
    #                                      is_write=True)


    # # 不进行数据扩充
    # # 由数据抽取返回的结果中获得需要扩展的图片路径和对应标签
    # input_file_list = []
    # output, files, labels = male_ret
    # for f, out_dir in files:
    #     input_file_list.append(f)
    # labels_dict = {}
    # for label in labels:
    #     pic_name, bone_age = label[:-1].split(' ')
    #     labels_dict[pic_name] = bone_age


    # output_path = input_para['augumentation_male_output']
    # lable_output_path = input_para['augumentation_male_label_output']
    # threshed = input_para['aug_threshed']
    # max_gen = input_para['aug_max_gen']
    # ignore = input_para['distribution_ignore']
    # pic_data_augmentation.augmentation(input_file_list, 
    #                                     output_path, 
    #                                     labels_dict, 
    #                                     lable_output_path,
    #                                     threshed=threshed,
    #                                     max_gen=max_gen,
    #                                     batch_size=1,
    #                                     save_prefix='bone',
    #                                     save_format='png', 
    #                                     ignore=ignore)


    # 数据划分
    # label_path = os.path.join(input_para['augumentation_male_output'], 'labels.txt')
    # input_dir = input_para['augumentation_male_output']
    # output_dir = input_para['male_split_output']


    # # 若没有扩充则用此路径
    # label_path = os.path.join(input_para['train_male_output'], 'labels.txt')
    # output_dir = input_para['male_split_output']
    # input_dir = input_para['train_male_output']


    # k_fold = input_para['male_k_fold']
    # data_split(input_dir, 
    #            output_dir, 
    #            label_path, 
    #            k_fold=k_fold)


    # # 数据格式转换
    # # male
    # train_data = input_para['male_split_output']
    # male_tfrecord_output = input_para['male_tfrecord_output']
    # data_convert_to_tfrecord(train_data, 
    #                          male_tfrecord_output,
    #                          input_para)

    # assert False, "节点测试"

    # 训练
    # label_path = os.path.join(input_para['augumentation_male_output'], 'labels.txt')    # 若扩充数据
    label_path = os.path.join(input_para['train_male_output'], 'labels.txt')    # 若没有扩充数据


    male_tfrecord_output = input_para['male_tfrecord_output']
    train_dir = input_para['train_dir']
    graph_dir = model_save_para['graph_dir']
    test_dir = input_para['male_split_output']
    original_dir = input_para['male_split_output']
    for network_setting in net_factory:
        print("[INFO] use model %s" % network_setting['model_name'])
        # # 训练
        # run_model(male_tfrecord_output, 
        #           original_dir, 
        #           input_para, 
        #           network_setting)

        # # 转换模型
        # convert_model(train_dir,
        #               test_dir,
        #               male_tfrecord_output,
        #               network_setting, 
        #               model_save_para, 
        #               input_para)
        # 使用当前模型对剩下的fold进行预测
        _ = prediction_train_data(graph_dir,
                                 test_dir,
                                 label_path,
                                 prediction_para, 
                                 network_setting)
        break


    prediction_output = prediction_para['prediction_output']
    train_data, labels = get_prediction_data(prediction_output) # 获得预测数据


    prediction_model = train_model(train_data, labels) # 训练融合模型


    fp = open("pickle_prediction_model.dat", "wb")
    pickle.dump(prediction_model, fp)
    fp.close()
    
    test_data = input_para['validation_male_output']
    label_path = os.path.join(test_data, 'labels.txt')
    model_list = []
    for model in net_factory:
        tmp_model_para = []
        tmp_model_para.append(model['model_name'])
        tmp_model_para.append(model['output_tensor_name'] + ":0")
        tmp_model_para.append(model['train_image_size'])
        model_list.append(tmp_model_para)

    # # test
    # model_list = [model_list[0]]


    # 使用训练好的模型对测试集进行预测, 方法基于stacking
    model_collection_prediction(prediction_model, 
                                test_data, 
                                label_path,
                                graph_dir, 
                                model_list)