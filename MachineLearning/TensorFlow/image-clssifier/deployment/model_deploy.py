# coding:UTF-8
# 2019-1-6
# model_deploy

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

import tensorflow as tf

slim = tf.contrib.slim

# __all__ 作用就是定义公开接口
__all__ = ['create_clones',
           'deploy',
           'optimize_clones',
           'DeployedModel',
           'DeploymentConfig',
           'Clone',
          ]

Clone = collections.namedtuple('Clone',
                               ['outputs',  # Whatever model_fn() returned.
                                'scope',  # The scope used to create it.
                                'device',  # The device used to create.
                               ])

DeployedModel = collections.namedtuple('DeployedModel',
                                       ['train_op',  # The `train_op`
                                        'summary_op',  # The `summary_op`
                                        'total_loss',  # The loss `Tensor`
                                        'clones',  # A list of `Clones` tuples.
                                       ])

# Default parameters for DeploymentConfig
_deployment_params = {'num_clones': 1,
                      'clone_on_cpu': False,
                      'replica_id': 0,
                      'num_replicas': 1,
                      'num_ps_tasks': 0,
                      'worker_job_name': 'worker',
                      'ps_job_name': 'ps'}


def create_clones(config, model_fn, args=None, kwargs=None):
	"""
	Creates multiple clones according to config using a `model_fn`.
	"""
 	clones = []
  	args = args or []
  	kwargs = kwargs or {}
  	with slim.arg_scope([slim.model_variable, slim.variable],
                      device=config.variables_device()):
    	for i in range(0, config.num_clones):
      		with tf.name_scope(config.clone_scope(i)) as clone_scope:
        		clone_device = config.clone_device(i)
        		with tf.device(clone_device):
          			with tf.variable_scope(tf.get_variable_scope(),
                                 reuse=True if i > 0 else None):
            			outputs = model_fn(*args, **kwargs)
          			clones.append(Clone(outputs, clone_scope, clone_device))
  	return clones


def _gather_clone_loss(clone, num_clones, regularization_losses):
	pass

def _optimize_clone(optimizer, clone, num_clones, regularization_losses,
                    **kwargs):
	pass

def optimize_clones(clones, optimizer,
                    regularization_losses=None,
                    **kwargs):
	pass 

def deploy(config,
           model_fn,
           args=None,
           kwargs=None,
           optimizer=None,
           summarize_gradients=False):
	pass 


def _sum_clones_gradients(clone_grads):
	pass 

def _add_gradients_summaries(grads_and_vars):
	pass 

class DeploymentConfig(object):
	"""
	–Device mapping: no known devices.
	–op: /job:localhost/replica:0/task:0/cpu:0
	"""
  	def __init__(self,
               num_clones=1,
               clone_on_cpu=False,
               replica_id=0,
               num_replicas=1,
               num_ps_tasks=0,
               worker_job_name='worker',
               ps_job_name='ps'):
	  	"""
	    num_clones: Number of model clones to deploy in each replica.
	  	clone_on_cpu: If True clones would be placed on CPU.
	  	replica_id: Integer.  Index of the replica for which the model is
	    deployed.  Usually 0 for the chief replica.
	  	num_replicas: Number of replicas to use.
	  	num_ps_tasks: Number of tasks for the `ps` job. 0 to not use replicas.
	  	worker_job_name: A name for the worker job.
	  	ps_job_name: A name for the parameter server job.
	  	"""
	  	# 基本判断
	    if num_replicas > 1:
	      	if num_ps_tasks < 1:
	        	raise ValueError('When using replicas num_ps_tasks must be positive')
	    if num_replicas > 1 or num_ps_tasks > 0:
	      	if not worker_job_name:
	        	raise ValueError('Must specify worker_job_name when using replicas')
	      	if not ps_job_name:
	        	raise ValueError('Must specify ps_job_name when using parameter server')
	    if replica_id >= num_replicas:
	      	raise ValueError('replica_id must be less than num_replicas')

	    self._num_clones = num_clones
	    self._clone_on_cpu = clone_on_cpu
	    self._replica_id = replica_id
	    self._num_replicas = num_replicas
	    self._num_ps_tasks = num_ps_tasks
	    self._ps_device = '/job:' + ps_job_name if num_ps_tasks > 0 else ''
	    self._worker_device = '/job:' + worker_job_name if num_ps_tasks > 0 else ''

  	@property
  	def num_clones(self):
    	return self._num_clones

  	@property
  	def clone_on_cpu(self):
    	return self._clone_on_cpu

  	@property
  	def replica_id(self):
    	return self._replica_id

  	@property
  	def num_replicas(self):
    	return self._num_replicas

  	@property
  	def num_ps_tasks(self):
    	return self._num_ps_tasks

  	@property
  	def ps_device(self):
    	return self._ps_device

  	@property
  	def worker_device(self):
    	return self._worker_device


  	def caching_device(self):
	    """
	    返回缓存变量的设备
	    """
	    if self._num_ps_tasks > 0:
	      	return lambda op: op.device
	    else:
	      	return None

  	def clone_device(self, clone_index):
	    """
	    复制
	    """
	    if clone_index >= self._num_clones:
	      	raise ValueError('clone_index must be less than num_clones')
	    device = ''
	    if self._num_ps_tasks > 0:
	      	device += self._worker_device
	    if self._clone_on_cpu:
	      	device += '/device:CPU:0'
	    else:
	      	device += '/device:GPU:%d' % clone_index
	    return device

  	def clone_scope(self, clone_index):
	    """
	    复制变量所属设备id
	    """
	    if clone_index >= self._num_clones:
	      raise ValueError('clone_index must be less than num_clones')
	    scope = ''
	    if self._num_clones > 1:
	      scope = 'clone_%d' % clone_index
	    return scope

  	def optimizer_device(self):
	    """Device to use with the optimizer.

	    Returns:
	      A value suitable for `tf.device()`.
	    """
	    if self._num_ps_tasks > 0 or self._num_clones > 0:
	      	return self._worker_device + '/device:CPU:0'
	    else:
	      	return ''

  	def inputs_device(self):
	    """Device to use to build the inputs.

	    Returns:
	      A value suitable for `tf.device()`.
	    """
	    device = ''
	    if self._num_ps_tasks > 0:
	      	device += self._worker_device
	    device += '/device:CPU:0'
	    return device

  	def variables_device(self):
	    """Returns the device to use for variables created inside the clone.

	    Returns:
	      A value suitable for `tf.device()`.
	    """
	    device = ''
	    if self._num_ps_tasks > 0:
	      	device += self._ps_device
	    device += '/device:CPU:0'

	    class _PSDeviceChooser(object):
	      """Slim device chooser for variables when using PS."""

	      	def __init__(self, device, tasks):
		        self._device = device
		        self._tasks = tasks
		        self._task = 0

	      	def choose(self, op):
		        if op.device:
		          	return op.device
		        node_def = op if isinstance(op, tf.NodeDef) else op.node_def
		        if node_def.op.startswith('Variable'):
		          	t = self._task
		          	self._task = (self._task + 1) % self._tasks
		          	d = '%s/task:%d' % (self._device, t)
		          	return d
		        else:
		          	return op.device

	    if not self._num_ps_tasks:
	      	return device
	    else:
	      	chooser = _PSDeviceChooser(device, self._num_ps_tasks)
	      	return chooser.choose