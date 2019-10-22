# coding:utf-8

class Map(object):
	def __init__(self, capcity):
		self.capcity = capcity
		self.map = {}
		self.nums = [0 for x in range(capcity)]
		self.size = 0

	def put(self, key, val):
		if self.size == capcity:
			self.remove()
		else:
			map[key] = value

		