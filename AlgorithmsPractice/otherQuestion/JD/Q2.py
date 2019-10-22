# coding:utf-8
"""
某校在积极推行无人监考制度，但是总有学生是不自觉的，如果将两个很熟的异性朋友放在同一个考场里，他们就会交流甚至作弊。因此一个考场中不能允许两个很熟的异性朋友存在，学校希望通过搬出一部分学生的方法来改善这一问题。

但是又因为教室数量有限，因此希望一个教室中容下的学生尽可能多，即需要搬出教室的学生数量尽可能少，请你输出搬出教室人数最少，且字典序最小的方案。

输入
  输入第一行有两个整数n和m，分别表示有n个男生和n个女生，有m个朋友关系。

(1<=n<=500,1<=m<=100000)

  接下来m行，每行有两个整数，x和y，表示第x号男生和第y号女生是朋友。男生的编号均为[1,n]，女生的编号为[n+1,2n]。

输出
输出第一行包含一个整数a，表示最少需要搬出教室的人数。

输出第二行有a个整数，即a个需要搬出教室的人的编号，要求人数最少，且字典序最小。

样例输入
2 2
1 3
1 4
样例输出
1
1
"""
import sys
# AC 36%
def solver(n, relations):
    """n表示有n个男生和n个女生，relations表示朋友关系"""
    # 生成朋友关系图
    friends = {}
    for relation in relations:
        for s in relation:
            friends[s] = []
    for nums in relations:
        if nums[0] != nums[1]:
            friends[nums[0]].append(nums[1])
            friends[nums[1]].append(nums[0])

    ret = []
    while True:
        rela = getMaxOutdegree(friends) # 获得最多朋友的学生编号, 朋友数大于0
        if rela == -1:
            break

        ret.append(rela)
        deleteNode(friends, rela)   # 删除朋友关系

    ret.sort()

    return ret 

def getMaxOutdegree(friends):
    """获得朋友数最多的学生编号
    @returns -1 未找到
    """
    # 根据字典排序
    keys = sorted(friends.keys())
    maxCount = 0
    retS = -1
    for s in keys:
        if len(friends[s]) > maxCount:
            maxCount = len(friends[s])
            retS = s 

    return retS

def deleteNode(friends, rela):
    """删除朋友关系"""
    for k,v in friends.items():
        if rela in v:
            index = v.index(rela)
            v.pop(index)
    friends[rela] = []  # 还需要删除当前朋友最多学生编号的关系

def printRet(ret):
    print(len(ret))
    if len(ret) == 0:
        print(0)
    for n in ret:
        print(n)

def test():
    n = 2
    relations = [[1,3],
                 [1, 4]]
    ret = solver(n, relations)
    printRet(ret)

def inputs():
    lines = input()
    nums = list(map(int, lines.split(" ")))
    relations = []
    for i in range(nums[1]):
        cur = list(map(int, input().split(" ")))
        relations.append(cur)
    ret = solver(nums[0], relations)
    printRet(ret)


if __name__ == '__main__':
    test()