# coding:utf-8
# 2019-1-30

import threading
import time

"""
Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。

Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

构造方法： 
Event()

实例方法： 
　　isSet(): 当内置标志为True时返回True。 
　　set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。 
　　clear(): 将标志设为False。 
　　wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。
"""
event = threading.Event()


def action(arg=None):
	print("current threading: %s" % threading.currentThread().getName())
	time.sleep(1)

	event.wait() # 等待event.set设置之后运行剩下的程序

	print("%s recive event" % threading.currentThread().getName())

queue = []

for i in range(5):
	t = threading.Thread(target=action, args=(i, ))
	queue.append(t)

for t in queue:
	t.start()

time.sleep(2)

event.clear()
print("Main thread set evevt.")
event.set()


