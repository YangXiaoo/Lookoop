# coding:utf-8
# 2019-2-1
"""The Abstract Factory design pattern is implemented as a number of Factory Methods
that belong to a single class and are used to create a family of related objects (the
parts of a car, the environment of a game, and so forth)"""

class Knight(object):
	"""创建角色"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact(self, obstacle):
		print('\nhello {}, you will {}, and {}'.format(self, obstacle, obstacle.action()))


class Dargon(object):
	""""创建小兵"""
	def __str__(self):
		return 'encounter Dargon'

	def action(self):
		return 'fight with it.'


class SavePrinces(object):
	"""一种游戏"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return '\n __SavePrinces__'

	def make_character(self):
		return Knight(self.name)

	def make_obstacle(self):
		return Dargon()


class Frog(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact(self, obstacle):
		print('\nhello {}, you will {}, and {}'.format(self, obstacle, obstacle.action()))

class Bug(object):
	def __str__(self):
		return 'encounter bugs'

	def action(self):
		return 'eat it'


class FrogWord(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return '\n__FrogWorld__'

	def make_character(self):
		return Frog(self.name)

	def make_obstacle(self):
		return Bug()


class GameEnv(object):
	"""抽象工厂设计模式"""
	def __init__(self, game):
		"""传入参数为类"""
		self.character = game.make_character()
		self.obstacle = game.make_obstacle()
		print(game)

	def play(self):
		self.character.interact(self.obstacle)


def main():
	inputs = '0'
	name = 'yauno'

	if int(inputs) == 0:
		game = GameEnv(SavePrinces(name))
	elif int(inputs) == 1:
		game = GameEnv(FrogWord(name))
	else:
		raise ValueError('Wrong choose[1, 2].')

	game.play()

if __name__ == '__main__':
	main()