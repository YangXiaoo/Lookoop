# coding:utf-8
# 2019-2-1

"""
工厂方法设计模式的实现是一个不属于任何类的单一函数，负责单一种变量的创建

The Factory Method design pattern is implemented as a single function that doesn't
belong to any class, and is responsible for the creation of a single kind of object
(a shape, a connection point, and so on).
"""

class A(object):
	def __init__(self, par):
		self.par = par

	@property
	def foo(self):
		print("A: ", self.par)


class B(object):
	def __init__(self, par):
		self.par = par

	@property
	def foo(self):
		print("B: ", self.par)	


def factory(par):
	"""工厂接口"""
	if len(par) > 5:
		tool = A(par)
	else:
		tool = B(par)

	return tool


def main():
	par = 'dfdfsdf'
	tool = factory(par)
	tool.foo

if __name__ == '__main__':
	main()