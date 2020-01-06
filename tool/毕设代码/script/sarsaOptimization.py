# coding:utf-8
# 2019-12-10
# 强化学习优化
import sys
sys.path.append("../")

import os 
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import matplotlib.pyplot as plt
import datetime
import logging
import numpy as np
import pickle

import model
from util import io, tool
from quadRegresstion import *

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.INFO)
logger.info("{}-new-log-{}".format('*'*30, '*'*30))
startTime = datetime.datetime.now()                     # 程序运行起始时间
TODAY = str(datetime.datetime.today()).split(" ")[0]    # 当前日期 2020-1-5

# 模型路径format
modelPathFormat = "../data/{}.model"
singleModelPathFormat = "../data//singleModel/{}.model"
QSavingPath = "../data/sarsaModel/sarsa-{}.model".format(TODAY)

globalOptimalValue = None # 全局最优解

def getModelName():
    """获得选择出来的最佳模型名称"""
    names = ["quadraticRegression", "stackingModel"]

    return names

def getSingleModel():
    """获得单个模型的名称"""
    names, models = model.getModel()

    return names

class EnvHandler(object):
    """最小值寻优框架"""
    def __init__(self, dim, checkLens, lmb):
        """初始化
        @param int dim 决策变量维数
        @param int checkLens 终止寻找取决长度
        @param float lmb 奖赏学习率
        """
        self.dim = dim
        self.checkLens = checkLens
        self.lmb = lmb

        self.alpha = 1e-4

        self.optimalValue = None    # 最优目标值
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

    def rewardJudge(self, computeValue):
        """奖赏判断,随着步数增加，减少负反馈影响，后期相当于先探探路"""
        self.descend()
        reward = (self.optimalValue - computeValue) * self.lmb  # 奖赏返回差值
        if reward > 0:  # 强化正反馈(削弱负反馈)
            reward /= self.lmb

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
        plt.savefig(picSavingPath)

    def saveRewardSnapShot(self, picSavingPath="rewardSnapShot.jpg"):
        """绘制最佳值与历史值的曲线图, X轴为迭代步，Y轴为当前最佳值"""
        plt.close() 
        x = [i for i in range(self.step)]
        plt.plot(x, self.rewardStore, label="reward value")
        plt.xlabel('Number of step')
        plt.ylabel('value')
        plt.savefig(picSavingPath)


class Env(EnvHandler):
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
        self.curPosition = self.initPosition(initPost)   # 当前位置记录
        self.vardidate = self.initCandidate(dim, lowBoundary, upBoundary)

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
        vardidate = []
        for i in range(dim):
            tmpCandidate = [i for i in range(lowBoundary[i], upBoundary[i])]
            vardidate.append(tmpCandidate)

        return vardidate

    def interact(self, action):
        """在指定动作，返回奖赏"""
        # assert self.isEnd == False
        reward = 0

        # 更新当前位置，获取当前位置的候选值
        if not self.checkBoundary(action):  # 检测边界
            return reward
        for i in range(len(action)):
            self.curPosition[i] += action[i]
        varValue = self.getCandidateValue(self.curPosition)

        # 预测候选值并保存
        computeValue = self.agent.predict([varValue])

        self.step += 1

        # 更新最佳值, 计算奖赏值
        if not self.optimalValue:
            self.optimalValue = computeValue
            self.optimalPosition = self.curPosition[:]  # 深度复制
        else:
            reward = self.rewardJudge(computeValue)
            if computeValue < self.optimalValue:
                # logger.info("step: {}, enter into test line".format(self.step))
                self.optimalValue = computeValue
                self.optimalPosition = self.curPosition[:]
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
            if self.curPosition[i]+action[i] >= len(self.vardidate[i]) or self.curPosition[i]+action[i] < 0:
                ret = False
                break

        return ret
    
    def getCandidateValue(self, curPosition):
        """获得指定位置的候选值"""
        value = []
        for i in range(self.dim):
            value.append(self.vardidate[i][curPosition[i]])

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
        return self.curPosition
    
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
            self.curPosition[i] += action[i]
        varValue = self.getCandidateValue(self.curPosition)
        # 预测候选值并保存
        computeValue = self.agent.predict([varValue])

        self.step += 1

        # 更新最佳值, 计算奖赏值
        if not self.optimalValue:
            self.optimalValue = computeValue
            self.optimalPosition = self.curPosition[:]  # 深度复制
        else:
            if computeValue < self.optimalValue:
                self.optimalValue = computeValue
                self.optimalPosition = self.curPosition[:]
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
            action = [np.random.randint(-1, 2) for i in range(Q.dim)] # 决策动作
        else:
            action = Q.getCurOptAction(state)

        return action

    @staticmethod
    def epsilonGreedyExcutor(Q, state):
        """e-贪心算法，对训练好的模型进行执行动作"""
        if (Q.getCurOptAction(state) == 0).all():
            action = [np.random.randint(-1, 2) for i in range(Q.dim)] # 决策动作
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
            self.q[i] = np.zeros((abs(upBoundary[i]- lowBoundary[i]), actionDim))

     
    def updateStateAndAction(self, state, action, newState, newAction, reward):
        """更新奖赏"""
        for i in range(self.dim):
            self.q[i][action[i]] = (1 - self.alpha) * self.q[i][action[i]] \
                + self.alpha * (reward + self.gamma * self.q[i][newAction[i]])

    
    def getCurOptAction(self, state):
        """基于当前奖赏的最佳动作"""
        action = []
        for i in range(self.dim):
            curAction = (self.q[i][state[i], :]).argmax()
            action.append(curAction)

        return np.array(action)


def generatePoints(lowBoundary, upBoundary, splitPointCount):
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
    """交叉组合"""
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
    plt.savefig(picSavingPath)

def saveProfileOfCheckLens(checkLensStore, picSavingPath="checkLens.jpg"):
    """绘保存收敛步数曲线为图片"""
    x = [i for i in range(len(checkLensStore))]
    plt.close()
    plt.plot(x, checkLensStore, label="value")
    plt.xlabel('Number of iter')
    plt.ylabel('value')
    plt.savefig(picSavingPath)


# 全局变量
EPSILON = 0.1       # 直接执行动作的概率
MAX_STEP = 10000   # 最大迭代步长

def excute():
    """针对训练好的模型进行寻优"""
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

    QSavingPath = "../data/Q.model"
    
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
        savingDir = "sarsaModelExcuteResults/{}".format(TODAY)
        tool.mkdirs(savingDir)
        e.saveValueSnapShot('{}/optimalValueRecord.jpg'.format(savingDir))
        e.saveVarSnapShot('{}/varRecord.jpg'.format(savingDir))

        # 打印结果
        logger.info("end step: {}, best result appears in step: {}, variabl: {}, optimal value: {}"
                    .format(e.step, e.optimalStep, var, value))

def train():
    """单目标，多约束寻优问题"""
    global globalOptimalValue, MAX_STEP

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
    maxIter = 5        # 最大迭代数
    checkLens = 500     # 检测最优最大步数
    lmb = 1     # 奖赏值学习率
    elta = 2
    gamma = 0.2 # 检查最优值的最大步数学习率
    preOptimalValueDistance = 0 # 上一次迭代中前后两次最优解之间的步数间隔

    # 初始化起点位置
    splitPointCount = 1
    # initPos = generatePoints(lowBoundary, upBoundary, splitPointCount) 
    initPos = [[300, 300, 300, 300, 200]] # 最原始的模型尺寸

    # 结果保存路径
    savingDir = "sarsaResults/{}".format(TODAY)
    tool.mkdirs(savingDir)

    # 打印当前运行参数信息
    logger.info("The global optimalValue is not enabled")
    logger.info("using model: {}".format(modelName))
    logger.info("dim: {}, actionDim: {}, lowBoundary: {}, upBoundary: {}, \
        maxIter: {}, init checkLens: {}, lmb: {}, splitPointCount: {}, pointsSize:{}, \
        EPSILON: {}, MAX_STEP: {}"\
        .format(dim, actionDim, lowBoundary, upBoundary, 
                maxIter, checkLens, lmb, splitPointCount, len(initPos),
                EPSILON, MAX_STEP))

    totalIter = len(initPos) * maxIter  # 总迭代数
    count = 1   # 记录迭代数

    # 训练
    Q = QFunction(dim, actionDim, lowBoundary, upBoundary)
    globalBestValue = []
    for index, pos in enumerate(initPos): # 选择不同的起点进行
        logger.info("using initial position: {}".format(pos))
        resultForEachStep = []
        bestValue = []
        checkLensStore = [checkLens]
        preCheckLens = checkLens
        for it in range(maxIter):
            curPos = pos[:] # 深度复制
            e = Env(agent, dim, lowBoundary, upBoundary, initPost=curPos, checkLens=checkLens, lmb=lmb)
            action = QExcutor.epsilonGreedy(Q, e.presentState)
            while (e.isEnd is False) and (e.step < MAX_STEP):
                state = e.presentState
                reward = e.interact(action) # 计算当前动作的奖赏
                newState = e.presentState   # 获得当前状态
                newAction = QExcutor.epsilonGreedy(Q, newState)  # 根据累积奖赏获得当前状态的下一个动作
                Q.updateStateAndAction(state, action, newState, newAction, reward)  # 更新状态和动作
                action = newAction

            # 更新收敛检查步数
            # checkLens *= elta
            checkLens = abs(int(preCheckLens + elta * checkLens * (e.optimalStep / e.step - gamma)))
            checkLensStore.append(checkLens)
            preOptimalValueDistance = e.getOptimalValueDistance()

            var, value = e.getOptimalValue()

            # 记录每个迭代的最佳值
            if var and value:
                resultForEachStep.append([it, var, value])
            if not bestValue or value < bestValue[2]:
                bestValue = [it, var, value, pos]
                curOptimalModelPath = os.path.join(os.path.dirname(QSavingPath), "p-{}-iter-{}-{}".format(index, it, os.path.basename(QSavingPath)))
                io.saveData(Q, curOptimalModelPath)

            # 按日期为目录保存绘制的结果曲线
            e.saveValueSnapShot('{}/optimalValueRecord-iter-{}.jpg'.format(savingDir, it))
            e.saveVarSnapShot('{}/varRecord-iter-{}.jpg'.format(savingDir, it))
            e.saveRewardSnapShot('{}/rewardRecord-iter-{}.jpg'.format(savingDir, it))

            # 预估剩余运行时间
            curTime = datetime.datetime.now() 
            curRunTime = curTime - startTime
            meanIterRunTime = curRunTime / count 
            estimateTime = (totalIter - count) * meanIterRunTime

            count += 1

            # 打印当前变动参数，当前最佳值，预估仍需要运行时间的时间
            logger.info("iter: {}, end step: {}, best value appears in step: {},\n\
                        optimal var: {}, optimal value: {},\n\
                        next checkLens: {}, preOptimalValueDistance: {},\n\
                        cur best value appears in iter: {},\n\
                        cur best optimal var:{}, cur best optimal value: {},\n\
                        still need to run: {}"
                        .format(it, e.step, e.optimalStep, 
                                var, value, 
                                checkLens, preOptimalValueDistance, 
                                bestValue[0], 
                                bestValue[1], bestValue[2], 
                                str(estimateTime)))
            
        saveProfileOfCheckLens(checkLensStore, '{}/checkLens-{}.jpg'.format(savingDir, index))
        saveProfileOfResults(resultForEachStep, '{}/result-{}.jpg'.format(savingDir, index))
        logger.info("based on cur initial position, best value appears in iter: {}, var: {},  bestValue : {}"\
                    .format(bestValue[0], bestValue[1], bestValue[2]))

        if not globalBestValue or globalBestValue[2] > bestValue[2]:
            globalBestValue = bestValue

    logger.info("global best value: {}".format(globalBestValue))
    endTime = datetime.datetime.now() 
    logger.info("run time: {}".format(str(endTime - startTime)))
    io.saveData(Q, QSavingPath)

def testGeneratePoints():
    """测试-网格划分生成"""
    lowBoundary = [-300, -300, -300, -300, -200]
    upBoundary = [300, 300, 100, 300, 200]
    ret = generatePoints(lowBoundary, upBoundary)


if __name__ == '__main__':
    train()