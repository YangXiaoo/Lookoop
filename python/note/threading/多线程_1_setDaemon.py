# coding:utf-8
# 2019-1-30

import  threading
import time

def action(arg):
	print("current arg is: %s" % arg)
	time.sleep(1)
	print("current threading: %s" % threading.currentThread().getName)


for i in range(5):
	t = threading.Thread(target=action, args=(i, ))
	t.setDaemon(True) # 主线程结束之后后台线程也结束
	t.start()

t.join() # 当setDaemon设置为True时, 等待子线程结束之后才终止主线程

print("main thrading end")


"""
setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
	如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
    如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
"""