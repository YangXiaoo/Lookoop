# coding:utf-8
# 2019-2-15
# https://www.cnblogs.com/wangyongsong/p/6750454.html
class A(object):
	x = 1

	@classmethod
	def test(cls): # cls传入的是当前类本身，被继承后传入其孩子
		print(cls, cls.x)


class B(A):
	x = 2


b = B()
b.test()