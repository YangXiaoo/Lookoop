# coding:utf-8
# 2020-11-09

# 2020-11-09
"""外协分配 
输入1： 各小组资源需求 [1, 5, 3, 9, 6]
输入2 : 各外协生产效率 [1,3,1,2,7,7]
输出: 能够满足需求的小组数量 4
"""
def quatifyTeam(need, efficent):
    need.sort()
    efficent.sort()
    qutifyNum = 0
    startIndex = 0

    for n in need:
        tmpIndex = startIndex
        for e in efficent[startIndex: ]:
            tmpIndex += 1
            if e >= n:
                qutifyNum += 1
                print("将外协: {} 分配给小组 {}".format(e, n))
                break

        startIndex = tmpIndex

    return qutifyNum

def testQuatifyTeam():
    need = [1, 5, 3, 9, 6]
    efficent = [1,3,1,2,7,7]

    ret = quatifyTeam(need, efficent)
    print("quatifyTeam: {}".format(ret))

# testQuatifyTeam()
#############################################################################
"""裁纸游戏
给定一个长方形的长和宽，将其裁剪为一个或多个正方形，且不能有纸张浪费，返回裁剪的正方形的最大变长.(求最大公约数)
"""
def maxSquareSize(length, width):
    maxSize = 1
    for size in range(2, min(length, width)):
        if length % size == 0 and width % size == 0:
            maxSize = max(size, maxSize)

    return maxSize

def gcd(a, b):
    """最大公约数辗转相除法"""
    if a < b:
        a, b = b, a
    x = a % b 
    while x != 0:
        x = a % b 
        a = b 
        b = x

    return a

def testMaxSquareSize():
    length, width = 15, 21

    # ret = maxSquareSize(length, width)
    ret = gcd(length, width)

    print("最大边长为: {}".format(ret))

# testMaxSquareSize()
#############################################################################
"""消消乐
相同字符长度达到消除长度可消除，返回消除后的字符串
输入: aabbbeccceeffaccfcaa (字符串)
输入: 20 (字符串长度)
输入: 3 (可消除长度)
输出: aaffaccfcaa
"""
def removeString(string, removeLen):
    if not string or removeLen == 0:
        return ""

    preChar, curLen = string[0], 0
    stack = []
    for c in string:
        stack.append(c)
        if preChar == c:
            curLen += 1
        else:
            preChar = c 
            curLen = 1
        if curLen == removeLen:
            removeStack(stack, removeLen)

            # 计算前置重复
            curLen, preChar = 1, stack[-1]
            while curLen < len(stack) and preChar == stack[len(stack) - curLen - 1]:
                curLen += 1

    return "".join(stack)

def removeStack(stack, length):
    while length > 0:
        stack.pop()
        length -= 1

def testRemoveString():
    string, removeLen = "aabbbeccceeffaccfcaa", 3

    ret = removeString(string, removeLen)
    print("消除后的字符串为: {}".format(ret))

testRemoveString()
#############################################################################
"""申请开发测试资源
输入1: 需要使用资源的日期数组 [1,4,6,7,8,20]
输入2: 天数 6
输入3: 连续使用1天，1周，1个月的成本数组 [4,14,30]
输入4: 可申请的方式种类数 3
输出: 最小资源使用成本 22 ; 输入异常返回-1   
"""
def minCostApply(applyDate, dateCount, cost, costTypeCount):
    """最小使用资源
    @param applyDate 日期数组
    @param dateCount 天数
    @param cost 使用成本
    @param costTypeCount 可申请方式种类 

    @return int
    """
    def helper(startIndex, curCost):
        nonlocal applyDate, cost, minCost
        if startIndex == len(applyDate):
            # print("[debug] curCost: {}".format(curCost))
            minCost = min(minCost, curCost)
        else:
            for i, c in enumerate(cost):
                curCost += c
                curEndDay = applyDate[startIndex] + getDay(i) 
                preIndex = startIndex
                while startIndex < len(applyDate):
                    if applyDate[startIndex] >= curEndDay:
                        break
                    startIndex += 1
                helper(startIndex, curCost)
                curCost -= c
                startIndex = preIndex


    # 检测异常
    if len(applyDate) != dateCount or len(cost) != costTypeCount:
        return -1

    minCost = 30 * 12
    helper(0, 0)

    return minCost

def getDay(costIndex):
    """根据使用成本的数组获取天数"""
    return [1, 7, 30][costIndex]

def testMinCostApply():
    applyDate = [1,4,6,7,8,20]
    dateCount = 6
    cost = [4,14,30]
    costTypeCount = 3

    ret = minCostApply(applyDate, dateCount, cost, costTypeCount)
    print(ret)

# testMinCostApply()
#############################################################################
"""成研访客

