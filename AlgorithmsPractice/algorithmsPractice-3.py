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
                print("将外协 {} 分配给小组 {}".format(e, n))
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

def removeString2(string, removeLen):
    """骚操作 直接使用字符串替换"""
    alphaNums = []
    for c in string:
        if c not in alphaNums:
            alphaNums.append(c)

    while True:
        preLength = len(string)
        for c in alphaNums:
            replaceStr = c * removeLen
            string = string.replace(replaceStr, '')
        if preLength == len(string):
            break

    return string


def removeStack(stack, length):
    while length > 0:
        stack.pop()
        length -= 1

def testRemoveString():
    string, removeLen = "aabbbeccceeffaccfcaa", 3

    ret = removeString2(string, removeLen)
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
    startP, endP = ord(startP) - ord('a'), ord(endP) - ord('a')
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
            print("curS: {}, curCost: {}, curPath: {}".format(curS, curCost, curPath))
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
# 2020-11-10
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
    """分割字符串获得人员"""
    pairNums = pair.split(",")
    peoples = []
    for p in pairNums:
        cop = p.split(":")
        peoples.append(cop[0])
        peoples.append(cop[1])

    return peoples

def initPair(pair):
    """分割字符串获得配对信息"""
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


# test_newPair()
#############################################################################
"""8.碰碰乐游戏
给定一数组表示方块，正负表示运动方向（负数向左，正数向右），求最终剩余方块
输入1： 初始方块 [5,10,2,-5]
输出：剩余方块 [5,10]
"""
def crashGame(block):
    if len(block) < 2:      # 特殊判断
        return block
    stack = []
    for b in block:
        stack.append(b)
        if b < 0:
            while len(stack) > 1:
                if stack[-2] < 0:                       # 倒数第二个为负数，退出循环
                    break
                else:                                   # 最后一个为负数，倒数第二个为正数
                    if stack[-1] + stack[-2] < 0:       # 正数被抵消
                        stack.pop(len(stack) - 2)
                    elif stack[-1] + stack[-2] > 0:     # 负数被抵消, 直接退出循环
                        stack.pop()
                        break
                    elif stack[-1] + stack[-2] == 0:    # 最后两个数可以直接抵消，抵消后退出循环
                        stack.pop()
                        stack.pop()
                        break
    return [stack, None][len(stack) == 0]

def test_crashGame():
    blocks = [[5,10,2,-5], [6,-6]]

    for block in blocks:
        ret = crashGame(block)
        print(ret)

# test_crashGame()
#############################################################################
"""健康打卡人员塞选
输入： 筛选条件 J="aA", 员工办公状态打卡 S="aAAbbb"
输出： 3 三名满足"aAA"
"""
def selectPeople(J, S):
    jNums =[j for j in J]
    match = []
    
    for s in S:
        if s in jNums:
            match.append(s)

    return len(match)

def test_selectPeople():
    J, S = "aA", "aAAbbb"

    ret = selectPeople(J, S)
    print(ret)

# test_selectPeople()
#############################################################################
"""到岗人数增长统计
记录多少天后人数会超过当天人数
输入：记录到岗人员数量的数组 [66,65,67,65]
输入2: 记录的天数 4
输出：字符串 2,1,0,0
"""
def employeeStatistic(employees, dayNum):
    """暴力破解"""
    if len(employees) == 1:
        return [0]

    ret = []
    for i, n in enumerate(employees):
        tmpRes = 0
        for j in range(i + 1, len(employees)):
            if employees[j] > n:
                tmpRes = j - i
                break

        ret.append(tmpRes)

    return ret 

def test_employeeStatistic():
    employees, dayNum = [66,65,67,65], 4

    ret = employeeStatistic(employees, dayNum)
    print(ret)

# test_employeeStatistic()
#############################################################################
"""更新应急预案
编写程序比较两个版本号，V1>V2返回1，V1<V2返回-1，相等返回0，异常返回-100
输入1：V1 "7.5.2.4"
输入2：V2 "7.5.3"
输出：-1
"""
def compareVersion(v1, v2):
    # 检查字符
    v1 = v1.split('.')
    v2 = v2.split('.')

    maxLen = max(len(v1), len(v2))

    for i in range(len(v1), maxLen):
        v1.append('0')
    for i in range(len(v2), maxLen):
        v2.append('0')

    # print("[DEBUG] v1: {}, v2: {}".format(v1, v2))
    ret = 0
    for i in range(maxLen):
        va = int(v1[i])
        vb = int(v2[i])
        if va > vb:
            ret = 1
            break
        elif va < vb:
            ret = -1
            break

    return ret 

def test_compareVersion():
    v = [
            ["7.5.2.4", "7.5.3"],   # -1
            ["0.1", "1.1"],         # -1
            ["1.01", "1.001"],      # 0
            ["1.0", "1.0.0"]        # 0
        ]
    for v1, v2 in v:
        ret = compareVersion(v1, v2)
        print(ret)

# test_compareVersion()
#############################################################################
"""12-用餐安全距离
给定座位情况（至少有一个0且至少有一个1），1代表有人坐座位上，0代表座位为空，选择一个空座位来坐，使得这个作为离最近的人的距离最大
输入1：座位情况 [1,0,0,0,0,1,0,1]
输入2：座位数量 7
输出：最大距离，异常返回-1  2
"""
def maxSeatGap(seats, seatsCount):
    if len(seats) != seatsCount or seatsCount < 2:
        return -1

    gap = [-1 for _ in range(seatsCount)]
    for i in range(seatsCount):
        if seats[i] != 1:
            left, right = i - 1, i + 1
            leftGap, rightGap = 1, 1
            while left >= 0:
                if seats[left] == 0:
                    leftGap += 1
                else:
                    break

                left -= 1
            while right < seatsCount:
                if seats[right] == 0:
                    rightGap += 1
                else:
                    break
                right += 1
            if left == -1 and leftGap < rightGap:               # 抵达左边界，左边距离小于右边距离时计算右边距离
                gap[i] = rightGap
            elif right == seatsCount and rightGap < leftGap:
                gap[i] = leftGap
            elif left != -1 and right != rightGap:              # 左右都没有抵达边界，则计算最小距离
                gap[i] = min(rightGap, leftGap)

    # print(gap)
    return max(gap)

def test_maxSeatGap():
    inputValue = [
        [[1,0,0,0,1,0,1], 7],   # 2
        [[1,0,0,0], 4]          # 3
    ]

    for seats, seatsCount in inputValue:
        ret = maxSeatGap(seats, seatsCount)
        print(ret)

# test_maxSeatGap()
#############################################################################
"""13-参会人员
给出多个会议的开始结束时间，保证所有会议都有项目组人员参加，至少需要安排多少人参会
输入1：会议开始时间数组 [0,5,15]
输入2：会议结束时间数组 [23,10,20]
输入3：会议数量 3
输出：至少需要安排的人数 2
"""
import functools
def meetingArrangement(s, t, meetingCount):
    """合并数组，不能合并的数组数量减1"""
    arragement = [[startTime, endTime] for (startTime, endTime) in zip(s, t)]
    arragement = sorted(arragement)
    print(arragement)
    ret = 1
    for i in range(1, len(arragement)):
        cur = arragement[i]
        pre = arragement[i-1]
        if cur[0] > pre[0] and cur[1] <= pre[1]:    # 能够合并
            pass
        else:
            ret += 1
    return meetingCount - ret + 1


def test_meetingArrangement():
    inputValue = [
        [[0,5,15], [23,10,20], 3],      # 2
        [[7,2], [10, 4], 2],             # 1
        [[1,2,4,5,6], [2,4,5,6,7], 5]   # 1
        ]

    for s, t, meetingCount in inputValue:
        ret = meetingArrangement(s, t, meetingCount)
        print(ret)

# test_meetingArrangement()
#############################################################################
"""14-项目任务分配优化
确定是否能将功能模块平均分配
输入1：各功能模块的工作量数组 [4,3,1,2,3,5,1,1,1,4]
输入2：模块数量 10
输入3：各项目组人数 5
输出：能否达到最佳项目进度，1是，0否，-1表示参数不合法。  1
"""
def assigningTask(workload, moduleCount, staffCount):
    totalWorkload = sum(workload)

    if totalWorkload % staffCount != 0:
        return 0

    avgerageWorkload = totalWorkload // staffCount
    # print("avgerageWorkload: {}".format(avgerageWorkload))
    visited = [False for _ in workload]
    def helper(visited, startIndex, curSum, k):
        nonlocal workload
        if k == 0: return True
        if curSum == avgerageWorkload: 
            return helper(visited, 0, 0, k - 1)
        for i in range(startIndex, len(workload)):
            if visited[i]:
                continue
            visited[i] = True
            if helper(visited, i + 1, curSum + workload[i], k):
                return True
            visited[i] = False

        return False

    return [0, 1][helper(visited, 0, 0, avgerageWorkload)]


def test_assigningTask():
    inputValue = [
        [[4,3,1,2,3,5,1,1,1,4], 10, 5],
        [[4,3,1,2,3,5,1,1,1,4,12], 11, 5],
        [[3,2,4,2,3,3,3], 7, 5],
    ]
    for workload, moduleCount, staffCount in inputValue:
        ret = assigningTask(workload, moduleCount, staffCount)
        print(ret)

test_assigningTask()