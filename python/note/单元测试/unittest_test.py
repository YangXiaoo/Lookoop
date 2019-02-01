# coding:utf-8
# 2019-2-1
import func
import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		"""初始化参数. 每一个执行模块都要先执行该函数"""
		print("runing setup.")
		self.foo = func.MyFunc()

	def tearDown(self):
		"""最后执行"""
		print("runing tearDown")
		self.foo = None

	def testAdd(self):
		self.assertEqual(self.foo.add(-1, 4), 3)


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(MyTest("testAdd"))

	runner = unittest.TextTestRunner()
	runner.run(suite)