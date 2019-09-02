# coding:utf-8
"""n个景点, m条路，求经过所有景点的非重复路径长度"""

import sys
import copy 

def solver(n, m, maps):
    """
    maps: 图表示
    """
    # 边集
    edge = {}
    for m in maps:
        ea, eb, l = m 
        if ea not in edge:
            edge[ea] = []
        edge[ea].append(eb)

        if eb not in edge:
            edge[eb] = []
        edge[eb].append(ea)
    # print(edge)

    # 点之间的距离
    vertex = {}
    for m in maps:
        ea, eb, l = m 
        v = str(ea) + str(eb)
        vertex[v] = l


    # print(vertex)
    def dfs(tmp, curRoot, pro):
        """dfs遍历获得指定长度的路径"""
        nonlocal road, edge
        if len(tmp) != 0:
            cur = road.get(pro, [])
            t = copy.deepcopy(tmp)
            t.sort()
            if t not in cur:
                cur.append(t[:])

        if curRoot in edge:
            for r in edge[curRoot]:
                if r not in tmp:
                    nextP = getNext(tmp, r)
                    tmp.append(r)
                    dfs(tmp, r, pro*nextP)
                    tmp.pop()

    def getNext(tmp, r):
        nonlocal edge
        pro = 1
        last = tmp[-1]
        lenE = len(edge[last])

        if len(tmp) > 2:
            if tmp[-2] in edge[last]:
                pro = 1/ (lenE - 1)

        return pro

    road = {}
    for s in edge.keys():
        curP = 1/len(edge[s]) * (1/n)
        dfs([s], s, curP)  # 从1开始寻找

    ret = 0
    for k,v in road.items():
        for r in v:
            ret += k * getLength(r, vertex)


    return ret

def getLength(r, vertex):
    ret = 0
    for i in range(len(r) -1):
        pre, next = r[i], r[i+1]
        ret += vertex.get(str(pre)+str(next), 0)

    return ret

def test():
    n, m = 4, 3
    maps = [[1,2,3],
            [2,3,1],
            [3,4,4]]
    ret = solver(n, m, maps)

    print(ret)


def inputs():
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split(" ")))

    maps = []
    for i in range(m):
        cur = list(map(int, sys.stdin.readline().strip().split(" ")))
        maps.append(cur)

    ret = solver(n, m, maps)
    print(ret)

if __name__ == '__main__':
    inputs()