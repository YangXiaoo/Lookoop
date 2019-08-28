# coding:utf-8
import sys
"""
给出一个仅包含加减乘除四种运算符的算式(不含括号)，如1+2*3/4，在保持运算符顺序不变的情况下，现在你可以进行若干次如下操作：如果交换相邻的两个数，表达式值不变，那么你就可以交换这两个数。

现在你可以进行任意次操作，使得算式的数字序列字典序最小，然后输出结果，数字之间的字典序定义为若a<b则a的字典序小于b。

输入
第一行包含一个整数n，表示算式的长度，即包含n个数字和n-1个运算符。(1≤n≤100000)。

第二行包含一个含有n个非0整数和n-1个运算符的算式，整数与运算符用空格隔开，运算符包括“+，-，*，/”，整数的绝对值不超过1000。

输出
按要求输出字典序最小的表达式，数字与符号之间用空格隔开。


样例输入
6
3 + 2 + 1 + -4 * -5 + 1
样例输出
1 + 2 + 3 + -5 * -4 + 1 
"""
# AC 9%
def solver(ops):
    """
    @param ops 字符串
    """
    opsList = ops.split(" ")
    i = 0
    numLens = (len(opsList) + 1) >> 1   # 数字长度
    symbol = []
    digits = []
    for x in range(1, len(opsList), 2):
        symbol.append(opsList[x])
    for x in range(0, len(opsList), 2):
        digits.append(opsList[x])

    # print("[debug] symbol: {}".format(symbol))
    # print("[debug] digits: {}".format(digits))
    i = 0
    it = 0
    while i < len(symbol):
        curLast = findSameOps(symbol, i)
        digits = handle(digits, i, curLast)
        # print("[debug] i:{}, curLast:{}, digits:{}".format(i, curLast, digits))
        i = curLast + 1

        it += 1
        # if it > 10:
        #     break

    ret = []
    for j in range(numLens-1):
        ret.append(digits[j])
        ret.append(symbol[j])
    ret.append(digits[-1])

    return " ".join(ret)

def handle(digits, left, right):
    right += 1
    tmp = digits[left:right]
    tmp = list(map(int, tmp))
    tmp.sort()
    # print("left:{}, right:{}, tmp:{}".format(left, right, tmp))
    tmp = [str(x) for x in tmp]
    digits = digits[:left] + tmp + digits[right:]

    return digits


def findSameOps(symbol, i):
    ret = i
    ops = symbol[i]
    flag = getFlag(ops)
    for j in range(i+1, len(symbol)):
        cur = getFlag(symbol[j])
        # print("cur:{}, flag:{}, i:{}".format(cur, flag, j))
        if cur != flag:
            if j - i == 1:
                return j
            else:
                return j - 1

    return len(symbol) - 1


def getFlag(ops):
    flag = 0    # 默认乘
    if ops == '+':
        flag = 1
    elif ops == '-':
        flag = 2
    elif ops == '/':
        flag = 3    # 除法

    return flag

def test():
    s = "3 + -2 + 1 + -4 * -5 + 1"
    ret = solver(s)
    print(ret)

def inputs():
    n = input()
    ops = input().strip()
    ret = solver(ops)
    print(ret)

if __name__ == '__main__':
    test()