# coding:utf-8
# 2020-5-10
# 对简单三维曲面进行寻优
"""
寻优的代理模型见SimpleModel类定义
"""
import sys
sys.path.append("../")

import os 
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import datetime
import logging
import numpy as np
import pickle
import random

from model import getModel
from util import io, tool
# from quadRegresstion import *

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.INFO)

startTime = datetime.datetime.now()                     # 程序运行起始时间
TODAY = str(datetime.datetime.today()).split(" ")[0]    # 当前日期 2020-1-5

# 模型路径format
modelPathFormat = "../data/{}.model"
singleModelPathFormat = "../data/singleModel/{}.model"
QSavingPath = "../data/sarsaModel/{}/sarsa.model".format(TODAY)
sarsaResultsSavingDir = "sarsaResults/{}".format(TODAY) # # 结果保存路径

globalOptimalValue = None # 全局最优解
globalAdder = 10

def checkDirIsExist():
    """检查signleModelPath,QSavingPath,sarsaResultsSavingDir目录是否存在，如果不存在则创建"""
    tool.mkdirs(os.path.dirname(singleModelPathFormat))
    tool.mkdirs(os.path.dirname(QSavingPath))
    tool.mkdirs(sarsaResultsSavingDir)


class SimpleModel():
    def __init__(self):
        pass

    def fit(self):
        pass

    def predict(self, x):
        x = x[0]
        return x[0]**2 + x[1]**2 + 2


class EnvHandler(object):
    """最小值寻优框架"""
    def __init__(self, dim, checkLens, lmb):
        """初始化
        @param int dim 决策变量维数
        @param int checkLens 终止寻找取决长度
        @param float lmb 奖赏学习率
        """
        global globalOptimalValue
        self.dim = dim
        self.checkLens = checkLens
        self.lmb = lmb

        self.alpha = 1e-5

        self.optimalValue = globalOptimalValue    # 最优目标值
        self.optimalPosition = None # 最优目标位置
        self.computeValueStore = []      # 计算结果记录
        self.optimalValueStore = []      # 最优值记录
        self.optimalVarStore = []   # 记录最优决策变量值
        self.varStore = []  # 记录决策变量值
        self.rewardStore = []

        self.isEnd = False  # 计算终止
        self.step = 0       # 步数记录
        self.optimalStep = 1

    def interact(self, action):
        """根据动作返回奖赏"""
        pass

    def descend(self):
        """修改学习率降,加速降低"""
        self.lmb = (1 - self.alpha) * self.lmb

    def rewardJudge01(self, computeValue):
        """奖赏判断,随着步数增加，减少负反馈影响
        根据实验，下一步的值比上一步的值大，若奖赏变为负数则会导致解永远在局部产生，所以奖赏值为负数时将奖赏值变为0
        """
        # self.descend()
        # reward = (self.optimalValue - computeValue) * self.lmb  # 奖赏返回差值
        reward = self.optimalValue - computeValue  # 奖赏返回差值
        if reward >= 0:  # 强化正反馈(削弱负反馈)
            # reward /= self.lmb
            reward = reward # or 50
        else:
            reward = 0

        return reward

    def rewardJudge(self, computeValue):
        """奖赏判断,随着步数增加，减少负反馈影响
        根据实验，下一步的值比上一步的值大，若奖赏变为负数则会导致解永远在局部产生，所以奖赏值为负数时将奖赏值变为0
        """
        global globalAdder
        reward = self.optimalValue - computeValue  # 奖赏返回差值
        if reward >= 0:  # 强化正反馈(削弱负反馈)
            # reward /= self.lmb
            globalAdder += 10
            reward = globalAdder
        else:
            reward = 0

        return reward

    def getOptimalValueDistance(self):
        """获得两个最优值之间最大的间隔距离"""
        maxGap = 0
        preIndex = 0
        for i in range(self.step-1):
            if self.optimalVarStore[i] != self.optimalVarStore[i+1]:
                curGap = i - preIndex
                if curGap > maxGap:
                    maxGap = curGap
                    preIndex = i

        return maxGap

    def saveValueSnapShot(self, picSavingPath="valueSnapShot.jpg"):
        """绘制最佳值与历史值的曲线图, X轴为迭代步，Y轴为当前最佳值"""
        plt.close()
        x = [i for i in range(self.step)]
        plt.plot(x, self.computeValueStore, label="compute value")
        plt.plot(x, self.optimalValueStore, label="optimal value")
        plt.xlabel('Number of step')
        plt.ylabel('value')
        # plt.title("Simple Plot")
        plt.legend()
        plt.savefig(picSavingPath)
        # plt.show()

    def saveVarSnapShot(self, picSavingPath="varSnapShot.jpg"):
        """绘制决策变量的曲线, X轴迭代步, Y轴决策变量的值"""
        plt.close() 
        fig, (ax1, ax2) = plt.subplots(2, 1)
        fig.subplots_adjust(hspace=0.5)
        x = [i for i in range(self.step)]
        for i in range(self.dim):
            tmpOptData = []
            tmpData = []
            for j in range(self.step):
                tmpOptData.append(self.optimalVarStore[j][i])
                tmpData.append(self.varStore[j][i])
            ax1.set_title("decision variabl")
            ax1.plot(x, tmpData, label="var-{}".format(i))
            ax1.set_xlabel("Number of step")
            ax1.set_ylabel("value")

            ax2.set_title("optimal variabl")
            ax2.plot(x, tmpOptData, label="opt-var-{}".format(i))
            ax2.set_xlabel("Number of step")
            ax2.set_ylabel("value")

        fig.tight_layout()
        plt.legend()
        plt.savefig(picSavingPath)

    def saveRewardSnapShot(self, picSavingPath="rewardSnapShot.jpg"):
        """绘制最佳值与历史值的曲线图, X轴为迭代步，Y轴为当前最佳值"""
        plt.close() 
        x = [i for i in range(self.step)]
        plt.plot(x, self.rewardStore, label="reward value")
        plt.xlabel('Number of step')
        plt.ylabel('value')
        plt.legend()
        plt.savefig(picSavingPath)

class SimpleEnvHandler(EnvHandler):
    def __init__(self, dim, checkLens, lmb):
        super(SimpleEnvHandler, self).__init__(dim, checkLens, lmb)
        pass

    def saveVarSnapShotOnSurface(self, picSavingPath="varSnapShotOnSurface.jpg"):
        plt.close() 
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        _x = np.arange(-10,10,0.2)
        _y = np.arange(-10,10,0.2)
        _x, _y = np.meshgrid(_x, _y)
        _z = _x**2 + _y**2 + 2
        ax.plot_surface(_x, _y, _z)

        x, y, z = [], [], []
        for j in range(self.step):
            x.append([self.varStore[j][0]])
            y.append([self.varStore[j][1]])
            z.append(self.agent.predict([[self.varStore[j][0], self.varStore[j][1]]]))
        ax.scatter(x, y, z, c='r', marker=".")
        plt.savefig(picSavingPath)

class Env(SimpleEnvHandler):
    """最小值寻优框架"""
    def __init__(self, agent, dim, lowBoundary, upBoundary, 
                initPost=None, checkLens=500, lmb=1):
        super(Env, self).__init__(dim, checkLens, lmb) # 初始化父类
        """初始化
        @param agent 代理模型，提供predict(X)接口
        @param int dim 决策变量维数
        @param [] lowBoundary  变量下界
        @param [] upBoundary 变量上界
        @param [,None] initPost  初始位置，默认位置中间点
        @param int checkLens 终止寻找取决长度
        @param float lmb 奖赏学习率
        """
        # global globalOptimalValue

        self.agent = agent
        self.lowBoundary = lowBoundary
        self.upBoundary = upBoundary
        self.state = self.initPosition(initPost)   # 当前位置记录
        self.candidate = self.initCandidate(dim, lowBoundary, upBoundary)

    def initPosition(self, initPost):
        """初始化初始位置,初始位置居中"""
        if initPost != None:
            return initPost
        posSplit = 0.5
        pos = []
        for i in range(self.dim):
            scope = self.upBoundary[i] - self.lowBoundary[i]
            pos.append(int(scope * posSplit))

        return pos 

    def initCandidate(self, dim, lowBoundary, upBoundary):
        """初始候选值"""
        candidate = []
        for i in range(dim):
            tmpCandidate = [i for i in range(lowBoundary[i], upBoundary[i])]
            candidate.append(tmpCandidate)

        return candidate

    def interact(self, action):
        """在指定动作，返回奖赏"""
        # assert self.isEnd == False
        reward = 0

        # 更新当前位置，获取当前位置的候选值
        if not self.checkBoundary(action):  # 检测边界
            return -5   # 达到边界的奖赏为负
        for i in range(len(action)):
            self.state[i] += action[i]
        varValue = self.getCandidateValue(self.state)

        # 预测候选值并保存
        computeValue = self.agent.predict([varValue])

        self.step += 1

        # 更新最佳值, 计算奖赏值
        if not self.optimalValue:
            self.optimalValue = computeValue
            self.optimalPosition = self.state[:]  # 深度复制
        else:
            reward = self.rewardJudge(computeValue)
            if computeValue <= self.optimalValue:
                # logger.info("step: {}, enter into test line".format(self.step))
                self.optimalValue = computeValue
                self.optimalPosition = self.state[:]
                self.optimalStep = self.step

        self.computeValueStore.append(computeValue)
        self.optimalValueStore.append(self.optimalValue)
        self.optimalVarStore.append(self.getCandidateValue(self.optimalPosition))
        self.varStore.append(varValue)
        self.rewardStore.append(reward)

        self.checkOptimalValueIsConvergence()  # 检查存储值的差值，低于某个阈值后结束迭代

        return reward

    def checkBoundary(self, action):
        """边界条件"""
        ret = True
        for i in range(self.dim):
            if self.state[i]+action[i] >= len(self.candidate[i]) or self.state[i]+action[i] < 0:
                ret = False
                break

        return ret
    
    def getCandidateValue(self, state):
        """获得指定位置的候选值"""
        value = []
        for i in range(self.dim):
            value.append(self.candidate[i][state[i]])

        return value
    
    def checkOptimalValueIsConvergence(self):
        """检测最优值在最近迭代步长中是否改变，没有改变的话结束迭代"""
        curOptimalStoreLens = len(self.optimalValueStore)
        if curOptimalStoreLens < self.checkLens:
            return None

        lastValue = self.optimalValueStore[curOptimalStoreLens-self.checkLens:]
        if lastValue == lastValue[::-1]:
            self.isEnd = True
            logger.debug("iteration: {}, find cur iteration optimal value, stop cur iteration".format(self.step))

    @property
    def presentState(self):
        """当前位置"""
        return self.state
    
    def getOptimalValue(self):
        """最佳值"""
        return self.getCandidateValue(self.optimalPosition), self.optimalValue

    def printOptimalValue(self):
        """打印最佳值"""
        optimalVar, optimalValue = self.getOptimalValue()
        logger.info("last step: {}, best value appears in step: {}, optimal var: {}, optimal value: {}"\
            .format(self.step, self.optimalStep, optimalVar, optimalValue))


class EnvExcutor(Env):
    """对训练好的模型执行动作提供必要环境"""
    def __init__(self, agent, dim, lowBoundary, upBoundary, initPost, checkLens):
        super(EnvExcutor, self).__init__(agent, dim, lowBoundary, upBoundary, initPost, checkLens)

    def interact(self, action):
        """根据动作，更新位置"""
        if not self.checkBoundary(action):  # 检测边界
            return 

        for i in range(len(action)):
            self.state[i] += action[i]
        varValue = self.getCandidateValue(self.state)
        # 预测候选值并保存
        computeValue = self.agent.predict([varValue])

        self.step += 1

        # 更新最佳值, 计算奖赏值
        if not self.optimalValue:
            self.optimalValue = computeValue
            self.optimalPosition = self.state[:]  # 深度复制
        else:
            if computeValue < self.optimalValue:
                self.optimalValue = computeValue
                self.optimalPosition = self.state[:]
                self.optimalStep = self.step

        self.computeValueStore.append(computeValue)
        self.optimalValueStore.append(self.optimalValue)
        self.optimalVarStore.append(self.getCandidateValue(self.optimalPosition))
        self.varStore.append(varValue)

        self.checkOptimalValueIsConvergence()  # 检查存储值的差值，低于某个阈值后结束迭代


class QExcutor(object):
    """提供执行动作策略"""
    def __init__(self):
        pass

    @staticmethod  
    def epsilonGreedy(Q, state):
        """e-贪心算法，根据当前状态获得下一个动作"""
        if (np.random.uniform() > 1 - EPSILON) or ((Q.getCurOptAction(state) == 0).all()):
            action = [random.randint(-1, 1) for i in range(Q.dim)] # 决策动作
        else:
            action = Q.getCurOptAction(state)

        return action

    @staticmethod
    def epsilonGreedyExcutor(Q, state):
        """e-贪心算法，对训练好的模型进行执行动作"""
        if (Q.getCurOptAction(state) == 0).all():
            action = [random.randint(-1, 1) for i in range(Q.dim)] # 决策动作
        else:
            action = Q.getCurOptAction(state)

        return action


class QFunction(object):
    """奖赏函数"""
    def __init__(self, dim, actionDim, lowBoundary, upBoundary):
        self.alpha = 0.1
        self.gamma = 0.9

        self.dim = dim  # 变量维度
        self.actionDim = actionDim
        self.q = [[] for i in range(dim)]   # 初始化决策概率值
        for i in range(dim):
            self.q[i] = np.zeros((abs(upBoundary[i] - lowBoundary[i]), actionDim))
     
    def updateStateAndAction(self, state, action, newState, newAction, reward):
        """更新奖赏"""
        for i in range(self.dim):
            self.q[i][state[i]][action[i]+1] = (1 - self.alpha) * self.q[i][state[i]][action[i]+1] \
                + self.alpha * (reward + self.gamma * self.q[i][newState[i]][newAction[i]+1])
    
    def getCurOptAction(self, state):
        """基于当前奖赏的最佳动作"""
        action = []
        for i in range(self.dim):
            curAction = (self.q[i][state[i], :]).argmax() - 1   # 获得当前最高动作索引，-1为真正动作
            action.append(curAction)

        return np.array(action)


def gridMeshPoints(lowBoundary, upBoundary, splitPointCount):
    """生成不同区域初始起点"""
    if splitPointCount == 0:
        return [None]
    dim = len(lowBoundary)
    pos = None
    gap = []
    for i in range(dim):
        gap.append(upBoundary[i] - lowBoundary[i])
    splitPoint = []
    for i in range(dim):
        increate = int(gap[i] // (splitPointCount + 1))
        tmpSplitPoint = []
        for j in range(splitPointCount):
            tmpSplitPoint.append(increate * (j + 1))
        splitPoint.append(tmpSplitPoint)
    # print("[DEBUG] splitPoint : {}".format(splitPoint))
    pos = crossPoint(splitPoint)

    return pos 

def crossPoint(points):
    """递归进行交叉组合
    @example points: [[1,10],[2,20],[3,30]]，返回[[1, 2, 3], [1, 2, 30], [1, 20, 3], [1, 20, 30], [10, 2, 3], [10, 2, 30], [10, 20, 3], [10, 20, 30]]
    """
    def helper(points, res):
        if not points:
            return res
        ret = []
        for i in res:
            for j in points[0]:
                ret.append(i + [j])

        return helper(points[1:], ret)

    res = [[v] for v in points[0]]

    return helper(points[1:], res)

def testGeneratePoints():
    """测试-网格划分生成"""
    lowBoundary = [-300, -300, -300, -300, -200]
    upBoundary = [300, 300, 100, 300, 200]
    ret = gridMeshPoints(lowBoundary, upBoundary)

def saveProfileOfResults(resultForEachStep, picSavingPath="result.jpg"):
    """保存结果曲线为图片"""
    x = [i for i in range(len(resultForEachStep))]
    valueStore = [x[2] for x in resultForEachStep]
    bestValueStore = []
    bestValue = None
    for i in range(len(resultForEachStep)):
        if not bestValue or resultForEachStep[i][2] < bestValue:
            bestValue = resultForEachStep[i][2]
        bestValueStore.append(bestValue)

    plt.close()
    plt.plot(x, valueStore, label="value")
    plt.plot(x, bestValueStore, label="optimal value")
    plt.xlabel('Number of iter')
    plt.ylabel('value')
    plt.legend()
    plt.savefig(picSavingPath)

def saveProfileOfCheckLens(checkLensStore, picSavingPath="checkLens.jpg"):
    """绘保存收敛步数曲线为图片"""
    x = [i for i in range(len(checkLensStore))]
    plt.close()
    plt.plot(x, checkLensStore, label="value")
    plt.xlabel('Number of iter')
    plt.ylabel('value')
    plt.legend()
    plt.savefig(picSavingPath)


# 全局变量
EPSILON = 0.1       # 直接执行动作的概率, 跳出局部解
MAX_STEP = 10000   # 最大迭代步长

def excute():
    """针对训练好的模型进行寻优"""
    logger.info("{}-sarsaOptimization-excute-{}".format('*'*25, '*'*25))
    # Env基本参数定义
    dim = 5         # 决策变量维数
    actionDim = 3   # 动作策略维度
    lowBoundary = [-300, -300, -300, -300, -200]    # 变量下界值
    upBoundary = [300, 300, 100, 300, 200]          # 变量上界值

    # 获得代理模型
    modelName = getModelName()[1]
    modelPath = modelPathFormat.format(modelName)   # quadraticRegression
    agent = io.getData(modelPath)   

    MAX_STEP = 10000
    checkLens = 1000     # 检测最优最大步数

    initPos = [[300, 300, 300, 300, 200]] # 最原始的模型尺寸

    # # 结果最优的代理模型路径
    # QSavingPath = "../data/Q.model"
    
    # 执行动作
    Q = io.getData(QSavingPath)
    for pos in initPos: # 选择不同的起点进行
        logger.info("using initial position: {}".format(pos))
        curPos = pos[:] # 深度复制
        e = EnvExcutor(agent, dim, lowBoundary, upBoundary, initPost=curPos, checkLens=checkLens)
        action = QExcutor.epsilonGreedyExcutor(Q, e.presentState)
        while (e.isEnd is False) and (e.step < MAX_STEP):
            e.interact(action) # 计算当前动作的奖赏
            state = e.presentState   # 获得当前状态
            newAction = QExcutor.epsilonGreedyExcutor(Q, state)  # 根据累积奖赏获得当前状态的下一个动作
            action = newAction
            
        var, value = e.getOptimalValue()

        # 按日期为目录保存绘制的结果曲线
        sarsaResultsSavingDir = "sarsaModelExcuteResults/{}".format(TODAY)
        tool.mkdirs(sarsaResultsSavingDir)
        e.saveValueSnapShot('{}/optimalValueRecord.jpg'.format(sarsaResultsSavingDir))
        e.saveVarSnapShot('{}/varRecord.jpg'.format(sarsaResultsSavingDir))

        # 打印结果
        logger.info("end step: {}, best result appears in step: {}, variabl: {}, optimal value: {}"
                    .format(e.step, e.optimalStep, var, value))

def train():
    """单目标，多约束寻优问题"""
    logger.info("{}-sarsaOptimization-train-{}".format('*'*25, '*'*25))
    global globalOptimalValue, MAX_STEP, EPSILON

    # Env基本参数定义
    dim = 2         # 决策变量维数
    actionDim = 3   # 动作策略维度
    lowBoundary = [-10, -10]    # 变量下界值
    upBoundary = [10, 10]          # 变量上界值

    # 获得代理模型
    modelName = "simple3d"
    agent = SimpleModel()   

    MAX_STEP = 1000
    maxIter = 500        # 最大迭代数
    checkLens = 5000     # 检测最优最大步数
    lmb = 1     # 奖赏值学习率
    # elta = 2
    # gamma = 0.8 # 检查最优值的最大步数学习率
    # preOptimalValueDistance = 0 # 上一次迭代中前后两次最优解之间的步数间隔

    # EPSILON衰减率
    preEPSILON = EPSILON    # 保存EPSILON值
    # eDescend = 0.001        # EPSILON衰减率，1000步后EPSILON衰减到0.0135

    # 初始化起点位置
    splitPointCount = 2
    initPos = gridMeshPoints(lowBoundary, upBoundary, splitPointCount) 

    # 打印当前运行参数信息
    # logger.info("The global optimalValue is not enabled, without EPSILON change")
    logger.info("The global optimalValue is enabled")
    logger.info("using model: {}".format(modelName))
    logger.info("dim: {}, actionDim: {}, lowBoundary: {}, upBoundary: {},\n\
                maxIter: {}, init checkLens: {}, lmb: {}, splitPointCount: {}, pointsSize:{},\n\
                EPSILON: {}, MAX_STEP: {}"
                .format(dim, actionDim, lowBoundary, upBoundary, 
                    maxIter, checkLens, lmb, splitPointCount, len(initPos),
                    EPSILON, MAX_STEP))

    totalIter = len(initPos) * maxIter  # 总迭代数
    count = 1   # 记录迭代数

    Q = QFunction(dim, actionDim, lowBoundary, upBoundary)  # 初始化Q函数
    logger.info("use a new QFunction")

    # # 选择上次最佳模型进行初始化
    # preOptimalModelPath = "../data/sarsaModel/p-0-iter-830-sarsa-2020-01-06.model"
    # Q = io.getData(preOptimalModelPath)
    # logger.info("initial QFunction is backup from: {}".format(preOptimalModelPath))

    # 开始训练
    globalBestValue = []
    for index, pos in enumerate(initPos): # 选择不同的起点进行
        logger.info("start training, using initial position: {}".format(pos))
        resultForEachStep = []  # 记录每一步的结果
        bestValue = []  # 记录最优结果
        checkLensStore = [checkLens]    # 记录收敛步长数
        preCheckLens = checkLens
        EPSILON = preEPSILON
        for it in range(maxIter):
            curPos = pos[:] # 深度复制
            e = Env(agent, dim, lowBoundary, upBoundary, initPost=curPos, checkLens=checkLens, lmb=lmb)
            action = QExcutor.epsilonGreedy(Q, e.presentState)
            while (e.isEnd is False) and (e.step < MAX_STEP):
                # logger.info("action: {}".format(action))
                state = e.presentState
                reward = e.interact(action) # 计算当前动作的奖赏
                newState = e.presentState   # 获得当前状态
                newAction = QExcutor.epsilonGreedy(Q, newState)  # 根据累积奖赏获得当前状态的下一个动作
                Q.updateStateAndAction(state, action, newState, newAction, reward)  # 更新状态和动作
                action = newAction[:]

            # # 更新收敛检查步数
            # # checkLens *= elta
            # checkLens = abs(int(preCheckLens + elta * checkLens * (e.optimalStep / e.step - gamma)))
            # checkLensStore.append(checkLens)
            preOptimalValueDistance = e.getOptimalValueDistance()

            var, value = e.getOptimalValue()

            if globalOptimalValue and value < globalOptimalValue:
                globalOptimalValue = value

            # 记录每个迭代的最佳值
            if var and value:
                resultForEachStep.append([it, var, value])
            if not bestValue or value < bestValue[2]:
                bestValue = [it, var, value, pos, index]
                curOptimalModelPath = os.path.join(os.path.dirname(QSavingPath), "p-{}-iter-{}-{}".format(index, it, os.path.basename(QSavingPath)))
                io.saveData(Q, curOptimalModelPath)

            # 按日期为目录保存绘制的结果曲线
            e.saveValueSnapShot('{}/optimalValueRecord-P-{}-iter-{}.jpg'.format(sarsaResultsSavingDir, index, it))
            e.saveVarSnapShot('{}/varRecord-P-{}-iter-{}.jpg'.format(sarsaResultsSavingDir, index, it))
            e.saveRewardSnapShot('{}/rewardRecord-P-{}-iter-{}.jpg'.format(sarsaResultsSavingDir, index, it))
            e.saveVarSnapShotOnSurface('{}/varRecordOnSurface-P-{}-iter-{}.jpg'.format(sarsaResultsSavingDir, index, it))
            # 预估剩余运行时间
            curTime = datetime.datetime.now() 
            curRunTime = curTime - startTime
            meanIterRunTime = curRunTime / count 
            estimateTime = (totalIter - count) * meanIterRunTime

            count += 1  # 迭代计数加1

            # 更新EPSILON值
            # EPSILON = (1 - eDescend) * EPSILON

            # 打印当前变动参数，当前最佳值，预估仍需要运行时间的时间
            logger.info("iter: {}, end step: {}, best value appears in step: {},\n\
                        optimal var: {}, optimal value: {},\n\
                        next checkLens: {}, preOptimalValueDistance: {},\n\
                        cur best value appears in iter: {},\n\
                        cur best optimal var:{}, cur best optimal value: {},\n\
                        cur EPSILON: {},\n\
                        still need to run: {}"
                        .format(it, e.step, e.optimalStep, 
                                var, value, 
                                checkLens, preOptimalValueDistance, 
                                bestValue[0], 
                                bestValue[1], bestValue[2], 
                                EPSILON,
                                str(estimateTime)))
            
        # 保存收敛步数曲线图
        # saveProfileOfCheckLens(checkLensStore, '{}/checkLens-{}.jpg'.format(sarsaResultsSavingDir, index))
        # 保存每个迭代结果曲线图以及当前最优解曲线图
        saveProfileOfResults(resultForEachStep, '{}/result-{}.jpg'.format(sarsaResultsSavingDir, index))

        # 打印使用当前初始起点的最优解
        logger.info("p: {}, based on cur initial position, best value appears in iter: {}, var: {},  bestValue : {}"\
                    .format(index, bestValue[0], bestValue[1], bestValue[2]))

        if not globalBestValue or globalBestValue[2] > bestValue[2]:
            globalBestValue = bestValue

    io.saveData(Q, QSavingPath) # 保存最终模型文件
    logger.info("global best value: {}".format(globalBestValue))
    endTime = datetime.datetime.now() 
    logger.info("run time: {}".format(str(endTime - startTime)))

checkDirIsExist()   # 创建文件保存目录

if __name__ == '__main__':
    train() 