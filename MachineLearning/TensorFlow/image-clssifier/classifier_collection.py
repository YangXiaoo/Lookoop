# coding:UTF-8
# 2019-1-15

import os

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

    'thresheded' : 100, # 每个年龄图片数量超过这个值则不会扩充
    'max_gen' : 5, # 默认单张图片扩充数量
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
    'dataset_name' : 'datasets',
    'tf_class_label_base' : 0,



    # 训练
    'train_dir' : r'C:\Study\test\kaggle-bonage\train_dir', # 存放节点和日志

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



net_factory = [
    # vgg_16
    {
        'model_name' : 'vgg_16',
        'train_image_size' : 244,
        'output_tensor_name' : 'vgg_16/fc8/squeezed',

        # Fine-Tuning
        'checkpoint_path' : None, # None
        'checkpoint_exclude_scopes' : 'vgg_16/fc6,vgg_16/fc7,vgg_16/fc8', # 不加载的节点
    },

    # inception_v3
    {
        'model_name' : 'inception_v3',
        'train_image_size' : 229,
        'output_tensor_name' : 'InceptionV3/Predictions/Reshape_1',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
    },

    # nasnet_large
    {
        'model_name' : 'nasnet_large',
        'train_image_size' : 331,
        'output_tensor_name' : 'final_layer/predictions',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : 'cell_17/',
    },

    # pnasnet_large
    {

        'model_name' : 'pnasnet_large',
        'train_image_size' : 331,
        'output_tensor_name' : 'final_layer/predictions',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
    },

    # resnet_v2_200
    {
        'model_name' : 'resnet_v2_200',
        'train_image_size' : 224,
        'output_tensor_name' : 'resnet_v2_200/predictions/Reshape_1',

        # Fine-Tuning
        'checkpoint_path' : None,
        'checkpoint_exclude_scopes' : '',
    },
]

model_save_para = {
        'is_training' : False,
        'default_image_size' : 224, 
        'dataset_name' : '',
        'labels_offset' : 0,
        'graph_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/graph',
        'data_split' : 'test',
        'dataset_dir' : '', # 处理后TF格式的数据集

        'input_checkpoint' : '', # ckpt模型
        'frozen_graph' : '',
        'output_node_names' : '',

        'input_saver' : '',
        'input_binary' : True, # bool

        'restore_op_name' : "save/restore_all",
        'filename_tensor_name' : "save/Const:0",
        'clear_devices' : True,
        'initializer_nodes' : '',
        'variable_names_blacklist' : '',
    }


prediction_para = {
    'model_path' : '', # graph_dir
    'label_path' : '', # 所有训练数据的标签
    'image_file' : '',
    'is_save' : True,
    'width' : 224,
    'height' : 224,
    'prediction_output' : r'C:\Study\test\tensorflow-bone\prediction_output'
}










def data_split(input_dir, 
                output_dir, 
                label_path, 
                k_fold=5):
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
                            **input_para):
    # 数据格式转换
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
                input_para, 
                network_setting):
    """

    """
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
    """

    """
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
    graph_dir: 所有graph的路径
    """
    prediction_para = prediction_para.copy()
    graph_index_dir = os.path.join(graph_dir, network_setting['model_name'])
    class_labels = os.listdir(graph_index_dir)
    prediction_para['label_path'] = label_path
    for c in class_labels:
        test_data_dir = os.path.join(test_dir, c, 'test')
        prediction_para['image_file'] = test_data_dir
        model_path = os.path.join(graph_index_dir, c, 'frozen_graph.pb')
        prediction_para['model_path'] = model_path
        prediction_para['tensor_name'] = network_setting['output_tensor_name']
        prediction_para['width'] = network_setting['train_image_size']
        prediction_para['height'] = network_setting['train_image_size']
        prediction_para['prediction_output'] = os.path.join(prediction_para['prediction_output'], network_setting['model_name'], c, 'prediction.npy') # 创建文件夹.

        run_inference_on_image(prediction_para)


def train_model(prediction_output):
    model_name = os.listdir(prediction_output)
    split_name = os.listdir(os.path.join(prediction_output, model_name))

    train_data, labels = [], []
    for s in split_name:
        tmp_test_data, tmp_test_labels = {}, []
        for m in model_name:
            tmp_data_path = os.path.join(prediction_output, m, s, 'prediction.npy')
            tmp_data = np.load(tmp_data_path) # {class_pic, data}
            for k,v in tmp_data.items():
                if k not in tmp_test_data:
                    tmp_test_data[k] = []

                tmp_test_data[k].extend(v) # {pic:[prediction_1, prediction_2, ]}
        for k,v in tmp_test_data.items():
            train_data.append(v)
            labels.append(int(k.split('_')[0]))

    num_classes = len(set(labels))
    feature = np.mat(train_data)
    labels = np.mat(labels).T
    softmax = regression.softmax(feature, labels, num_classes, 10000, 0.2)
    softmax.train()
    np.save("weights.npy", weights)

    return softmax


def model_single_prediction(test_data, 
                            label_path,
                            graph_dir, 
                            model_name, 
                            tensor_name,
                            image_size):
    """
    一个神经网络模型训练好的模型对数据进行预测
    """
    model_graph_dir = os.path.join(model_dir, model_name)
    class_list = os.listdir(model_graph_dir)
    prediction = {} # '{pic:array(prediction_data)}'
    for s in class_list:
        model_path = os.path.join(model_graph_dir, s, 'frozen_graph.pb')
        prediction_para['model_path'] = model_path
        prediction_para['tensor_name'] = tensor_name
        prediction_para['width'] = image_size
        prediction_para['height'] = image_size
        prediction_para['is_save'] = False
        tmp_model_prediction = run_inference_on_image(graph_path, 
                                                label_path, 
                                                test_data, 
                                                tensor_name,
                                                image_size)
        for k,v in tmp_model_prediction.items():
            prediction[k] += v

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
    validation
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
    # # 抽取数据
    threshed = input_para['male_k_fold']
    train_size = 0.9
    get_data.main(input_para['pic_path'], 
                input_para['csv_path'], 
                input_para['train_male_output'],
                input_para['train_female_output'], 
                input_para['validation_male_output'],
                input_para['validation_female_output'], 
                input_para['lables_output'],
                train_size=train_size,
                threshed=threshed,
                is_write=False)

    # # 数据扩充
    label_path = os.path.join(input_para['train_male_output'], 'labels.txt')
    lables = pic_data_augumentation.getLablesDict(lable_path)
    input_path = input_para['train_male_output']
    output_path = input_para['augumentation_male_output']
    lable_output_path = input_para['augumentation_male_label_output']
    thresheded = input_para['thresheded']
    max_gen = input_para['max_gen']
    ignore = input_para['distribution_ignore']
    pic_data_augumentation.augmentation(input_path, 
                                        output_path, 
                                        labels, 
                                        lable_output_path,
                                        thresheded=100,
                                        max_gen=5,
                                        batch_size=1,
                                        save_prefix='bone',
                                        save_format='png', 
                                        ignore=False)


    # # 数据划分
    # label_path = os.path.join(input_para['augumentation_male_output'], 'labels.txt')
    # input_dir = input_para['augumentation_male_output']
    # output_dir = input_para['male_split_output']
    # k_fold = input_para['male_k_fold']

    # data_split(input_dir, 
    #             output_dir, 
    #             label_path, 
    #             k_fold=k_fold)


    # # 数据格式转换
    # # male
    # train_data = input_para['male_split_output']
    # male_tfrecord_output = input_para['male_tfrecord_output']
    # data_convert_to_tfrecord(train_data, 
    #                         male_tfrecord_output,
    #                         **input_para)


    # # 训练
    # train_dir = input_para['train_dir']
    # graph_dir = model_save_para['graph_dir']
    # test_dir = input_para['male_split_output']
    # for network_setting in net_factory
    #     run_model(male_tfrecord_output, **input_para, **network_setting)
    #     convert_model(train_dir,
    #                 male_tfrecord_output,
    #                 **network_setting, 
    #                 **model_save_para, 
    #                 **input_para)

    #     prediction_train_data(graph_dir,
    #                     test_dir,
    #                     label_path,
    #                     **prediction_para, 
    #                     **network_setting)

    # prediction_output = prediction_para['prediction_output']
    # prediction_model = train_model(prediction_output)
    
    # test_data = input_para['validation_male_output']
    # label_path = os.path.join(test_data, 'labels.txt')
    # model_collection_prediction(prediction_model, 
    #                             test_data, 
    #                             label_path,
    #                             graph_dir, 
    #                             model_list):