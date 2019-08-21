# coding:utf-8
# 指定范围内质数的各位和与十位和的最小值
from math import sqrt
import sys
def solver(low, high):
    prime = []
    for n in range(low, high):
        if isPrime(n):
            if n > 1:
                prime.append(n)

    # print(prime)
    # 每个质数的十位各位值, 如果没有则输出0
    if len(prime) == 0:
        return 0

    ret1 = 0    # 各位
    ret2 = 0    # 十位和
    # print(prime)
    for n in prime:
        if n >= 10:
            tmp = n // 10
            ret2 += tmp % 10
            # print(ret2)
        ret1 += n % 10
    # print(ret1, ret2)
    return min(ret1, ret2)


def isPrime(num):
    # print("[debug] sqrt-num: {}, num: {}".format(int(sqrt(num)), num))
    for j in range(2, int(sqrt(num)) + 1):
        # print("[debug] j: {}, num: {}".format(j, num))
        if num % j == 0:
            return False

    return True


def test():
    low, high = 1, 9
    ret = solver(low, high)
    print(ret)

if __name__ == '__main__':
    test()