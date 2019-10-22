# coding=utf-8

"""
2
2 1 4 3
4
1 2 0 2
"""

def solver(n, init, m, nums):
    ret = []
    for i in nums:
        gap = 2**i
        init = reverseNum(init, gap)   # 每gap间隔翻转
        cur = computeReversePair(init)
        ret.append(cur)

    return ret 

def reverseNum(init, gap):
    ret = []
    for i in range(0, len(init), gap):
        c = init[i:i+gap][::-1]
        ret.extend(c)
    # print(ret, gap)
    return ret

def computeReversePair(init):
    count = 0
    for i in range(len(init)-1):
        for j in range(i, len(init)):
            if init[i] > init[j]:
                count += 1

    return count

def test():
    n = 2
    init = [2,1,4,3]
    m = 4
    nums = [1,2,0,2]
    ret = solver(n, init, m, nums)
    print(ret)

if __name__ == '__main__':
    test()