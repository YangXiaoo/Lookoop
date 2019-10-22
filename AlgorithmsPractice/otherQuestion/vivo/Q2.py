#!/usr/bin/python
# -*- coding: utf-8 -*-
 
'''
Welcome to vivo !
'''

def solution(total_disk,total_memory,app_list):
    # TODO Write your code here
    ret = 0
    que = [[total_disk, total_memory, 0]] # 初始15磁盘， 10内存，0个用户
    while len(que) != 0:
        curSize = len(que)
        tmp = []
        for i in range(curSize):
            cur = que.pop()
            for app in app_list:
                disk, memory, curUser = cur
                if disk < app[0] or memory < app[1]:
                    if ret < curUser:
                        ret = curUser
                else:
                    tmp.append([disk-app[0], memory-app[1], curUser + app[2]])

        que = tmp
    return ret

def inputs():
    input1 = input()
    disk = int(input1.split()[0])
    memory = int(input1.split()[1])
    input2 = input1.split()[2]
    app_list = [[int(j) for j in i.split(',')] for i in input2.split('#')]
    print(solution(disk,memory,app_list))

def test():
    disk = 15
    memory = 10
    s = "5,1,1000#2,3,3000#5,2,15000#10,4,16000"
    app_list = [list(map(int, x.split(","))) for x in s.split("#")]
    print(solution(disk,memory,app_list))

if __name__ == "__main__":
    test()
