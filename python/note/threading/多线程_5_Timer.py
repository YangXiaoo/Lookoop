# coding:utf-8
# 2019-1-30

import threading
import time

def action(arg=None):
	print("action")

print("staring timer... wait for 5 sec.")
timer = threading.Timer(5, action)
timer.start()