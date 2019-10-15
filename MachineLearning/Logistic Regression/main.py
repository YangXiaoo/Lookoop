# 2018-9-29
# Logistic Regression
# python 机器学习算法
import numpy as np

def sig(x):
    '''
    Sigmoid函数
    input:  x(mat):feature * w
    output: sigmoid(x)(mat):Sigmoid值
    '''
    return 1.0 / (1 + np.exp(-x))


def loadData(file_name, skip=True):
	"""
	载入数据
	"""
	feature = []
	label = []
	file = open(file_name)

	for line in file.readlines():
		feature_tmp = []
		label_tmp = []
		data = line.strip().split("\t") # split(" ")
		feature_tmp.append(1)  # 偏置项
		if skip:
			for i in data[:-1]:
				feature_tmp.append(float(i))
		else:
			for i in data:
				feature_tmp.append(float(i))
		label_tmp.append(float(data[-1]))

		feature.append(feature_tmp)
		label.append(label_tmp)

	file.close()
	return np.mat(feature), np.mat(label)


def train(feature, label, max_iteration, alpha):
	"""
	使用梯度下降法训练
	feature: m x n, 特征
	label: m x 1, 标签
	"""
	n = np.shape(feature)[1]
	w = np.mat(np.ones((n, 1)))

	i = 0
	while i < max_iteration:
		i += 1
		h = sig(feature * w) # feature: m x n, w: n x 1
		#print(np.shape(label), np.shape(h))
		error = label - h # m x 1
		w = w + alpha * feature.T * error # 1 x n x m x m x 1
		if i % 100 == 0:
			error_rate = errorRate(h, label)
			print("iteration: %d, error rate: %.10f" % (i, error_rate))
	return w


def errorRate(h, label):
	"""
	损失函数
	"""
	m = np.shape(h)[0]

	sum_error = 0.0 # 初始损失为0
	for i in range(m):
		if h[i, 0] > 0 and h[i, 0] < 1:
			sum_error -= label[i, 0] * np.log(h[i, 0]) + (1 - label[i, 0]) * np.log(1 - h[i, 0])
		else:
			pass
	return sum_error / m


def saveModel(file_name, w):
	m = np.shape(w)[0]
	with open(file_name, "w") as f:
		w_tmp = []
		for i in range(m):
			w_tmp.append(str(w[i, 0]))
		f.write("\t".join(w_tmp))
		f.close()


def loadModel(file_name):
	weight = []
	with open(file_name) as f:
		for l in f.readlines():
			weight_tmp = []
			data = l.strip().split("\t")
			for i in data:
				weight_tmp.append(float(i))
			weight.append(weight_tmp)
		f.close()
	return np.mat(weight)


def prefict(data, w, r):
	h = sig(data * w.T)
	m = np.shape(data)[0]
	for i in range(m):
		if h[i, 0] < r:
			h[i, 0] = 0.0
		else:
			h[i, 0] = 1.0
	return h


if __name__ == '__main__':
	feature, label = loadData("data.txt")
	# print(feature, label)

	# 训练
	print("training...")
	w = train(feature, label, 100000, 0.01)
	saveModel("weight", w)

	print("\npredicting...")
	w = loadModel("weight")
	print(w)
	feature, label = loadData("test_data", skip=False)
	# 预测
	h = prefict(feature, w, 0.5)
	# print(h)