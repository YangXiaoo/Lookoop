# coding:utf-8
# 2019-2-6

"""外观模式
外观模式的一般描述是 : 外观模式定义了一个高层的功能, 为子系统中的多个模块协同的完成某种功能需求提供简单的对外功能调用方式, 使得这一子系统更加容易被外部使用。

外观模式的目的不是给予子系统添加新的功能接口, 而是为了让外部减少与子系统内多个模块的交互, 松散耦合, 从而让外部能够更简单地使用子系统。

外观模式的本质是：封装交互，简化调用。

https://www.cnblogs.com/lwbqqyumidi/p/3754251.html
"""
from abc import ABCMeta, abstractmethod

class Excute(metaclass=ABCMeta):
	"""执行操作类"""
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def approve(self):
		pass


class RevenueOffice(Excute):
	"""财政部"""
	def __init__(self, type):
		self.type = type

	def approve(self):
		print("RevenueOffice approved, type: {self.type}".format(self=self))


class SaicOffice(Excute):
	"""工商局"""
	def __init__(self, type):
		self.type = type

	def approve(self):
		print("SaicOffice approved, type: {self.type}".format(self=self))


class ApproveFacade(object):
	"""外观模式"""
	def __init__(self, type):
		self.type = type

	def excute_approve(self):
		revenue = RevenueOffice(self.type)
		saic = SaicOffice(self.type)

		revenue.approve()
		saic.approve()


def main():
	work_type = 1
	office = ApproveFacade(work_type)

	office.excute_approve()

if __name__ == '__main__':
	main()

