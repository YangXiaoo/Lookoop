# coding:utf-8

"""
在中国有N座城市和M条无向道路,第i条道路连接Ai和Bi，长度为Ci。 马可波罗想要在中国访问R座城市(r1,r2...rR)(不一定按照这个顺序)。 他可以制定一条旅行路线，这条路线一定要包括这R座城市。 现在问如何制定这条旅行路线，使得经过的总长度最小？

提示：输入样例效果如图所示



输入
N M R r1 r2 ... rR A1 B1 C1 A2 B2 C2 ....... AM BM CM 其中2<=N<=200, 1<=M<=5000, 2<=R<=min(22,N), Ci<=10000 保证无重边。

输出
输出一行表示旅行路线最小的长度。


样例输入
4 6 3
2 3 4
1 2 4
2 3 3
4 3 1
1 4 1
4 2 2
3 1 6
样例输出
3
"""

def solver(n, m, st, maps):
    """
    n : N座城市
    m : m条路
    st : 需要访问的城市[1, 3, 4]
    maps: 城市之间的距离
    """
    r = len(st)
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
        if ea > eb:
            ea, eb = eb, ea
        v = str(ea) + str(eb)
        vertex[v] = l

    def dfs(tmp, curRoot):
        """dfs遍历获得指定长度的路径"""
        nonlocal road, r, edge
        if len(tmp) >= r:
            t = sorted(tmp)
            count = 0
            for n in st:
                if n in tmp:
                    count += 1
            if count == len(st):
                road.append(tmp)
        else:
            if curRoot in edge:
                for n in edge[curRoot]:
                    if n not in tmp:
                        tmp.append(n)
                        dfs(tmp, n)
                        tmp.pop()
    
    road = []
    for r in st:
        dfs([r], r)

    ret = {}
    for r in road:
        lens = getLength(r, vertex)
        if lens not in ret:
            ret[lens] = []

        ret[lens].append(r[:])

    s = sorted(ret.keys())[0]

    return s

def getLength(r, vertex):
    ret = 0
    for i in range(len(r) -1):
        pre, next = r[i], r[i+1]
        ret += vertex.get(str(pre)+str(next), 0)

    return ret

def test():
    n, m, st = 4, 6, [2,3,4]
    maps = [[1, 2, 4],
            [2, 3, 3],
            [4, 3, 1],
            [1, 4, 1],
            [4, 2, 2],
            [3, 1, 6]]

    ret = solver(n,m,st, maps)

    print(ret)


def inputs():
    n, m, r = list(map(int, input().strip().split()))
    st = list(map(int, input().strip().split()))
    maps = []
    for i in range(m):
        cur = list(map(int, input().strip().split()))
        maps.append(cur)

    ret = solver(n, m, st, maps)

    print(ret)

if __name__ == '__main__':
    test()

