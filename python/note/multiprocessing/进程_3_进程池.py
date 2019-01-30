# coding:utf-8
# 2019-1-30

from  multiprocessing import Process,Pool
import time
  
"""
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中有两个方法：

apply
apply_async
"""

def Foo(i):
    time.sleep(2)
    return i+100
  
def Bar(arg):
    print(arg)

if __name__ == '__main__':
	pool = Pool(5)
	# print pool.apply(Foo,(1,))
	# print pool.apply_async(func =Foo, args=(1,)).get()
	  
	for i in range(10):
	    pool.apply_async(func=Foo, args=(i,),callback=Bar)
	  
	print('end')
	pool.close()
	pool.join() # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。