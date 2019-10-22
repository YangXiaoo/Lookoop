# coding:utf-8
"""给定一个字符串A，一个字符串B，求B在A中出现的次数"""
import sys
def solver(a, b):
    ret = 0
    lenB = len(b)
    lenA = len(a)
    if lenA < lenB:
        return ret 

    for i in range(0, lenA - lenB + 1):
        cur = a[i:i+lenB]
        if cur == b:
            ret += 1


    return ret 

def test():
    a, b = "zyzyzyz", "zyz"
    ret = solver(a, b)
    print(ret)

def inputs():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    ret = solver(a, b)
    print(ret)

if __name__ == '__main__':
    inputs()