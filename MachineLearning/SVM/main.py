# 2018-10-3
# Support Vector Machines
# python 机器学习算法
# 拉格朗日对偶问题 https://blog.csdn.net/blackyuanc/article/details/67640844
import numpy as np
import cPickle as pickle

def loadDate(file_name):
	feature = []
	label = []
	f = open(file_name)
	for line in f.readlines():
		feature_tmp = []
		line_data = line.strip().split(" ")
		label.append(float(line_data[0]))
		for i in line_data[1:]:
			i = i.split(":")
			feature_tmp.append(float(i[-1]))
		feature.append(feature_tmp[:])
	f.close()

	return np.mat(feature), np.mat(label).T 




class SVM:
    def __init__(self, dataSet, labels, C, toler, kernel_option):
        self.train_x = dataSet # 训练特征
        self.label = labels  # 训练标签
        self.C = C # 惩罚参数
        self.toler = toler     # 迭代的终止条件之一
        self.feature_size = np.shape(dataSet)[0] # 训练样本的个数
        self.alphas = np.mat(np.zeros((self.feature_size, 1))) # 拉格朗日乘子
        self.b = 0 # 截距
        self.error_tmp = np.mat(np.zeros((self.feature_size, 2))) # 保存E的缓存
        self.kernel_opt = kernel_option # 选用的核函数及其参数
        self.kernel_mat = calcKernel(self.train_x, self.kernel_opt) # 核函数的输出


def calcKernel(train_x, kernel_opt):
	"""
	采用核函数将非线性问题转换为线性问题
	"""
	m = np.shape(train_x)[0]
	kernel_matrix = np.mat(np.zeros((m, m)))
	for i in range(m):
		kernel_matrix[: , i] = calcKernelValue(train_x, train_x[i, :], kernel_option)
	return kernel_matrix


def calcKernelValue(train_x, train_x_i, kernel_option):
	"""
	核函数
	train_x_i: train_x矩阵的第i行
	"""
	kernel_type =kernel_option[0]
	m = np.shape(train_x)[0]
	kernel_value = np.mat(np.zeros((m, 1))) # m x 1

	# 径向基函数——Radial Basis Function
	if kernel_type == "rbf":
		sigma = kernel_option[1]
		if int(sigma) == 0:
			sigma = 1.0
		for i in range(m):
			diff = train_x[i, :] - train_x_i # 1 x n
			kernel_value[i] = np.exp(diff * diff.T / (-2.0 * sigma**2))
	else:
		kernel_value = train_x * train_x_i.T # m x n  x  (1 x n).T

	return kernel_value


def calcError(svm, alpha_k):
	"""
	计算误差： E = g(X) - y
	"""
	g_k = float(np.multiply(svm.alphas, svm.label).T * svm.kernel_mat[:, alpha_k] + svm.b)
	error_k = g_k - float(svm.label[alpha_k])

	return error_k


def updateErrorTmp(svm, alpha_k):
	"""
	更新误差值
	"""
	error = calcError(svm, alpha_k)
	svm.error_tmp[alpha_k] = [1, error]


def selectSecondSample(svm, alpha_i, error_i):
	"""
	选择第二个样本
	"""

	# 标记为已经被优化
	svm.error_tmp[alpha_i] = [1, error_i]
	# 列出没有被标记的alpha的索引, .A转换为数组
	candidate_alpha_list = np.nonzero(svm.error_tmp[: 0].A)[0]

	max_step, alpha_j, error_j = 0, 0, 0

	if len(candidate_alpha_list) > 1:
		for alpha_k in candidate_alpha_list:
			if alpha_k == alpha_i:
				continue
			error_k = calcError(svm, alpha_k)

			# 选取第二个变量, 使得alpha_j能够发生足够大的变化
			if abs(error_k - error_i) > max_step:
				max_step = abs(error_k - error_i)
				alpha_j = alpha_k
				error_j = error_k

	else:
		# 随机选择一个alpha
		alpha_j = alpha_i
		while alpha_j == alpha_i:
			alpha_j = int(np.random.uniform(0, svm.feature_size))
		error_j = calcError(svm, alpha_j)

	return alpha_j, error_j


def chooseAndUpdate(svm, alpha_i):
	"""
	SMO算法对alpha进行更新
	"""
	error_i = calcError(svm, alpha_i)

	# 判断选择出的第一个变量是否违反了KKT条件
	if (svm.label[alpha_i] * error_i < - svm.toler) and \
		(svm.alphas[alpha_i] < svm.C) or \
		(svm.label[alpha_i] * error_i > svm.toler) and \
		(svm.alphas[alpha_i] > 0):

		# 1.选择第二个变量
		alpha_j, error_j = selectSecondSample(svm, alpha_i, error_i)
        alpha_i_old = svm.alphas[alpha_i].copy()
        alpha_j_old = svm.alphas[alpha_j].copy()

        # 2. 计算上下界
        # 如果y1 != y2
        if svm.label[alpha_i] != svm.label[alpha_j]:
        	L = max(0, svm.alphas[alpha_j] - svm.alphas[alpha_i])
        	H = min(svm.C, svm.C + svm.alphas[alpha_j] - svm.alphas[alpha_i])
        else:
        	# y1 == y2
        	L = max(0, svm.alphas[alpha_j] + svm.alphas[alpha_i] - svm.C) 
        	H = min(svm.C, svm.alphas[alpha_j] + svm.alphas[alpha_i])

        # 收敛
        if L == H:
        	return 0

        # 3. 计算eta
        




def svmTrain(train_x, label, C, toler, max_iter, kernel_option = ('rbf', 0.431029)):
	# 1. 初始化SVM分类器
	svm = SVM(train_x, label, C, toler, kernel_option)

	# 2. 训练
	entire_set = True # 所有样本
	alpha_pairs_changed = 0
	iteration = 0

	while (iteration < max_iter) and ((alpha_pairs_changed > 0) or entire_set):
		print("Iteration: %d" % iteration)
		alpha_pairs_changed = 0

		if entire_set:
			# 对所有样本
			for x in range(svm.feature_size):
				alpha_pairs_changed += chooseAndUpdate(svm, x)
		else:
			bound_samples = []
			for i in range(svm.feature_size):
				if svm.alphas[i, 0] > 0 and svm.alphas[i, 0] < svm.C:
					bound_samples.append(i)
			for x in bound_samples:
				alpha_pairs_changed += chooseAndUpdate(svm, x)

		iteration += 1

        # 在所有样本和非边界样本之间交替
        if entire_set:
            entire_set = False
        elif alpha_pairs_changed == 0:
            entire_set = True

    return svm