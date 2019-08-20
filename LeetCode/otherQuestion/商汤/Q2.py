# coding:utf-8
# 2019-8-19

def solver(s, maps):
    """字符串s, 字典maps"""
    queue = [0]
    visit = []
    lenS = len(s)
    lensDict = [len(x) for x in maps]
    while queue:
        curIndex = queue.pop()
        for i, l in enumerate(lensDict):
            curLens = l + curIndex
            if curLens in visit:
                continue

            if s[curIndex:curLens] == maps[i]:
                if curLens == lenS:
                    return "true"
                queue.append(curLens)
                visit.append(curLens)
    # print(visit)
    return "false"

def test():
    s = "applepenapple"
    maps =  ["apple","pen"]
    ret = solver(s, maps)
    print(ret)

if __name__ == '__main__':
    test()

