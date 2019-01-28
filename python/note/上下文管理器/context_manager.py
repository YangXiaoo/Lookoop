# coding=utf-8
# 2019-1-28
# 上下文管理器
# __enter__ 与 __exit__ 用于资源分配以及释放相关工作, 如打开关闭文件, 异常处理, 断开流的链接以及锁分配
class MyContextManager(object):
	def __enter__(self):
		print("extering...")

	def __exit__(self, exception_type, exception_value, traceback):
		print("leaving...")

		if exception_type is None:
			print("No Exception.")
			return False

		elif exception_type is ValueError:
			print("Value error")
			return False
		else:
			print("other error")
			return True


if __name__ == '__main__':
	# with MyContextManager():
	# 	print("Testing..")
	# 	raise(ValueError)

	with MyContextManager():
		print("Testing..")