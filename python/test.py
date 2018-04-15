def func(num):
	def func1(num1):
		print(num+num1)
	return func1
var = func(10)
var(20) #结果为30