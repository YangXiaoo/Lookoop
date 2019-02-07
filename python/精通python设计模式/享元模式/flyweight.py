# coding:utf-8
# 2019-2-6

"""享元模式

所谓享元模式就是运行共享技术有效地支持大量细粒度对象的复用。系统使用少量对象,而且这些都比较相似，状态变化小，可以实现对象的多次复用。

      共享模式是支持大量细粒度对象的复用，所以享元模式要求能够共享的对象必须是细粒度对象。

      在了解享元模式之前我们先要了解两个概念：内部状态、外部状态。

      内部状态：在享元对象内部不随外界环境改变而改变的共享部分。

      外部状态：随着环境的改变而改变，不能够共享的状态就是外部状态。

      由于享元模式区分了内部状态和外部状态，所以我们可以通过设置不同的外部状态使得相同的对象可以具备一些不同的特性，而内部状态设置为相同部分。在我们的程序设计过程中，我们可能会需要大量的细粒度对象来表示对象，如果这些对象除了几个参数不同外其他部分都相同，这个时候我们就可以利用享元模式来大大减少应用程序当中的对象。如何利用享元模式呢？这里我们只需要将他们少部分的不同的部分当做参数移动到类实例的外部去，然后再方法调用的时候将他们传递过来就可以了。这里也就说明了一点：内部状态存储于享元对象内部，而外部状态则应该由客户端来考虑。

优点
      1、享元模式的优点在于它能够极大的减少系统中对象的个数。

      2、享元模式由于使用了外部状态，外部状态相对独立，不会影响到内部状态，所以享元模式使得享元对象能够在不同的环境被共享。

缺点
      1、由于享元模式需要区分外部状态和内部状态，使得应用程序在某种程度上来说更加复杂化了。

      2、为了使对象可以共享，享元模式需要将享元对象的状态外部化，而读取外部状态使得运行时间变长。 
"""

from enum import Enum 

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree():
	pool = dict()

	def __new__(self, tree_type):
		obj = self.pool.get(tree_type, None)

		if not obj:
			obj = object.__new__(self) # 创建对象
			self.pool[tree_type] = obj
			obj.tree_type = tree_type

		return obj 

	def render(self, age, x, y):
		print('type of a tree: {} at ({}, {})'.format(age, x, y))


def main():
	t1 = Tree(TreeType.apple_tree)
	t2 = Tree(TreeType.apple_tree)
	t3 = Tree(TreeType.cherry_tree)
	t4 = Tree(TreeType.peach_tree)

	print('id(t1):{}, id(t2):{}, id(t1) == id(t2)? : {}'.format(id(t1), id(t2), id(t1) == id(t2)))
	print('id(t3):{}, id(t4):{}, id(t3) == id(t4)? : {}'.format(id(t3), id(t4), id(t3) == id(t4)))

if __name__ == '__main__':
	main()

