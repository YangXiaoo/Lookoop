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
from tool import tf_configure

slim = tf.contrib.slim 

# parameters
input_para = {
    
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


    # Optimization
    'weight_decay' : 0.00004,
    'opt_epsilon' : 1.0, # Epsilon term for the optimizer

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
    'dataset_name' : 'bone', # 加载数据集的模块名
    'dataset_split_name' : 'train', # 划分数据集的名称
    'dataset_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/data', # 数据存储
    'labels_offset' : 0,  # 标签偏移

    # 'model_name' : 'vgg_16', # vgg
    # 'model_name' : inception_v3, # inception3
    # 'model_name' : 'nasnet_large', # NASnet
    # 'model_name' : 'pnasnet_large', # pnasnet
    'model_name' : 'resnet_v2_200', # resnet

    'preprocessing_name' : None, # 预处理

    'batch_size' : 2, # batch size
    # 'train_image_size' : 229, # inception_3
    # 'train_image_size' : 244, # vgg_16 训练图片大小, None使用默认大小
    # 'train_image_size' : 331, # nasnet
    # 'train_image_size' : 331, # pnasnet
    'train_image_size' : 224, # resnet
    'max_number_of_steps' : 120, # 最大迭代次数


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


def main(input_para):
    """
    训练入口
    """
    tf.logging.set_verbosity(tf.logging.INFO) # 日志设置开始入口

    with tf.Graph().as_default(): # 实例化一个图

        # 运行环境初始化
        deploy_config = model_deploy.DeploymentConfig(
            num_clones=input_para['num_clones'],
            clone_on_cpu=input_para['clone_on_cpu'],
            replica_id=input_para['task'],
            num_replicas=input_para['worker_replicas'],
            num_ps_tasks=input_para['num_ps_tasks'])

        # 初始化迭代计数器
        with tf.device(deploy_config.variables_device()):
            global_step = slim.create_global_step() 


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
        # DatasetDataProvider参数设置
        # dataset：Dataset 类实例
        # num_readers：并行阅读器数量
        # reader_kwargs=None：阅读器关键配置字典
        # shuffle：是否打乱
        # num_epochs：每个数据源被读取的次数，如果设为None数据将会被无限循环的读取
        # common_queue_capacity：读取数据队列的容量，默认为256
        # common_queue_min：读取数据队列的最小容量
        # record_key：（不是很理解）
        # seed=None：打乱是的种子
        # scope=None：范围
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
                num_threads=input_para['num_preprocessing_threads'],
                capacity=input_para['batch_size'])

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


        summaries = set(tf.get_collection(tf.GraphKeys.SUMMARIES)) # Summary是对网络中Tensor取值进行监测的一种Operation

        clones = model_deploy.create_clones(deploy_config, clone_fn, [batch_queue])
        first_clone_scope = deploy_config.clone_scope(0) # master

        # 获得第一个环境下的操作
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS, first_clone_scope)


        end_points = clones[0].outputs
        for end_point in end_points:
            x = end_points[end_point]
            summaries.add(tf.summary.histogram('activations/' + end_point, x))

            # Tensorflow-tf.nn.zero_fraction()
            # 将输入的Tensor中0元素在所有元素中所占的比例计算并返回,
            # 因为relu激活函数有时会大面积的将输入参数设为0,
            # 所以此函数可以有效衡量relu激活函数的有效性
            summaries.add(tf.summary.scalar('sparsity/' + end_point, tf.nn.zero_fraction(x)))

        # 添加loss到summary
        for loss in tf.get_collection(tf.GraphKeys.LOSSES, first_clone_scope):
            summaries.add(tf.summary.scalar('losses/%s' % loss.op.name, loss))

        # 添加变量
        for variable in slim.get_model_variables():
            summaries.add(tf.summary.histogram(variable.op.name, variable))

        # 滑动平均设置
        if input_para['moving_average_decay']:
            moving_average_variables = slim.get_model_variables()
            variable_averages = tf.train.ExponentialMovingAverage(
                input_para['moving_average_decay'], 
                global_step)
        else:
            moving_average_variables, variable_averages = None, None

        # 求解方法
        with tf.device(deploy_config.optimizer_device()): # '/job:/device:CPU:0'
            learning_rate = tf_configure.configure_learning_rate(
                dataset.num_samples, 
                global_step,
                input_para)
            optimizer = tf_configure.configure_optimizer(learning_rate, input_para) # tf.train.exponential_decay
            summaries.add(tf.summary.scalar('learning_rate', learning_rate))

        if input_para['sync_replicas']:
            optimizer = tf.train.SyncReplicasOptimizer(
                opt=optimizer,
                replicas_to_aggregate=input_para['replicas_to_aggregate'],
                variable_averages=variable_averages,
                variables_to_average=moving_average_variables,
                replica_id=tf.constant(input_para['task'], tf.int32, shape=()),
                total_num_replicas=input_para['worker_replicas'])
        elif input_para['moving_average_decay']:
            # 更新Opt
            update_ops.append(variable_averages.apply(moving_average_variables))

        variables_to_train = tf_configure.get_variables_to_train(input_para) # 获得训练参数

        # 分布式 求解设置
        # https://blog.csdn.net/NockinOnHeavensDoor/article/details/80632677
        total_loss, clones_gradients = model_deploy.optimize_clones(
            clones,
            optimizer,
            var_list=variables_to_train)

        # 添加损失
        summaries.add(tf.summary.scalar('total_loss', total_loss))

        # 创建gradient更新操作
        grad_updates = optimizer.apply_gradients(clones_gradients, global_step=global_step)
        update_ops.append(grad_updates)

        update_op = tf.group(*update_ops) # 组合操作, 返回操作

        # 设置依赖, 只有update_op执行完后才能执行with里面的
        # 它是通过在计算图内部创建 send / recv节点来引用或复制变量的
        # 最主要的用途就是更好的控制在不同设备间传递变量的值；
        # 另外，它还有一种常见的用途，就是用来作为一个虚拟节点来控制流程操作，
        # 比如我们希望强制先执行loss_averages_op或updata_op, 然后更新相关变量
        with tf.control_dependencies([update_op]):
            train_tensor = tf.identity(total_loss, name='train_op')

        summaries |= set(tf.get_collection(tf.GraphKeys.SUMMARIES, first_clone_scope))
        # 融合所有summary
        summary_op = tf.summary.merge(list(summaries), name='summary_op')

        # 训练
        slim.learning.train(
            train_tensor,
            logdir=input_para['train_dir'],
            master=input_para['master'],
            is_chief=(input_para['task'] == 0),
            init_fn=tf_configure.get_init_fn(input_para),
            summary_op=summary_op,
            number_of_steps=input_para['max_number_of_steps'],
            log_every_n_steps=input_para['log_every_n_steps'],
            save_summaries_secs=input_para['save_summaries_secs'],
            save_interval_secs=input_para['save_interval_secs'],
            sync_optimizer=optimizer if input_para['sync_replicas'] else None)


if __name__ == '__main__':
  main(input_para)
