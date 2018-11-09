# coding: utf-8
# 2018-8-19
# 神经网络
# jupyter notebook 查看ipynd格式
import os
try:
	import numpy
except:
	print("Automate excute: pip install numpy ....")
	sleep(3)
	os.system("pip install numpy")
	import numpy
# import scipy.special # 有sigmoid函数
import math



"""
a. 初始化函数
b. 训练
c. 测试
"""

class neuralNetwork(object):
	def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
		"""
		初始化网络参数, 共三层网络
		"""
		self.in_nodes = inputNodes
		self.hide_nodes = hiddenNodes
		self.out_nodes = outputNodes
		self.l_rate = learningRate

		# 将input层与hidden层权重用矩阵表示
		# 同理表示 hidden层与output层
		# pow(self.hide_nodes, -0.5) 标准方差为传入链接数目的开方
		# 矩阵规模： hidden x in 这样表示是因为 weight_in_hide x inputs 才能正确相乘
		self.weight_in_hide = numpy.random.normal(0.0, pow(self.hide_nodes, -0.5), (self.hide_nodes, self.in_nodes))
		self.weight_hide_out = numpy.random.normal(0.0, pow(self.out_nodes, -0.5), (self.out_nodes, self.hide_nodes))

		self.active_function = lambda x: (1/(1 + math.e**(-x))) # sigmoid函数

	def train(self, inputs_list, targets_list):
		"""
		训练数据集
		"""
		inputs = numpy.array(inputs_list, ndmin=2).T #转换为2d array并且转置. ndmin表示矩阵维度
		targets = numpy.array(targets_list, ndmin=2).T

		hidden_inputs = numpy.dot(self.weight_in_hide, inputs)
		hidden_outputs = self.active_function(hidden_inputs)

		final_inputs = numpy.dot(self.weight_hide_out, hidden_outputs)
		final_outputs = self.active_function(final_inputs)

		output_errors = (targets - final_outputs) # 期望差值
		hidden_error = numpy.dot(self.weight_hide_out.T, output_errors) # 误差反向传播

		# 根据误差修改各层权重
		self.weight_hide_out += self.l_rate * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
		self.weight_in_hide += self.l_rate * numpy.dot((hidden_error * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))


	def test(self, inputs_lists):
		"""
		测试
		"""
		inputs = numpy.array(inputs_lists, ndmin=2).T

		hidden_inputs = numpy.dot(self.weight_in_hide, inputs)
		hidden_outputs = self.active_function(hidden_inputs)

		final_inputs = numpy.dot(self.weight_hide_out, hidden_outputs)
		final_outputs = self.active_function(final_inputs)

		return final_outputs




def test():

	inputNodes = 784 # 28 x 28
	hiddenNodes = 1000
	outputNodes = 10 # 输出的值个数
	learningRate = 0.1

	net = neuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

	# 读取训练数据集
	train_data_file = open("C:/Study/github/Lookoop/Image/Python神经网络/mnist_dataset/mnist_train_100.csv", "r")
	train_data_list = train_data_file.readlines()
	train_data_file.close()

	######## 训练 #########
	iteration = 50 # 迭代次数
	for i in range(iteration):
		for record in train_data_list:
			values = record.split(',') # 转化为数组, values[0] 为标签
			# 转化数据规模为0.01~1
			inputs = (numpy.asfarray(values[1:]) / 255.0 * 0.99) + 0.01
			targets = numpy.zeros(outputNodes) + 0.01 # 初始化输出节点，避免0
			targets[int(values[0])] = 0.99 # 将的每个标签的值置为0.99(避免1)， 数据标签为0-9
			# 避免0和1是因为激活函数生成0和1是不可能
			net.train(inputs, targets)
		print("完成第 ", i, "次迭代")


	#############  测试 ##############
	# 读取测试数据
	test_data_file = open("C:/Study/github/Lookoop/Image/Python神经网络/mnist_dataset/mnist_train_100.csv", "r")
	test_data_list = test_data_file.readlines()
	test_data_file.close()	

	result = [] # 存储test结果
	for record in test_data_list:
		values = record.split(',')
		correct_label = int(values[0]) # 正确值
		inputs = (numpy.asfarray(values[1:]) / 255.0 * 0.99) + 0.01
		
		outputs = net.test(inputs)

		label = numpy.argmax(outputs) # 找出最大索引，若训练正确则索引即为标签值

		if label == correct_label:
			print("\n数字 ", correct_label, "识别成功！")
			result.append(1)
		else:
			print("\n数字 ", correct_label, "识别失败！")
			result.append(0)

		for i in range(10):
			print("数字: ", i, " 的概率为： ", outputs[i])


	# 最终准确率
	result_array = numpy.asarray(result) # asarray不会深度拷贝数组，占用内存少
	print("识别率 = ", result_array.sum() / result_array.size)




if __name__ == "__main__":
	test()







