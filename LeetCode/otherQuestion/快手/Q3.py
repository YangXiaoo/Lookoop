# coding:utf-8
# 合并输入流，输入两行，第一行数据每隔4个插入第二行的一个数据，第二行多余的数据插入第一行末尾

import sys
# AC 100%
def solver(line1, line2):
    ret = []
    index = 0
    for i in range(len(line1)):
        if i != 0 and i % 4 == 0:
            if index < len(line2):
                ret.append(line2[index])
                index += 1
        ret.append(line1[i])
    if index != len(line2):
        ret.extend(line2[index:])

    return " ".join(ret)

def inputs():
    line1 = sys.stdin.readline().strip().split(" ")
    line2 = sys.stdin.readline().strip().split(" ")

    ret = solver(line1, line2)
    print(ret)

def test():
    line1 = ['1','2','3','4','5','6','7','8','9']
    line2 = ['a', 'b', 'c']

    ret = solver(line1, line2)
    print(ret)

if __name__ == '__main__':
    test()