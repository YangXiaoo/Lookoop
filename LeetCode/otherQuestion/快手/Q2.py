# coding:utf-8
# 输入一个32为整型数每次每个位上的数取平方相加得到的新的数采取同样操作，看最后是否能得到1， 如果能则为true, 反之为false
import sys
# AC 100%
def solver(nums):
    ret = []
    for n in nums:
        maps = {}   # 记录重复数
        while True:
            if n not in maps:
                maps[n] = 0
            else:
                ret.append("false")
                break

            if n == 1:
                ret.append("true")
                break

            n = getNext(n)

    return ret 

def getNext(n):
    ret = 0
    while n > 0:
        cur = n % 10
        ret += cur ** 2
        n = n // 10

    return ret

def printRet(ret):
    for n in ret:
        print(n)

def inputs():
    n = int(sys.stdin.readline().strip())
    nums = []
    for i in range(n):
        cur = int(sys.stdin.readline().strip())
        nums.append(cur)

    ret = solver(nums)
    printRet(ret)

def test():
    nums = [19, 7]
    ret = solver(nums)
    printRet(ret)


if __name__ == '__main__':
    inputs()