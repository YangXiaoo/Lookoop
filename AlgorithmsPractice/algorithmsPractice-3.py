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

# testRemoveString()
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
输入1: 节点数，节点按照字母顺序编号 8
输入2：字符串表示，可达节点间耗时 a->b:4,b->h:1,b->e:2,e->d:1,h->g:1,h->c:2,g->f:2,g->c:5,f->c:2,c->d:1
输入3: 当前访客位置 a
输入4: 访客目的地 d
输出：最短耗时，如果没有字母串为None abed
"""
def minCostPath(pointCount, path, startP, endP):
    edges = initPath(pointCount, path)
    print("edges: {}".format(edges))
    # startP, endP = ord(startP) - ord('a'), ord(endP) - ord('a')
    # print("startP: {}, endP: {}".format(startP, endP))
    minCost, minPath = 0, []

    def helper(curS, curCost, curPath):
        """辅助函数，递归查找"""
        nonlocal minCost, minPath, edges
        if curS == endP:
            if minCost == 0 or curCost < minCost:
                minCost = curCost
                minPath = curPath[::]
        else:
            # print("curS: {}, curCost: {}, curPath: {}".format(curS, curCost, curPath))
            for pIndex, c in enumerate(edges[curS]):
                if c != 0:
                    curPath.append(chr(pIndex + ord('a')))
                    curCost += c
                    helper(pIndex, curCost, curPath)
                    curCost -= c
                    curPath.pop()

    helper(startP, 0, [chr(startP + ord('a'))])

    if minCost != 0:
        return "".join(minPath)

    return None 


def initPath(pointCount, path):
    pathNums = path.split(',')
    edges = [[0 for _ in range(pointCount)] for _ in range(pointCount)]
    for p in pathNums:
        pStart, pEnd, cost = ord(p[0]) - ord('a'), ord(p[3]) - ord('a'), int(p[-1])
        edges[pStart][pEnd] = cost

    return edges

def testMinCostPath():
    pointCount = 8
    path = "a->b:4,b->h:1,b->e:2,e->d:1,h->g:1,h->c:2,g->f:2,g->c:5,f->c:2,c->d:1"
    startP = 'a'
    endP = 'd'
    tmp = minCostPath(pointCount, path, startP, endP)
    print(tmp)

# testMinCostPath()
#############################################################################
"""结对编程
根据人员合作情况，判断重新结对是否能够让所有结对的成员曾经有合作经验
输入1: 结对对数 2
输入2：结对情况 tom:jim, mike:mini
输入3：有合作经验的对数数量 2
输入4：有合作经验的人员对应情况 mike:jim, tom:mini
输出： 能否重新结对，1是，0否  1
"""
def newPair(pairCount, pair, copCount, cop):
    edges = initPair(cop)
    peoples = getPeople(pair)
    finalCop = []

    for p in peoples:
        if p in edges:
            finalCop.append(p)

    print(finalCop)
    return len(finalCop) == pairCount

def getPeople(pair):
    pairNums = pair.split(",")
    peoples = []
    for p in pairNums:
        cop = p.split(":")
        peoples.append(cop[0])
        peoples.append(cop[1])

    return peoples

def initPair(pair):
    pairNums = pair.split(",")
    edges = {}
    for p in pairNums:
        cop = p.split(":")
        edges[cop[0]] = cop[1]
        edges[cop[1]] = cop[0]

    return edges

def test_newPair():
    pairCount, pair, copCount, cop = 2, "tom:jim,mike:mini", 2, "mike:jim,tom:mini"

    ret = newPair(pairCount, pair, copCount, cop)
    print(ret)


test_newPair()
