# coding:utf-8
# 2019-2-4

"""适配器让两个或多个不兼容的接口兼容"""

class Human(object):
	def __init__(self, name):
		self.name = name

	def speak(self):
		print('{} say hello.'.format(self.name))


class Mp3(object):
	def __init__(self, name):
		self.name = name

	def play(self):
		print("play song: {}".format(self.name))


class Computer(object):
	def __init__(self, name):
		self.name = name

	def excute(self):
		print('{} show message.'.format(self.name))


class Adapter(object):
	"""统一接口"""
	def __init__(self, obj, extend_method=None):
		self.obj = obj 
		if extend_method:
			self.__dict__.update(extend_method)

def main():
	objects = []
	human = Human('yauno')
	mp3 = Mp3('young and beautiful')
	computer = Computer('screen')

	objects.append(Adapter(human, dict(excute=human.speak)))
	objects.append(Adapter(mp3, dict(excute=mp3.play)))
	objects.append(computer)

	for obj in objects:
		# print(obj)
		obj.excute()

if __name__ == '__main__':
	main()