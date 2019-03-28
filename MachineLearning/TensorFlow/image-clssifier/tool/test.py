# coding:utf-8
import os



low = 4
for k, i in enumerate(range(5)):
	
	if k < low:
		print("skip traindata: {}".format(k))
		continue
	print("trianing: {}".format(k))