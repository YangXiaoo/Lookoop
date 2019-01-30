# coding:utf-8
# 2019-1-30

from multiprocessing import Process
from multiprocessing import Manager
 
import time
 

 """
 进程之间无法共享数据
 """

 
li = []
 
def foo(i):
    li.append(i)
    print ('say hi',li)

if __name__ == '__main__':
	for i in range(10):
	    p = Process(target=foo,args=(i,))
	    p.start()
	p.join()
	print ('ending',li)
