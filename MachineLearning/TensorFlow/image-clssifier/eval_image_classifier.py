# coding:UTF-8
# 2019-1-8
# eval iamge


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import tensorflow as tf

from datasets import dataset_factory
from nets import nets_factory
from preprocessing import preprocessing_factory

slim = tf.contrib.slim


input_para = {
    'batch_size' : 2,
    'max_num_batches' : None,
    'master' : '',
    'checkpoint_path' : r'C:\Study\github\others\Deep-Learning-21-Examples-master\chapter_3\data_prepare\satellite\train_dir_incept',
    'eval_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/eval_dir_incept',
    'num_preprocessing_threads' : 2,
    'dataset_name' : 'bone',
    'dataset_split_name' : 'validation',
    'dataset_dir' : 'C:/Study/github/others/Deep-Learning-21-Examples-master/chapter_3/data_prepare/satellite/data',
    'labels_offset' : 0,
    'model_name' : 'inception_v3',
    'preprocessing_name' : None,
    'moving_average_decay' : None,
    'eval_image_size' : None
}


def main(_):

    tf.logging.set_verbosity(tf.logging.INFO)

    # 初始全局步长
    with tf.Graph().as_default():
        global_step = slim.get_or_create_global_step()
    # with tf.Graph().as_default():
    #     global_step = slim.create_global_step() 

    # tf.train.get_global_step(graph=None)
    dataset = dataset_factory.get_dataset(
        input_para['dataset_name'], input_para['dataset_split_name'], input_para['dataset_dir'])

    network_fn = nets_factory.get_network_fn(
        input_para['model_name'],
        num_classes=(dataset.num_classes - input_para['labels_offset']),
        is_training=False)

    provider = slim.dataset_data_provider.DatasetDataProvider(
        dataset,
        shuffle=False,
        common_queue_capacity=2 * input_para['batch_size'],
        common_queue_min=input_para['batch_size'])

    [image, label] = provider.get(['image', 'label'])
    label -= input_para['labels_offset']

    preprocessing_name = input_para['preprocessing_name'] or input_para['model_name']
    image_preprocessing_fn = preprocessing_factory.get_preprocessing(
        preprocessing_name,
        is_training=False)


    eval_image_size = input_para['eval_image_size'] or network_fn.default_image_size

    image = image_preprocessing_fn(image, eval_image_size, eval_image_size)

    images, labels = tf.train.batch(
        [image, label],
        batch_size=input_para['batch_size'],
        num_threads=input_para['num_preprocessing_threads'],
        capacity=5 * input_para['batch_size'])


    logits, _ = network_fn(images)

    # tf.contrib.quantize.create_eval_graph()
    global_step = slim.get_or_create_global_step() 

    if input_para['moving_average_decay']:
        variable_averages = tf.train.ExponentialMovingAverage(
            input_para['moving_average_decay'], 
            global_step)
        variables_to_restore = variable_averages.variables_to_restore(slim.get_model_variables())
        variables_to_restore[global_step.op.name] = global_step
    else:
        variables_to_restore = slim.get_variables_to_restore()

    predictions = tf.argmax(logits, 1)
    labels = tf.squeeze(labels)

    names_to_values, names_to_updates = slim.metrics.aggregate_metric_map({
        'Accuracy': slim.metrics.streaming_accuracy(predictions, labels),
        'Recall_5': slim.metrics.streaming_recall_at_k(
            logits, labels, 5),
    })

    for name, value in names_to_values.items():
        summary_name = 'eval/%s' % name
        op = tf.summary.scalar(summary_name, value, collections=[])
        op = tf.Print(op, [value], summary_name)
        tf.add_to_collection(tf.GraphKeys.SUMMARIES, op)


    if input_para['max_num_batches']:
        num_batches = input_para['max_num_batches']
    else:
        num_batches = math.ceil(dataset.num_samples / float(input_para['batch_size']))

    if tf.gfile.IsDirectory(input_para['checkpoint_path']):
        checkpoint_path = tf.train.latest_checkpoint(input_para['checkpoint_path'])
    else:
        checkpoint_path = input_para['checkpoint_path']

    tf.logging.info('Evaluating %s' % checkpoint_path)

    slim.evaluation.evaluate_once(
        master=input_para['master'],
        checkpoint_path=checkpoint_path,
        logdir=input_para['eval_dir'],
        num_evals=num_batches,
        eval_op=list(names_to_updates.values()),
        variables_to_restore=variables_to_restore)


if __name__ == '__main__':
  tf.app.run()