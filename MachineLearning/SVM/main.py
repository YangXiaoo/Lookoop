# 2018-10-3
# Support Vector Machines
# python 机器学习算法
# 拉格朗日对偶问题 https://blog.csdn.net/blackyuanc/article/details/67640844
import numpy as np
# import cPickle as pickle

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
        while len(feature_tmp) < 13:
            feature_tmp.append(0)
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
        kernel_matrix[: , i] = calcKernelValue(train_x, train_x[i, :], kernel_opt)
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
            # print(train_x[i, :] , train_x_i)
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
    # 1. 若yE < 0, 即yg < 1时，此时若a < C则违反KKT条件
    # 2. 若yE > 0, 即yg > 1时，此时若a > 0则违反KKT条件
    # 3. 若yE = 0, 即yg = 1时，表明是支持向量, 无序优化
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
        eta = svm.kernel_mat[alpha_i, alpha_i] + svm.kernel_mat[alpha_j, alpha_j] - \
            2 * svm.kernel_mat[alpha_i, alpha_j]

        if eta <= 0:
            return 0

        # 4. 更新alpha_j
        svm.alphas[alpha_j] += svm.label[alpha_j] * (error_i - error_j) / eta

        # 5. 确定最终的alpha_j
        if svm.alphas[alpha_j] > H:
            svm.alphas[alpha_j] = H
        if svm.alphas[alpha_j] < L:
            svm.alphas[alpha_j] = L 

        # 6. 判断是否结束
        if abs(alpha_j_old - svm.alphas[alpha_j]) < 0.00001:
            chooseAndUpdate(svm, alpha_j)
            return 0

        # 7. 更新alpha_i
        svm.alphas[alpha_i] += svm.label[alpha_i] * svm.label[alpha_j] * \
            (alpha_j_old -svm.alphas[alpha_j])


        # 8. 更新b1, b2
        b1 = -error_i - svm.label[alpha_i] * (svm.alphas[alpha_i] - alpha_i_old) * svm.kernel_mat[alpha_i, alpha_i] - \
             svm.label[alpha_j] * (svm.alphas[alpha_j] - alpha_j_old) * svm.kernel_mat[alpha_i, alpha_j] + svm.b# 有问题svm.kernel_mat[alpha_j, alpha_i]

        b2 = - error_j - svm.label[alpha_i] * (svm.alphas[alpha_i] - alpha_i_old) \
            * svm.kernel_mat[alpha_i, alpha_j] \
            - svm.label[alpha_j] * (svm.alphas[alpha_j] - alpha_j_old) \
            * svm.kernel_mat[alpha_j, alpha_j] + svm.b

        if svm.alphas[alpha_i] > 0 and svm.alphas[alpha_i] < svm.C:
            svm.b = b1
        elif 0 < svm.alphas[alpha_j] and svm.alphas[alpha_j] < svm.C:
            svm.b = b2
        else:
            svm.b = (b1 + b2) / 2.0

        # 9. 更新error
        updateErrorTmp(svm, alpha_i)
        updateErrorTmp(svm, alpha_j)

        return 1
    else:
        return 0



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


def svmPredict(svm, test_data):
    kernel_value = calcKernelValue(svm.train_x, test_data, svm.kernel_opt)
    prediction = kernel_value.T * np.multiply(svm.label, svm.alphas) + svm.b 
    return prediction


def calcAccurancy(svm, test_x, test_label):
    n_sample = np.shape(test_x)[0]
    correct = 0
    for i in range(n_sample):
        prediction = svmPredict(svm, test_x[i, :])
        if np.sign(prediction) == np.sign(test_label[i]):
            correct += 1
    accurancy = correct / n_sample

    return accurancy


def saveModle(svm_model, model_file):
    pass


if __name__ == "__main__":
    # 1、导入训练数据
    dataSet, labels = loadDate("heart_scale")
    # 2、训练SVM模型
    C = 0.6
    toler = 0.001
    maxIter = 500
    svm_model = svmTrain(dataSet, labels, C, toler, maxIter)
    # 3、计算训练的准确性
    accuracy = calcAccurancy(svm_model, dataSet, labels)  
    print ("The training accuracy is: %.3f%%" % (accuracy * 100))
    # 4、保存最终的SVM模型
    saveModle(svm_model, "model_file")