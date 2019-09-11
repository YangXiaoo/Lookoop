#!/usr/bin/python
# -*- coding: utf-8 -*-
 
'''
Welcome to vivo !
输入：
(()(()((()(0)))))
输出：
5
'''

def solution(s):

    #TODO Write your code here
    
    giftIndex = findGift(s)
    ret = []
    for gitf in giftIndex:
        cur = getMin(s, gitf)
        ret.append(cur)

    return min(ret)

def findGift(s):
    """找到礼物的位置"""
    ret = []
    for index, c in enumerate(s):
        if c == '0':
            ret.append(index)

    return ret

def getMin(s, index):
    """给定s与礼物位置，找出最少需要拆的盒子"""
    stack = []
    # maps = {')':'('}
    for i, c in enumerate(s[:index]):
        if c == '(':
            stack.append(c)
        else:
            stack.pop()

    return len(stack)

def test():
    s = "(()(()((()(0)))))"
    ret = solution(s)
    print(ret)

def inputs():
    input = input()
    print(solution(input))


if __name__ == '__main__':
    test()