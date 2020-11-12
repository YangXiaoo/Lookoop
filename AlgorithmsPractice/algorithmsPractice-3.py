# coding:utf-8
# 2020-11-09

# 2020-11-09
"""2-外协分配 
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
"""3-裁纸游戏
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
"""4-消消乐
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
"""5-申请开发测试资源
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
"""6-成研访客
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
    print("startP: {}, endP: {}".format(startP, endP))
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
"""7-结对编程 
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
"""8-碰碰乐游戏
给定一数组表示方块，正负表示运动方向（负数向左，正数向右），求最终剩余方块
输入1： 初始方块 [5,10,2,-5]
输出：剩余方块 [5,10]
"""
def crashGameHandler(block):
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
                    blockSum = stack[-1] + stack[-2]
                    if blockSum < 0:                    # 正数被抵消
                        stack.pop(len(stack) - 2)
                    elif blockSum > 0:                  # 负数被抵消, 直接退出循环
                        stack.pop()
                        break
                    elif blockSum == 0:                 # 最后两个数可以直接抵消，抵消后退出循环
                        stack.pop()
                        stack.pop()
                        break

    return stack 

def crashGame(block):
    """左右边界不相接"""
    stack = crashGameHandler(block)
    return [stack, None][len(stack) == 0]

def crashGame2(block):
    """考虑左右链接成环"""
    handledBlock = crashGameHandler(block)
    while True:
        preLength = len(handledBlock)
        if preLength < 2:
            break
        # 只有左边界块往左（负值），右边界块往右（正值）才会合并
        if handledBlock[0] < 0 and handledBlock[-1] > 0:
            blockSum = handledBlock[0] + handledBlock[-1]
            if  blockSum == 0:                  # 左右抵消
                handledBlock.pop(0)
                handledBlock.pop()
            elif blockSum > 0:                  # 负值被抵消
                handledBlock.pop(0)
            else:                               # 正值被抵消
                handledBlock.pop()

        if preLength == len(handledBlock): break

    return [handledBlock, None][len(handledBlock) == 0]


def test_crashGame():
    blocks = [[5,10,2,-5], [6,-6], [-6, -4, -3, 3, 4, 6]]

    for block in blocks:
        ret = crashGame2(block)
        print(ret)

# test_crashGame()
#############################################################################
"""9-健康打卡人员塞选
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
"""10-到岗人数增长统计
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
def employeeStatistic2(employees, dayNum):
    ret = [0 for _ in employees]
    stack = []

    for i in range(dayNum):
        curPeopleCount = employees[i]
        while stack and curPeopleCount > employees[stack[-1]]:
            preIndex = stack.pop()
            ret[preIndex] = i - preIndex
        stack.append(i)

    return ret

def test_employeeStatistic():
    inputValue = [
        [[66,65,67,65], 4],         # [2, 1, 0, 0]
        [[1, 5, 4, 3, 4, 6], 6],    # [1, 4, 3, 1, 1, 0]
    ]
     
    for employees, dayNum in inputValue:
        ret = employeeStatistic2(employees, dayNum)
        print(ret)

    print("------------------")

test_employeeStatistic()
#############################################################################
"""11-更新应急预案
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
    inputValue = [
            ["7.5.2.4", "7.5.3"],   # -1
            ["0.1", "1.1"],         # -1
            ["1.01", "1.001"],      # 0
            ["1.0", "1.0.0"]        # 0
        ]
    for v1, v2 in inputValue:
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

# test_assigningTask()
#############################################################################
"""15-数据库备库情况
排查出第一个没有备份数据库的系统，返回索引，如果不存在返回-1.
输入：aabcc
输出：2
"""
def checkBackup(databseNums):
    database, backupInfo = [], {}
    for d in databseNums:
        if d not in database:
            database.append(d)
        backupInfo[d] = backupInfo.get(d, 0) + 1

    for i, d in enumerate(databseNums):
        if backupInfo[d] == 1:
            return i 

    return -1

def test_checkBackup():
    databseNums = "aabcc"

    ret = checkBackup(databseNums)
    print(ret)

# test_checkBackup()
#############################################################################
"""16-办公用品采购
求需求量最大的前三种办公用品的总数
输入： p = [1,1,1,2,2,3,3,4,5]
输出：7
"""
def maxPurchase(p):
    officeInfo = {}
    for v in p:
        officeInfo[v] = officeInfo.get(v, 0) + 1

    needInfo = [v for (k, v) in officeInfo.items()]
    needInfo = sorted(needInfo, reverse=True)

    if len(needInfo) < 3:
        return sum(needInfo)
    else:
        return sum(needInfo[:3])

def test_maxPurchase():
    inputValue = [
        [1,1,1,2,2,3,3,4,5],    # 7
        [1,1,1,1,5],            # 5
        [1,1,2,2,3,4,5,6]       # 5
    ]

    for p in inputValue:
        ret = maxPurchase(p)
        print(ret)

# test_maxPurchase()
#############################################################################
"""17-代码格式检查
对括号进行判断，返回添加最少括号使得括号正确的括号数
输入：())
输出： 1
"""
def validParenthese(s):
    mapDict = {')': '('}

    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            curChange = mapDict[c]
            if len(stack) != 0 and stack[-1] == curChange:
                stack.pop()
            else:
                stack.append(c)

    return len(stack)

def test_validParenthese():
    inputValue = [
        "())",  # 1
        "(((",  # 3
        "()",   # 0
        "()))(("    # 4
    ]

    for s in inputValue:
        ret = validParenthese(s)
        print(ret)

# test_validParenthese()
#############################################################################
"""18-新员工分配任务
给定开发合集，找到不相邻的开发任务的最大工作量
"""
def maxWorkload(workload):
    dp = [0 for _ in workload]
    dp[0] = workload[0]
    dp[1] = workload[1]
    for i in range(2, len(workload)):
        dp[i] = max(dp[i - 1], workload[i] + dp[i - 2])

    # print(dp)
    return dp[-1]

def test_maxWorkload():
    inputValue = [
        [1,2,3,1],          # 4
        [2,7,9,3,1],        # 12
        [2,1,4,5,3,1,1,3],  # 12
    ]

    for workload in inputValue:
        ret = maxWorkload(workload)
        print(ret)

# test_maxWorkload()
#############################################################################
"""19-专利统计情况
给定保存员工信息的数据结构，包含唯一ID，发表专利数和直系下属的ID，多个下属用'&'分割，每条记录用'{}'包含。
返回员工和他下属的专利数量之和
输入：专利信息字符串，查找员工ID {1,5,[2&3]}{2,3,[]}{3,3,[]};1
输出：该员工辖内发表专利数 11

{1,5,[2&3]}: ,1号员工专利数为5，下属员工号为2,3
"""
def patentStatistics(s):
    userPatent, userRelation = {}, {}

    searchUserId = s.split(';')[-1]

    patentInfo = s.split(';')[0][1:-1].split('}{')
    print(patentInfo)
    for info in patentInfo:
        userId, patentCount, underlingInfo = info.split(',')
        userPatent[userId] = int(patentCount)
        underlingNums = underlingInfo[1:-1].split('&')
        # print("underlingNums: {}".format(underlingNums))
        userRelation[userId] = []
        for underling in underlingNums:
            if underling != '':
                userRelation[userId].append(underling)
    print(userPatent, userRelation)

    def helper(curUser):
        nonlocal patentCount, userRecord, userRelation, userPatent
        if curUser:
            patentCount += userPatent[curUser]
            for user in userRelation[curUser]:
                if user and user not in userRecord:
                    if userPatent[user]:
                        userRecord.append(user)
                        helper(user)

    patentCount = userPatent[searchUserId]
    userRecord = []
    for user in userRelation[searchUserId]:
        helper(user)

    return patentCount

def test_patentStatistics():
    inputValue = [
        "{1,5,[2&3]}{2,3,[]}{3,3,[]};1",
        "{1,5,[2]}{2,3,[3]}{3,4,[]};2"
    ]

    for s in inputValue:
        ret = patentStatistics(s)
        print(ret)

# test_patentStatistics()
#############################################################################
"""20-规范数字格式
给定一个整数N，每隔三位加一个英文逗号','作为千位符，处理后以字符串格式返回
输入：n=987
"""
def addThousandSeparator(n):
    n = str(n)
    stack, count = [], 0
    for c in n[::-1]:
        count += 1
        if count == 4:
            stack.append(',')
            count = 1
        stack.append(c)
        # print(stack)

    return "".join(stack[::-1])

def test_addThousandSeparator():
    inputValue = [
        987,            # 987
        1234,           # 1,234
        123456789,      # 123,456,789
        0,              # 0
        123456789900,   # 123,456,789,900
    ]

    for n in inputValue:
        ret = addThousandSeparator(n)
        print(ret)

# test_addThousandSeparator()
#############################################################################
"""21-制定考试目标分数
给定分数数组，返回第一个比自己高的分数, 没有比自己高的分数记为-1
输入：[70,75,60]
输出：[75,-1,-1]
"""
def setTargetScore(scores):
    record = [-1 for _ in scores]
    stack = []
    for i in range(len(scores)):
        curScore = scores[i]
        while stack and curScore > scores[stack[-1]]:
            preIndex = stack.pop()
            record[preIndex] = i
        stack.append(i)

    for i in range(len(record)):
        if record[i] != -1:
            record[i] = scores[record[i]]

    return record

def test_setTargetScore():
    inputValue = [
        [70,75,60],                 # [75, -1, -1]
        [70,80,72,85,94,63,70],     # [80, 85, 85, 94, -1, 70, -1]
    ]

    for scores in inputValue:
        print("------------------------")
        ret = setTargetScore(scores)
        print(ret)

# test_setTargetScore()
#############################################################################
"""外协完成模块数
每名中级可以开发medium个模块，每名高级可以完成high个模块，给定n名外协，计算能够完成功能数的可能情况。
输入：medium = 1, high = 2, num = 3
输出：[3,4,5,6]
"""
def computeCompleteModule(medium, high, num):
    ret = []
    users = [medium, high]
    def helper(curIndex, curUserCount, curModuleCount):
        if curUserCount == num:
            if curModuleCount not in ret:
                ret.append(curModuleCount)
        else:
            for i in range(len(users)):
                helper(i, curUserCount + 1, curModuleCount + users[i])

    helper(0, 0, 0)

    return ret 

def test_computeCompleteModule():
    inputValue = [
        [1,2,3],
    ]

    for medium, high, num in inputValue:
        ret = computeCompleteModule(medium, high, num)
        print(ret)

# test_computeCompleteModule()
#############################################################################
"""23-保证itable用户唯一
以最小整数重命名用户姓名
输入：name = ['a', 'b(1)', 'c(22)', 'b', 'c']
输出： ['a', 'b(1)', 'c(22)', 'b(2)', 'c']
"""
def renameUser(names):
    userNameRecord = {}
    repeatRecord = {}
    for i, name in enumerate(names):
        if name in userNameRecord:
            names[i] = "{}({})".format(name, userNameRecord[name] + 1)
            userNameRecord[name] = userNameRecord[name] + 1
        else:
            if name and name[-1] == ')':
                userName, suffix = name.split('(')[0], name[:-1].split('(')[-1]
                if userName in userNameRecord:                                              # 如果已经重复则
                    userNameRecord[userName] = max(userNameRecord[userName], int(suffix))   # 记录最大的版本号
                else:
                    userNameRecord[userName] = int(suffix)
            else:
                userNameRecord[name] = 0

    return names

def test_renameUser():
    inputValue = [
        ['a', 'b(1)', 'c(22)', 'b', 'c'],
        ['a', 'a(1)', 'a', 'c'],
        ['a(11)', 'a(1)', 'a', 'a'],
    ]

    for names in inputValue:
        ret = renameUser(names)
        print(ret)

# test_renameUser()
#############################################################################
"""24-批量节点调度
给定节点先后列表prerequisite和一个查询对列表queries,判断节点queires[i][0]是否必须在节点quires[i][1]之前调起，
如果是返回1，否则返回0
输入：n = 2, prerequisite=[[1,0]], quires=[[0,1],[1,0]]
输出：[0,1]
"""
def checkIsPrerequisite(n, prerequisite, quires):
    def helper(curNode, endNode):
        nonlocal edges, ret 
        if curNode == endNode:
            ret.append(1)
            return True
        else:
            for i, n in enumerate(edges[curNode]):
                if n != 0:
                    if helper(i, endNode): return True
        ret.append(0)

    edges = [[0 for _ in range(n)] for _ in range(n)]
    for nodes in prerequisite:
        edges[nodes[0]][nodes[1]] = 1

    ret = []
    for startNode, endNode in quires:
        helper(startNode, endNode)

    return ret

def test_checkIsPrerequisite():
    inputValue = [
        [2, [[1,0]], [[0,1],[1,0]]],        # [0,1]
        [3, [[1,0],[2,0]], [[0,1],[2,0]]],  # [0,1]
    ]

    for n, prerequisite, quires in inputValue:
        ret = checkIsPrerequisite(n, prerequisite, quires)
        print(ret)

# test_checkIsPrerequisite()