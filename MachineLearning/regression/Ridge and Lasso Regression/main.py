# coding:UTF-8
# 2018-10-12
# 岭回归和Lasso回归
# BFGS算法： https://blog.csdn.net/itplus/article/details/21897443

import numpy as np

def loadData(file_path):
    '''导入训练数据
    input:  file_path(string):训练数据
    output: feature(mat):特征
            label(mat):标签
    '''
    f = open(file_path)
    feature = []
    label = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        feature_tmp.append(1)
        for i in range(len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        feature.append(feature_tmp)
        label.append(float(lines[-1]))
    f.close()
    return np.mat(feature), np.mat(label).T


def ridgeRegression(feature, label, lam):
    """
    利用最小二乘法求解岭回归模型的参数
    """
    n = np.shape(feature)[1]

    w = (feature.T * feature + lam * np.mat(np.eye(n))).I * feature.T * label

    return w


def getGradient(feature, label, w, lam):
    err = (label - feature * w).T   
    left = err * (-1) * feature 

    return left.T + lam * w


def getResult(feature, label, w, lam):
    """
    获得平方差
    """
    y = (label - feature * w).T * (label - feature * w)
    wx = lam * w.T * w
    return y + wx # (left + right) / 2


def getError(feature, label, w):
    m = np.shape(feature)[0]
    left = (label - feature * w).T * (label - feature * w)
    return (left / (2 * m))[0, 0]


def bfgs(feature, label, lam, max_iter, sigma, delta):
    """
    牛顿法BFGS
    https://blog.csdn.net/itplus/article/details/21897443
    """
    n = np.shape(feature)[1]
    w0 = np.mat(np.zeros((n, 1)))
    Bk = np.eye(n)
    it = 1
    while it <= max_iter:
        print("iter: ", it, " loss: ", getError(feature, label, w0))

        gk = getGradient(feature, label, w0, lam)
        dk = np.mat(-np.linalg.solve(Bk, gk))

        m = 0
        mk = 0
        while m < 20:
            left = getResult(feature, label, (w0 + (delta**m) * dk), lam)
            right = getResult(feature, label, w0, lam)

            if left < right + sigma * (delta**m) * (gk.T * dk)[0, 0]:
                mk = m 
                break
            m += 1

        # 校正
        w = w0 + (delta**mk) * dk
        sk = w - w0
        yk = getGradient(feature, label, w, lam) - gk
        if yk.T * sk > 0:
            Bk = Bk - (Bk * sk * sk.T * Bk) / (sk.T * Bk * sk) + (yk * yk.T) / (yk.T * sk) 

        it += 1
        w0 = w

    return w0


def lbfgs(feature, label, lam, maxCycle, m=10):
    n = np.shape(feature)[1]
    # 1、初始化
    w0 = np.mat(np.zeros((n, 1)))
    rho = 0.55
    sigma = 0.4
    
    H0 = np.eye(n)
    
    s = []
    y = []
    
    k = 1
    gk = getGradient(feature, label, w0, lam)  # 3X1
    # print gk
    dk = -H0 * gk
    # 2、迭代
    while (k < maxCycle):
        print("iter: ", k, "\terror: ", getError(feature, label, w0) )
        m = 0
        mk = 0
        gk = getGradient(feature, label, w0, lam)
        # 2.1、Armijo线搜索
        while (m < 20):
            newf = getResult(feature, label, (w0 + rho ** m * dk), lam)
            oldf = getResult(feature, label, w0, lam)
            if newf < oldf + sigma * (rho ** m) * (gk.T * dk)[0, 0]:
                mk = m
                break
            m = m + 1
        
        # 2.2、LBFGS校正
        w = w0 + rho ** mk * dk
        
        # 保留m个
        if k > m:
            s.pop(0)
            y.pop(0)
        
        # 保留最新的
        sk = w - w0
        qk = getGradient(feature, label, w, lam)  # 3X1
        yk = qk - gk
        
        s.append(sk)
        y.append(yk)
        
        # two-loop
        t = len(s)
        a = []
        for i in range(t):
            alpha = (s[t - i - 1].T * qk) / (y[t - i - 1].T * s[t - i - 1])
            qk = qk - alpha[0, 0] * y[t - i - 1]
            a.append(alpha[0, 0])
        r = H0 * qk
        
        for i in range(t):
            beta = (y[i].T * r) / (y[i].T * s[i])
            r = r + s[i] * (a[t - i - 1] - beta[0, 0])
            
        if yk.T * sk > 0:
            print("update OK!!!!")
            dk = -r
        
        k = k + 1
        w0 = w
    return w0

def getPrediction(data, w):
    '''
    预测
    '''
    return data * w

if __name__ == "__main__":
    # 1、导入数据
    print("loading data ...")
    feature, label = loadData("data.txt")
    # 2、训练模型
    print ("traing...")
    method = "bfgs"  # 选择的方法
    if method == "bfgs":  # 选择BFGS训练模型
        print("using BFGS...")
        w0 = bfgs(feature, label, 0.5, 50, 0.4, 0.55)
    elif method == "lbfgs":  # 选择L-BFGS训练模型
        print("using L-BFGS...")
        w0 = lbfgs(feature, label, 0.5, 50, m=10)
    else:  # 使用最小二乘的方法
        w0 = ridgeRegression(feature, label, 0.5)

    print(w0)
