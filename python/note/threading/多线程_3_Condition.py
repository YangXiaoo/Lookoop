# coding:utf-8
# 2019-1-30

import threading
import time

"""
Condition（条件变量）通常与一个锁关联。 需要在多个Contidion中共享一个锁时, 可以传递一个Lock/RLock实例给构造方法, 否则它将自己生成一个RLock实例。
可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

构造方法： 
Condition([lock/rlock])

实例方法： 
　　acquire([timeout])/release(): 调用关联的锁的相应方法。 
　　wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。 
　　notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。 
　　notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
"""

condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1;
                    print ("Producer(%s):deliver one, now products:%s" %(self.name, products))
                    condition.notify() # 从等待池中挑选一个线程并通知由下一句释放锁定
                    condition.release()
                else:
                    print ("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products))
                    condition.wait(); # 商品数量已近满了所以讲当前线程放入等待池等待被通知
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print ("Consumer(%s):consume one, now products:%s" %(self.name, products))
                    condition.notify()
                    condition.release()
                else:
                    print ("Consumer(%s):only 1, stop consume, products:%s" %(self.name, products))
                    condition.wait();
                time.sleep(2)

if __name__ == "__main__":
    for p in range(0, 2):
        p = Producer()
        p.start()

    for c in range(0, 3):
        c = Consumer()
        c.start()
