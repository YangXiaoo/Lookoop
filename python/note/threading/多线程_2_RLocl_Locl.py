# coding:utf-8
# 2019-1-30

import threading
import time

gl_num = 0
lock = threading.RLock() # 同一线程内程序不会堵塞
# threading.Lock() # 会产生死锁

def show_a(arg):
    """
    多次运行可能产生混乱 这种场景就是适合使用锁的场景
    """
    global gl_num
    time.sleep(0.1)
    gl_num +=1
    print(gl_num)


def show_b(arg):
    """
    加锁
    """
    lock.acquire() # 获得锁
    global gl_num
    time.sleep(0.1)
    gl_num +=1
    print(gl_num)
    lock.release() # 解锁


for i in range(100):
    t = threading.Thread(target=show_b, args=(i,))
    t.start()

print('main thread stop')