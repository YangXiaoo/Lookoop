# coding:utf-8
# 2019-12-10
# 强化学习优化
import sys
sys.path.append("../")

import logging
import numpy as np
import geatpy as ea
import pickle

import model
from util import io, tool
from quadRegresstion import *

# 日志设置
LOGGER_PATH = "../log"
logger = tool.getLogger(LOGGER_PATH)
logger.setLevel(logging.INFO)

# 模型路径format
modelPathFormat = r"C:\Study\github\Lookoops\tool\毕设代码\data/{}.model"
singleModelPathFormat = r"C:\Study\github\Lookoops\tool\毕设代码\data/singleModel/{}.model"

def getModelName():
    """获得选择出来的最佳模型名称"""
    names = ["quadraticRegression", "stackingModel"]

    return names

def getSingleModel():
    """获得单个模型的名称"""
    names, models = model.getModel()

    return names


EPSILON = 0.1
MAX_STEP = 5000

class Env(object):
    """最小值寻优环境"""
    def __init__(self, agent, dim, lowBoundary, upBoundary, initPost=None, checkLens=500):
        """初始化
        @param agent 代理模型，提供predict(X)接口
        @param int dim 变量维数
        @param [] lowBoundary  变量下界
        @param [] upBoundary 变量上界
        @param [,None] initPost  初始位置，默认位置中间点
        @param int checkLens 终止寻找取决长度
        """
        self.agent = agent
        self.step = 0   # 步数记录
        self.optimalValue = None
        self.dim = dim
        self.lowBoundary = lowBoundary
        self.upBoundary = upBoundary
        self.curPos = self.initPosition(initPost)   # 当前位置记录
        self.checkLens = checkLens      # 判断最优值终止结果步长
        self.computeStore = [None]      # 计算结果记录
        self.optimalStore = [None]      # 最优值记录
        self.isEnd = False  # 计算终止
        self.candidate = self.initCan(dim, lowBoundary, upBoundary)

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

    def initCan(self, dim, lowBoundary, upBoundary):
        """初始候选值"""
        candidate = []
        for i in range(dim):
            tmpCandidate = [i for i in range(lowBoundary[i], upBoundary[i])]
            candidate.append(tmpCandidate)

        return candidate

    def interact(self, action):
        """在指定动作，返回奖赏"""
        assert self.isEnd == False

        reward = 0

        # 跟新当前位置，获取当前位置的候选值
        if not self.checkBoundary(action):  # 检测边界
            return reward
        for i in range(len(action)):
            self.curPos[i] += action[i]
        value = self.getCurCandidateValue()

        computeValue = self.agent.predict([value])
        self.computeStore.append(computeValue)

        # 更新最佳值, 计算奖赏值
        if not self.optimalValue:
            self.optimalValue = computeValue
        else:
            reward = self.rewardJudge(computeValue)
            if computeValue < self.optimalValue:
                self.optimalValue = computeValue

        self.step += 1
        self.optimalStore.append(self.optimalValue)
        self.checkOptimalValue()  # 检查存储值的差值，低于某个阈值后结束迭代

        return reward

    def checkBoundary(self, action):
        """检测是否越过边界"""
        ret = True
        for i in range(self.dim):
            if self.curPos[i]+action[i] >= len(self.candidate[i]) or self.curPos[i]+action[i] < 0:
                ret = False
                break

        return ret

    def getCurCandidateValue(self):
        """获得当前位置的候选值"""
        value = []
        for i in range(self.dim):
            value.append(self.candidate[i][self.curPos[i]])

        return value

    def rewardJudge(self, computeValue):
        """奖赏判断"""
        lmb = 0.01     # lambda
        reward = (self.optimalValue - computeValue) * lmb  # 奖赏返回差值，越小奖赏越多

        return reward

    def checkOptimalValue(self):
        """检测最优值在最近迭代步长中是否改变，没有改变的话结束迭代"""
        lastValue = self.optimalStore[len(self.optimalStore)-self.checkLens:]

        if lastValue == lastValue[::-1]:
            self.isEnd = True
            logger.debug("find cur iteration optimal value, stop cur iteration")

    @property
    def state(self):
        pass

    @property
    def presentState(self):
        """当前位置"""
        return self.curPos

    def printOptimalValue(self):
        """打印最佳值"""
        logger.info("cur optimal var: {}, optimal value: {}".format(self.getCurCandidateValue(), self.optimalValue))

    def getOptimalValue(self):
        """最佳值"""
        return self.getCurCandidateValue(), self.optimalValue
    

class QClass(object):
    """奖赏结构"""
    def __init__(self, dim, lowBoundary, upBoundary):
        self.alpha = 0.1
        self.gamma = 0.9

        self.dim = dim
        self.q = [[] for i in range(dim)]
        for i in range(dim):
            self.q[i] = np.zeros((abs(upBoundary[i]- lowBoundary[i]), 3))


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


def epsilonGreedy(Q, state):
    """e-贪心算法"""
    if (np.random.uniform() > 1 - EPSILON) or ((Q.getCurOptAction(state) == 0).all()):
        action = [np.random.randint(-1, 2) for i in range(Q.dim)]
    else:
        action = Q.getCurOptAction(state)

    return action

def generatePos(lowBoundary, upBoundary, splitPointCount):
    """生成不同区域初始起点"""
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
    # [[120, 240, 360, 480], [120, 240, 360, 480], [80, 160, 240, 320], [120, 240, 360, 480], [80, 160, 240, 320]]
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

def main():
    dim = 5     # 变量维数
    lowBoundary = [-300, -300, -300, -300, -200]    # 变量下界值
    upBoundary = [300, 300, 100, 300, 200]          # 变量上界值
    modelName = getModelName()[1]
    modelPath = modelPathFormat.format(modelName)   # quadraticRegression
    agent = io.getData(modelPath)   # 代理模型
    maxIter = 10    # 最大迭代数
    splitPointCount = 3
    initPos = generatePos(lowBoundary, upBoundary, splitPointCount) # [None]

    logger.info("using model: {}".format(modelName))
    logger.info("dim: {}, lowBoundary: {}, upBoundary: {}, maxIter: {}, splitPointCount: {}, posSize:{}, MAX_STEP: {}".format(dim, lowBoundary, upBoundary, maxIter, splitPointCount, len(initPos), MAX_STEP))
    for pos in initPos:
        Q = QClass(dim, lowBoundary, upBoundary)
        logger.info("using initial position: {}".format(pos))
        bestValue = []
        for it in range(maxIter):
            logger.debug("iter: {}".format(it))
            e = Env(agent, dim, lowBoundary, upBoundary, initPost=pos)
            action = epsilonGreedy(Q, e.presentState)
            while (e.isEnd is False) and (e.step < MAX_STEP):
                logger.debug("e.step: {}".format(e.step))
                state = e.presentState
                reward = e.interact(action) # 计算当前动作的奖赏
                newState = e.presentState
                newAction = epsilonGreedy(Q, newState)
                Q.updateStateAndAction(state, action, newState, newAction, reward)
                action = newAction
                # e.printOptimalValue()
                bestValue.append([e.getOptimalValue()[1], e.getOptimalValue()[0]])
        bestValue.sort()
        logger.info("bestValue store: {}".format(bestValue[0]))

def testGeneratePoints():
    """测试-网格划分生成"""
    lowBoundary = [-300, -300, -300, -300, -200]
    upBoundary = [300, 300, 100, 300, 200]
    ret = generatePos(lowBoundary, upBoundary)

if __name__ == '__main__':
    main()
