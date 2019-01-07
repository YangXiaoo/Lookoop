# coding:UTF-8
# 2019-1-7
# configure

import tensorflow as tf

__all__ = [
    'configure_learning_rate',
    'configure_optimizer',
]

def configure_learning_rate(num_samples_per_epoch, global_step, **input_par):
  """
  设置学习率
  """
    decay_steps = int(num_samples_per_epoch / input_parbatch_size *
                    input_par['num_epochs_per_decay'])
    if input_parsync_replicas:
        decay_steps /= input_par['replicas_to_aggregate']

    if input_par['learning_rate_decay_type'] == 'exponential':
        return tf.train.exponential_decay(
            input_par['learning_rate'],
            global_step,
            decay_steps,
            input_par['learning_rate_decay_factor'],
            staircase=True,
            name='exponential_decay_learning_rate')

    elif input_par['learning_rate_decay_type'] == 'fixed':
        return tf.constant(input_par['learning_rate'], name='fixed_learning_rate')
    elif input_par['learning_rate_decay_type'] == 'polynomial':
        return tf.train.polynomial_decay(
            input_par['learning_rate'],
            global_step,
            decay_steps,
            input_par['end_learning_rate'],
            power=1.0,
            cycle=False,
            name='polynomial_decay_learning_rate')
    else:
        raise ValueError(
            'learning_rate_decay_type [%s] was not recognized',
            input_par['learning_rate_decay_type'])



def configure_optimizer(learning_rate, **input_par):
  """
  设置求解方法
  """
    if input_par['optimizer'] == 'adadelta':
        optimizer = tf.train.AdadeltaOptimizer(
            learning_rate,
            rho=input_par['adadelta_rho'],
            epsilon=input_par['opt_epsilon'])
    elif input_par['optimizer'] == 'adagrad':
        optimizer = tf.train.AdagradOptimizer(
            learning_rate,
            initial_accumulator_value=input_par['adagrad_initial_accumulator_value'])
    elif input_par['optimizer'] == 'adam':
        optimizer = tf.train.AdamOptimizer(
            learning_rate,
            beta1=input_par['adam_beta1'],
            beta2=input_par['adam_beta2'],
            epsilon=input_par['opt_epsilon'])
    elif input_par['optimizer'] == 'ftrl':
        optimizer = tf.train.FtrlOptimizer(
            learning_rate,
            learning_rate_power=input_par['ftrl_learning_rate_power'],
            initial_accumulator_value=input_par['ftrl_initial_accumulator_value'],
            l1_regularization_strength=input_par['ftrl_l1'],
            l2_regularization_strength=input_par['ftrl_l2'])
    elif input_par['optimizer'] == 'momentum':
        optimizer = tf.train.MomentumOptimizer(
            learning_rate,
            momentum=input_par['momentum'],
            name='Momentum')
    elif input_par['optimizer'] == 'rmsprop':
        optimizer = tf.train.RMSPropOptimizer(
            learning_rate,
            decay=input_par['rmsprop_decay'],
            momentum=input_par['momentum'],
            epsilon=input_par['opt_epsilon'])
    elif input_par['optimizer'] == 'sgd':
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
    else:
        raise ValueError('Optimizer [%s] was not recognized', input_par['optimizer'])
    return optimizer


def get_variables_to_train(input_par):
     """
    获得需要训练的变量
    """
    if input_par['trainable_scopes'] is None:
        return tf.trainable_variables()
    else:
        scopes = [scope.strip() for scope in input_par['trainable_scopes'].split(',')]

    variables_to_train = []
    for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variables_to_train.extend(variables)
    return variables_to_train