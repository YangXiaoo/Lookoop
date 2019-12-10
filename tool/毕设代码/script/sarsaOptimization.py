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
logger.setLevel(logging.DEBUG)

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
MAX_STEP = 600

class Env(object):
    """最小值寻优,待写成通用"""
    def __init__(self, agent, dim, lowBoundary, upBoundary, initPost=None):
        self.agent = agent
        self.step = 0   # 步数记录
        self.optimalValue = None
        self.curPos = self.initPosition(initPost)   # 当前位置记录
        self.computeStore = [None]  # 计算结果记录
        self.optimalStore = [None]
        self.isEnd = False  # 计算终止
        self.candidate = self.initCan(dim, lowBoundary, upBoundary)

        self.dim = dim
        self.lowBoundary = lowBoundary
        self.upBoundary = upBoundary

    def initPosition(self, initPost):
        """初始化初始位置,初始位置居中"""
        if initPost != None:
            slef.curPos - initPost

        posSplit = 0.5
        pos = []
        for i in range(self.dim):
            scope = self.upBoundary[i] - self.lowBoundary[i]
            pos.append(scope // posSplit)

        return pos 


    def initCan(self, dim, lowBoundary, upBoundary):
        """初始候选值"""
        candidate = []
        for i in range(dim):
            tmpCandidate = [i for i in range(lowBoundary[i], upBoundary[i])]
            candidate.append(tmpCandidate)

        return candidate

    def interact(self, action):
        """指定动作，返回奖赏"""
        assert self.isEnd == False

        reward = 0

        # 跟新当前位置，获取当前位置的候选值
        if not self.checkBoundary(action):  # 检测边界
            return reward
        for i in range(len(action)):
            self.curPos[i] += action[i]
        value = self.getCurCandidateValue()

        computeValue = agent.predict(value)
        self.computeStore.append(computeValue)

        # 更新最佳值
        if not self.optimalValue:
            self.optimalValue = computeValue
        else:
            reward = self.rewardJudge(computeValue)
            if computeValue < self.optimalValue:    # 更新最优值
                self.optimalValue = computeValue

        self.step += 1
        self.optimalStore.append(self.optimalValue)
        self.checkOptimalValue()  # 检查存储值的差值，低于某个阈值后结束迭代

        return reward

    def checkBoundary(self, action):
        """检测是否越过边界"""
        ret = True
        for i in range(self.dim):
            if self.curPos[i]+action[i] > len(self.candidate[0]) or self.curPos[i]+action[i] < 0:
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
        lmb = 1     # lambda
        reward = (self.optimalValue - computeValue) * lmb  # 奖赏返回差值，越小奖赏越多

        return reward

    def checkOptimalValue(self):
        """检测最优值在最近迭代步长中是否改变，没有改变的话结束迭代"""
        checkLens = 10
        lastValue = self.optimalStore[len(self.optimalStore)-checkLens:]

        if lastValue == lastValue[::-1]:
            self.isEnd = True


    @property
    def state(self):
        pass

    @property
    def presentState(self):
        """当前位置"""
        return self.curPos

    def printOptimalValue(self):
        """打印最佳值"""
        logger.info(self.optimalValue)
    


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
            action.append(self.q[i][state[i], :].argmax())

        return action


def epsilonGreedy(Q, state):
    """e-贪心算法"""
    if (np.random.uniform() > 1 - EPSILON) or ((Q.getCurOptAction(state) == 0).all()):
        action = [np.random.randint(-1, 1) for i in range(Q.dim)]
    else:
        action = Q.getCurOptAction(state)

    return action

def main():
    dim = 5
    lowBoundary = [-300, -300, -300, -300, -200]
    upBoundary = [300, 300, 100, 300, 200]
    modelName = getModelName()[0]
    modelPath = modelPathFormat.format(modelName)   # quadraticRegression
    agent = io.getData(modelPath)   # 代理模型
    Q = QClass(dim, lowBoundary, upBoundary)
    maxIter = 50
    initPos = None
    logger.info("using model: {}".format(modelName))
    for it in range(maxIter):
        logger.info("iter: {}".format(it))
        e = Env(agent, dim, lowBoundary, upBoundary)
        action = epsilonGreedy(Q, e.presentState)
        while (e.isEnd is False) and (e.step < MAX_STEP):
            reward = e.interact(action) # 计算当前动作的奖赏
            newState = e.presentState
            newAction = epsilonGreedy(Q, newState)
            Q.updateStateAndAction(state, action, newState, newAction, reward)
            action = newAction
            e.printOptimalValue()

if __name__ == '__main__':
    main()
