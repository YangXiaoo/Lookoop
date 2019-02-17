# coding:utf-8
import tool_test_yauno

def fooo(arg=None,
		 a=None):
	for i in range(1000000000):
		pass
	print("end")

if __name__ == '__main__':
	import cProfile
	cProfile.run("fooo()")
	 