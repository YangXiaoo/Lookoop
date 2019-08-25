# coding:utf-8
"""
给定图(全连通图,无环)，确定好序列
好序列定义
1. 能从a1走到ak
2. 从a1走到ak要走最短路
3. 走的路中至少包含一条黑边
输入：
4 4
1 2 1
2 3 1
3 4 1

输出：
252
"""
import sys

# 未解决
def solver(n, k, maps):
    """
    n 树的节点数
    k 序列的长度
    maps[[]] [u v w] 树节点u和v之间有一条边，边的颜色为w(0红色，1黑色)
    """
    candidates = getCandidates(n, k)
    edges = getEdges(maps)
    print(edges)
    ret = []
    record = {}
    for can in candidates:
        for i in range(len(can)-1):
            if can[i] != can[i+1]:
                key = "".join(map(str, can[i:i+1]))
                if key in record:
                    r = record[key]
                    if r:
                        ret.append(can)
                        break
                else:
                    record[key] = False
                curRoad = getRoad(can[i], can[i+1], edges)
                if hasBlankEdge(curRoad, maps):
                    record[key] = True
                    ret.append(can)
                    break

    return len(ret)

def hasBlankEdge(road, maps):
    for i in range(len(road)-1):
        cur = [road[i], road[i+1]]
        cur.sort()
        for m in maps:
            u, v, w = m 
            edge = [u, v]
            edge.sort()
            if edge == cur:
                if w == 1:
                    return True

    return False

def getCandidates(n, k):
    def dfs(tmp):
        nonlocal n, k, ret
        if len(tmp) == k:
            ret.append(tmp[:])
        else:
            for i in range(1, n+1):
                tmp.append(i)
                dfs(tmp)
                tmp.pop()

    ret = []
    dfs([])

    return ret 

def getRoad(u, v, edges):
    """获得路径"""
    nodes = edges[u]
    nextNodes = []
    for n in nodes:
        nextNodes.append([u, n])

    while True:
        for i, node in enumerate(nextNodes):
            if node[-1] == v:
                return node 
            else:
                nodes = edges[node[-1]]
                for n in nodes:
                    if node[-1] != n:
                        node.append(n)
            print(node)

def getEdges(maps):
    edges = {}
    for nodes in maps:
        _u, _v, _w = nodes
        if _u not in edges:
            edges[_u] = []
        edges[_u].append(_v)

        if _v not in edges:
            edges[_v] = []
        edges[_v].append(_u)
    return edges

def test():
    n, k = 4, 4
    maps = [[1,2,1],
            [2,3,1],
            [3,4,1]]

    ret = solver(n, k, maps)
    print(len(ret))

def inputs():
    n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
    for i in range(n-1):
        cur = list(map(int, sys.stdin.readline().strip().split(" ")))
        maps.append(cur)

    ret = solver(n, k, maps)
    print(ret)
if __name__ == '__main__':
    test()