# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea
import pickle

class MyProblem(ea.Problem): # 继承Problem父类
    def __init__(self):
        name = 'MyProblem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数）
        maxormins = [1] # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        self.Dim = 5 # 初始化self.Dim（决策变量维数）
        varTypes = [0 for _ in range(self.Dim)] # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [-300 for _ in range(self.Dim)] # 决策变量下界
        ub = [300 for _ in range(self.Dim)] # 决策变量上界
        lbin = [1, 1, 1, 1, 0.7]
        ubin = [1, 1, 0.3, 1, 0.7]
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, self.Dim, varTypes, lb, ub, lbin, ubin)
    
    def aimFunc(self, pop): # 目标函数
        model = self.loadModel()
        X = pop.Phen # 得到决策变量矩阵
        # print(X)
        feature = []
        for i in range(self.Dim):
            feature.append(X[:, [i]][0])
        val = model.predict(X)
        ret = []
        for v in val:
            ret.append(v)
        x = np.array(ret)
        x = x[:, np.newaxis]
        pop.ObjV = x
    
    def loadModel(self):
        modelName = "singleModel/ElasticNet"
        modelPath = "../../data/{}.model".format(modelName)
        model = pickle.load(open(modelPath, 'rb'))

        return model