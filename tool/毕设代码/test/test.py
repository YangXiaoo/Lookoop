# coding:utf-8
import math

class A():
	def f(self, a, b):
		print(a,b)

class B(A):
	def f(self, a):
		print(a)

t = B()
t.f('a', 'b')