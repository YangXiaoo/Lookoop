# 2018-12-12
tf.Graph.device() # 指定运行计算的设备
tf.add_to_collection() # 将资源加入一个或多个集合中
tf.get_collection() # 获取一个集合里面的所有资源

result.get_shape() # 获取结果张量的维度信息
tf.Tensor.eval() # 计算一个张量的值
tf.InteractiveSession() # 将生成的会话注册成默认会话
tf.placeholder() # 占位符

tf.ConfigProto() # 配置需要生成的会话,以下为参数
	# allow_soft_placement: 1.无法在CPU进行计算，2. 没有CPU资源 3. 运算输入包含对CPU计算结果引用
	# log_device_placement: 记录日志

tf.matual() # 元素之间相乘
tf.random_normal([2,3], stddev=2) # 产生一个2x3的矩阵， 各个元素为0，标准差为2的随机数
tf.Variable(weights.initialized_value()) # 用weights来初始化相同值
tf.global_variavles_initializer() # 初始化所有变量
tf.global_variables() # 获取当前计算图的所有变量
tf.trainable_varibles() # 获得所有优化参数
tf.clip_by_value() # 将一个张量中的数值限制在一个范围内
tf.reduce_mean() # 求元素平均
tf.log()
tf.argmax(y, 1) # 获取y中最大值的索引
# 损失函数
tf.nn.softmax_cross_entropy_with_logits(lables=y_, logits=y)

# 比较大小
tf.greater(v1, v2).eval() # v1>v2则True

# 训练大致过程
barch_size = 
x = tf.placeholder(tf.float32, shape(barch_size, 2), name='x_input')
y_ = tf.placeholder(tf.float32, shape(barch_size, 1), name='y_input')
# 定义网络结构及优化算法
loss = 
train_step = tf.train.AdamOptimizer(0.0001).minimize(loss)
with tf.Session as sess:
	for i in range(STEPS):
		# 准备batch_size个数
		current_x, current_y = 
		sess.run(train_step, feed_dict={x: current_x, y_:current_y})

# 学习率
global_step = tf.Variable(0)
learning_rate = tf.train.exponential_decay(0.1, global_step, 100, 0.96, staircase=True)
learning_step = tf.train.GradientDescentOpimizer(learning_rate).minimize(loss, global_step=global_step)


tf.cast(data, tf.int32) # 将x的数据格式转化成dtype.例如，原来x的数据格式是bool，那么将其转化成float以后，就能够将其转化成0和1的序列。反之也可以

tf.FixedLengthRecordReader(record_bytes=record_bytes) # 读取固定长度字节数信息

tf.strided_slice( input_, begin, end , stride) # 提取张量的一部分[begin, end)

# 命令行
# 三个参数：变量，默认值，用法描述
tf.app.flags.DEFINE_string() ：定义一个用于接收 string 类型数值的变量;
tf.app.flags.DEFINE_integer() : 定义一个用于接收 int 类型数值的变量;
tf.app.flags.DEFINE_float() ： 定义一个用于接收 float 类型数值的变量;
tf.app.flags.DEFINE_boolean() : 定义一个用于接收 bool 类型数值的变量;
FLAGS = tf.app.flags.FLAGS # 使用


# 文件处理
if tf.gfile.Exists(FLAGS.train_dir):
tf.gfile.DeleteRecursively(FLAGS.train_dir)
tf.gfile.MakeDirs(FLAGS.train_dir)