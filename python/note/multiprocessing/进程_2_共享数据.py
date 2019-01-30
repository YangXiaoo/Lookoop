# coding:utf-8
# 2019-1-30

from multiprocessing import Process, Array, Manager, RLock
import time

array = Array('i', [11,22,33,44])

def action(arg):
    array[arg] = 100 + arg
    print("arg: %s, array[%s]: %s" % (arg, arg, array[arg]))



 
def Foo(i, dic):
    dic[i] = 100+i
    print(dic.values())
 

def Foo_a(lock,temp,i):
    """
    将第0个数加100
    """
    lock.acquire()
    temp[0] = 100+i
    for item in temp:
        print(i,'----->',item)
    lock.release()




if __name__ == '__main__':
    # for i in range(4):
    #     process = Process(target=action, args=(i, ))
    #     process.start()

    # manage = Manager()
    # dic = manage.dict()
    # for i in range(2):
    #     p = Process(target=Foo,args=(i,dic, ))
    #     p.start()
    #     p.join()

    lock = RLock()
    temp = Array('i', [11, 22, 33, 44])

    for i in range(20):
        p = Process(target=Foo_a,args=(lock,temp,i,))
        p.start()