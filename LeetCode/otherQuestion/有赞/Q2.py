# coding:utf-8
"""给定n,m,k表示n个点，m条边，经过k个点；求k个点最长路径为多长，且有多各个"""
import sys

def solver(n, m, k, maps):
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
    def dfs(tmp, curRoot):
        """dfs遍历获得指定长度的路径"""
        nonlocal road, k, edge
        if len(tmp) == k:
            road.append(tmp[:])
        else:
            if curRoot in edge:
                for n in edge[curRoot]:
                    if n not in tmp:
                        tmp.append(n)
                        dfs(tmp, n)
                        tmp.pop()


    road = []
    dfs([1], 1)  # 从1开始寻找
    if len(road) == 0:
        return 0, 0

    # print(road)
    ret = {}
    for r in road:
        lens = getLength(r, vertex)
        if lens not in ret:
            ret[lens] = []

        ret[lens].append(r[:])

    s = sorted(ret.keys())[0]

    retRoad = ret[s]

    return str(s) + str(len(retRoad))


def getLength(r, vertex):
    ret = 0
    for i in range(len(r) -1):
        pre, next = r[i], r[i+1]
        ret += vertex.get(str(pre)+str(next), 0)

    return ret

def test():
    n, m, k = 6, 6, 4
    maps = [[1,2,1],
            [2,3,1],
            [3,4,1],
            [2,5,1],
            [3,6,1],
            [5,6,1]]
    length, dup = solver(n, m, k, maps)
    print(str(length) + " " + str(dup))

def inputs():
    line = sys.stdin.readline().strip()
    n, m, k = list(map(int, line.split(" ")))

    maps = []
    for i in range(m):
        cur = list(map(int, sys.stdin.readline().strip().split(" ")))
        maps.append(cur)

    ret = solver(n, m, k, maps)
    print(ret)


if __name__ == '__main__':
    test()