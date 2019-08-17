# coding:utf-8
import sys

class Node():
    def __init__(self, start, end):
        self.start = start
        self.end = end

def solver(nodes):
    lens = len(nodes)
    nodes.sort()
    print(nodes)
    team = []
    ret = []
    maxLens = 0
    for n in nodes:
        team.append(Node(n[0], n[1]))
        maxLens = max(maxLens, n[1])

    ret.append(team[0])
    for i in range(1, lens):
        curNode = team[i]
        if curNode.start > ret[-1].end:
            return -1
        while curNode.end >= ret[-1].end:
            printRet(ret)
            # print(curNode.start)
            if curNode.start <= ret[-1].start or findPre(ret, curNode):
                if ret[-1].start != 0:
                    ret.pop()
                else:
                    break
            else:
                break
        if curNode.end > ret[-1].end:
            ret.append(curNode)
    if ret[-1].end == maxLens:
        printRet(ret)
        return len(ret)

    return -1

def findPre(ret, curNode):
    for i, n in enumerate(ret):
        if n.end >= curNode.start:
            print(n.end)
            return True

    return False

def printRet(ret):
    node = []
    for r in ret:
        node.append([r.start, r.end])

    print(node)
def test():
    nodes = [[4, 6],
            [3, 6], 
            [2, 4],
            [0, 2],
            [4, 7]]

    ret = solver(nodes)

    print(ret)

if __name__ == '__main__':
    test()