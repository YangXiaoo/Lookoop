# coding:utf-8
# 2019-2-4

import copy

class Book(object):
	def __init__(self, name, author, price, **rest):
		self.name = name
		self.author = author
		self.price = price
		self.__dict__.update(rest)

	def __str__(self):
		ret = []
		content = sorted(self.__dict__.items())
		for k,v in content:
			ret.append('{} : {}'.format(k, v))
		return '\n'.join(ret)


class Prototype(object):
	"""原型"""
	def __init__(self):
		self.objects = dict()

	def register(self, identifier, obj):
		self.objects[identifier] = obj 

	def unregister(self, identifier, obj):
		if identifier in self.objects:
			del self.objects[identifier]
		else:
			raise ValueError('identifier {} not exists.'.format(identifier))

	def clone(self, identifier, **attr):
		if identifier in self.objects:
			obj = self.objects[identifier]
		else:
			raise ValueError('identifier {} not exists.'.format(identifier))

		new_obj = copy.deepcopy(obj)
		new_obj.__dict__.update(**attr)

		return new_obj


def main():
	book_1 = Book('name', 'author', 'price', publisher='yauno', publish_date='1995-03-07')

	prototype = Prototype()

	identifier = 'yauno_01'
	prototype.register(identifier, book_1)

	book_2 = prototype.clone(identifier, publisher='yangxiao', publish_date='2019-2-4')

	books = [book_1, book_2]

	for book in books:
		print(id(book))
		print(book)
		print()

if __name__ == '__main__':
	main()