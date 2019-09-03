# coding:utf-8
# 2019/9/3
"""
给定一个整数的数组，找出其中的pair(a,  b)，使得a+b=0，并返回这样的pair数目。（a,  b）和(b,  a)是同一组。

输入
 整数数组

输出
找到的pair数目   


样例输入
-1,  2,   4,  5,  -2
样例输出
1
"""

def solver(nums):
    maps = {}
    ret = 0
    retList = []
    for n in nums:
        if n in maps:
            if maps[n] == 1:
                if n not in retList and -n not in retList:
                    retList.append(n)
                    ret += 1

        maps[-n] = maps.get(-n, 0) + 1

    # print(maps, retList)
    return ret 


def test():
    nums = [0,0,0, -1, 1, -1, 1]
    ret = solver(nums)
    print(ret)

def inputs():
    nums = list(map(int, input().strip().split(" ")))
    ret = solver(nums)
    print(ret)

if __name__ == '__main__':
    test()