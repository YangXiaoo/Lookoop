#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
"""
小米之家有很多米粉喜欢的产品，产品种类很多，价格也不同。比如某签字笔1元，某充电宝79元，某电池1元，某电视1999元等

假设库存不限，小明去小米之家买东西，要用光N元预算的钱，请问他最少能买几件产品？

输入
第1行为产品种类数

接下来的每行为每种产品的价格

最后一行为预算金额


输出
能买到的最少的产品的件数，无法没有匹配的返回-1


样例输入
2
500
1
1000
样例输出
2
"""
#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************

# ac 71%
def  solution(prices, budget):
    """最少能买几件"""
    prices.sort()
    prices = prices[::-1]   # 从高到低排序
    if budget == 0 or 0 in prices:
        return -1
    # print(prices)
    ret = 0
    for p in prices:
        cur = budget // p
        ret += cur
        budget -= cur*p
        if budget == 0:
            break
        
    if ret == 0 or budget != 0: # 没有匹配或者钱没有用完
        ret = -1

    return ret



#******************************结束写代码******************************

def inputs():
    _prices_cnt = 0
    _prices_cnt = int(input())
    _prices_i=0
    _prices = []
    while _prices_i < _prices_cnt:
        _prices_item = int(input())
        _prices.append(_prices_item)
        _prices_i+=1

    _budget = int(input())

      
    res = solution(_prices, _budget)

    print(str(res) + "\n")

def test():
    prices = [0]
    budget = 0
    ret = solution(prices, budget)
    print(ret)

if __name__ == '__main__':
    test()