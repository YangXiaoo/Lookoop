# 2018-8-5
# Bucket Sort

# Reference
# Introduction to Algorithms [P112]
# Data Structures and Algorithm Analysis in C [P189]
# https://www.cnblogs.com/shihuc/p/6344406.html

class BucketSort(object):
	def __init__(self, A, m):
		self.A = A # Integer Arrary
		self.lens = len(A)
		self.m = m
		self.bucket = {}

	def Sort(self):
		self.putIntoBucket()

