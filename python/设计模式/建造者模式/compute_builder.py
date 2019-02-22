# coding:utf-8
# 2019-2-4

"""建造模式：将产品的内部表象和产品的生成过程分割开来，从而使一个建造过程生成具有不同的内部表象的产品对象。建造模式使得产品内部表象可以独立的变化，客户不必知道产品内部组成的细节。建造模式可以强制实行一种分步骤进行的建造过程
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
角色：


抽象建造者（Builder）
具体建造者（Concrete Builder）
指挥者（Director）
产品（Product）
建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。


适用场景：
当创建复杂对象(对象由多个部分组构成, 且对象的创建要经过多个不同的步骤, 这些步骤也许还要遵从特定的顺序)

优点：
隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细的控制
--------------------- 
作者：孤傲的天狼 
来源：CSDN 
原文：https://blog.csdn.net/weixin_42040854/article/details/80612620 
版权声明：本文为博主原创文章，转载请附上博文链接！"""

class computer(object):
	"""计算机类"""
	def __init__(self, serial_number):
		self.serial_number = serial_number
		self.gpu = None
		self.cpu = None

	def __str__(self):
		return "cpu : {self.gpu}\ngpu : {self.cpu}".format(self=self)


class computerBuilder(object):
	"""建造者"""
	def __init__(self, serial_number):
		self.computer = computer(serial_number)

	def gpu_config(self, gpu):
		self.computer.gpu = gpu

	def cpu_config(self, cpu):
		self.computer.cpu = cpu


class HardwareEngineer(object):
	"""指挥者
	参数入口在指挥者函数上
	返回值也是由指挥者返回"""
	def __init__(self, builder=None):
		self.builder = builder

	def construct(self, serial_number, gpu, cpu):
		self.builder = computerBuilder(serial_number)
		self.builder.gpu_config(gpu)
		self.builder.cpu_config(cpu)

	@property
	def computer(self):
		return self.builder.computer

def main():
	serial_number = 'aaa'
	engineer = HardwareEngineer()
	engineer.construct(serial_number=serial_number, gpu='Inter Core 7', cpu='8BG')
	computer = engineer.computer
	print(computer)

if __name__ == '__main__':
	main()