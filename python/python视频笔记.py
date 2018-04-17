#date(2018-4-15)
1)OS模块简单介绍
		OS对进程和进程运行环境进行管理，OS模块还可以处理大部分文件系统操作：比如删除
	重命名文件，遍历目录树，以及管理文件访问权限。
	OS与SYS的区别：
		os负责程序与操作系统的交互，sys负责程序与python解释器的交互
	os.path和sys.path：
		sys.path是常用的PATH环境变量，os.path是一个模块，提供一些方法函数。
	(1)函数使用
		os.name: 输出字符串指示正在使用的平台。
		os.getcwd():函数得到当前工作目录。运行目录：程序执行目录。工作目录，
					程序运行时，操作的一系列相对路径。
		os.listdir():返回指定目录下的所有文件和目录名的一个列表，但没有列出是什么目录什么文件。
		os.remove('file_name'):删除指定文件
		os.rmdir('dir_name'):删除指定目录
		os.mkdir('dir_name'):创建目录
		os.makedirs('/a/b/c')：递归创建目录
		os.system('ls'):执行shell命令
		os.chdir('file_path'):改变工作目录
		os.chmod('file_name'):改变文件或目录的权限
		os.path.isdir('dir_name'):是否为目录，返回值为bool
		os.path.isfile('file_name')
		os.path.islink('name')
		os.path.getsize('file_name')

2)pickle模块
	mylist = [1,2,3,4]
	obj = pickle.dumps(mylist) #转换为二进制
	var = pickle.loads(obj)	#转换

	dump(obj, file) :将对象写到文件，可以是实际文件，也可以是任何类似于文件的对象
	obj = load(file):把文件里保存的数据返回成原来的数据对象

	myfile = open('1','+wb') #二进制写入模式打开
	pickle.dump(mylist, myfile) #写入文件中
	myfile.close()  #关闭文件流
	myfile = open('1','rb')
	var = pickle.load(myfile)


3)闭包

def wai():
	a = 1
	def nei():
		print(a)
	return nei

func = wai()

---------
def func(num):
	def func1(num1):
		print(num+num1)
	return func1
var = func(10) #闭包私有化
var(20) #结果为30
-------------
mylist = [1,2,3,4]

def func(obj):
	def func1():
		obj[0] += 1
		print(obj)
	return func1

var = func(mylist) #[2,2,3,4]  实现了闭包私有化
var()			#[3,2,3,4]
var()			#[4,2,3,4]
var()			#[5,2,3,4]
print(mylist)   #[5,2,3,4]


4)装饰器
	@func1
	def func2():
		pass

	函数运行时增加功能且不影响这个函数原有的内容
	(1)普通装饰器
----------------------------
def func1(func):
	def add_func():
		print('这是我要添加的功能')
		return func()  #函数调用
	return add_func

@func1  #装饰器函数
def func2():  #被装饰函数
	print('hello wolrd')

func2()  #func1(func2)()

---------------------
#带参数的装饰器
def func1(func):
	def func2(a,b):
		print(a,b)
		return func(a,b)
	return func2

@func1
def func(x,y):
	print('This is a add function')
	print(x+y)

func(10,20) 

-----------------------
#装饰器函数带参数
def arg_func(arg):
	def _func(func):
		def _func1():
			if arg == 'good':
				print('go out')
			elif arg == 'bad'
				print('stay home')
			return func()
		return _func1
	return _func

#arg_func 装饰器函数的参数接受函数，因为装饰器函数只能接受函数
#arg_func 	-> 	_func
#_func 		-> 	_func1
#_func1 	-> 	执行添加功能，执行被装饰的函数

@arg_func('bad')
def func():
	print('bad day')

@arg_func('good')
def  func1():
	print('good day')

func()  #函数调用,func为函数名
func1()




正则
----
特殊符号与字符
\d :匹配任何数字
\s ：匹配任何空白符\n\t\r\v\f 
\w :匹配任何数字，字母，字符==[a-zA-Z0-9_]

	(1)re.compile(pattern) 
		编译正则表达式
	(2)re.match(pattern,string) 
		使用正则表达式匹配字符串，匹配成功则返回一个匹配对象，否则返回None；
	成功时可以使用结果的group函数获取匹配到的值
	(3)re.search(pattern,string)
		返回字符串中正则表达式pattern的第一次出现
	(4)re.split(pattern,string)
		根据模式来分割字符串
	(5)re.final(pattern,string) 
		返回一个列表，包含字符串中所有模式匹配的的子串
	(6)re.sub(pat,repl,string)
		将字符串中与pat匹配的字符换位repl
		string = 'a*b*s'
  		re.sub('\*','-',string)

	reg = re.compile('^a')
	res = re.match(reg,'adssdaa')
	res.group() #返回结果

########简单网页爬虫
	from urllib.request import *

	import re

	url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1523799239447_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A3%8E%E6%99%AF'
	html = urlopen(url)

	obj = html.read().decode()

	urls = re.findall(r'"thumbURL":"(.*?)"',obj)

	index = 0
	for url in urls:
		try:
			print('downloading...%d'%index)
			urlretrieve(url,'pic'+str(index)+'.jpg')
			index += 1
		except Exception:
			print('Error...%d'%index)
		else:
			print('complete')

面向对象
-------
类：抽象出来的属性集合，是描述
实例：具体实例
属性：类中的方法函数也可以是类中的变量
实例属性：定义在方法中的属性，只作用于当前实例的类
类属性：类属性在整个实例化的对象中共有，类属性定在在类中且在函数体外，类属性通常不作为实例属性使用

1)构造函数__init__(self)
		构造方法或初始化函数
	class A:   #自己不能有这个方法
		def __init__(self): #专门为实例初始的函数，若没有self，实例无法使用
			self.num = 1
	a = A()
	b = A()
	a.num = 1 #A.num没有值，实例变量独立私有

2)函数 
	class A:
		def func(self,x,y):
			print('x+y:',x+y)

	a = A()
	a.func(3,4) #结果为7
	A.func(3,4) #报错，因为使用了self

3)类的方法 
	class A:  #自己可以有自己的方法
		num = 1  #类方法可以访问类变量num
		@classmethod
		def func(cls):  #用cls指向num 
			print('num:',cls.num)

	A.func()  	# num: 1
	a = A()
	a.func()	# num: 1

4)静态方法
@staticmethod
静态方法不需要默认的任何参数，跟一般的普通函数类似
这样就可以在多个实例化彼此之间共享这个函数中的数据和内容
	class A:
		@staticmethod
		def func():
			print('hell worl')

	A.func() #hello world
	a = A()
	b = A() #实例a和b都是同一个实例

类方法需要传递cls参数，静态方法无需传递
静态方法和类方法都不可以访问实例变量 #__init__(self)构造的函数
类方法可以访问类变量num，静态方法不可以


继承
----
1)使用
	class A:
		@staticmethod
		def func():
			print('hell worl')

	class A1(A):
		pass

	A1.func()  #结果为 hello world

	A1.__bases__  #继承自A
	A.__bases__   #继承自object(原始父类)

2)有初始化时
	class A:
		def __init__(self):
			self.num = 1
			print('hell worl')

	class A1(A):
		pass

	a = A()  	
	a.num 		# 1
	b = A1()
	b.num 		# 1  #也继承了A的实列

	class A1(A):   #重写将覆盖继承与父类的属性
		def __init__(self):
			self.var = 1 

	#子类未定义自己的构造函数时继承父类构造函数


多继承
------
class A:
	def __init__(self):
		print('this is a')

class B:
	def __init__(self):
		print('this is b')

class C(A,B): #继承顺序为从左到右，从下到上的方式进行
	pass

c = C()  #this is a 



多态
----
多态：根据数据的类型执行不同的操作
实现多态：在面向对象中实现多态，通过对子类重写父类中已有的函数

class A:
	def func(self):
		print('this is a')

class B:
	def func(self):
		print('this is b')

a = A() #this is a 
b = B() #this is b

print(instance(a,A))  # True ,a是A的实例
print(instance(b,A))  # True
print(instance(a,B))  # False

def myfunc(var):
	var.func()

myfunc(a)  # this is a 
myfunc(b)  # this is b


其它类中的内建函数
-----------------
1) __call__(self)  #使实例可以回调函数

class A:
	def __call__(self):
		print('this is A')
a = A()
a()  #执行call函数中的内容

2)__del__ 

class A:
	def __del__(self):   #一般可以不用写
		print('this is delete')
	def __new__(self):  
	#构造函数，执行过程中，分配空间，给一个空篮子
		print('this is new')
		return super(A,self).__new__(self)  #找到父类
	def __init__(self): #数据初始化，
		self.num = 1

a = A()
a.num  # 1

del a  # 删除实例

3)__slots__(self)

class A:
	__slots__('name','age')  #此时的实例不能创建其新变量，将属性锁定到规定的范围内

a = A()
a.name = youth
a.age = 23
a.height = 170 #错误，不能创建，因为已经被锁定了



循环与递归
--------------
	重复执行，解决的问题是线性的

#遍历列表
mylist = [1,2,3,[4,5],[6,[7,8]]]

def func(obj):
	for var in obj:
		if 'list' in str(type(var)):
			func(var)
		else:
			print(var)
	return None 
func(mylist)


CSV文件操作
-----------
 - open 
 - r 	#读
 - w 	#写，但会截断清空
 - a  	#附加
 - +	#读写模式
#csv文件写
import csv

fp = open('1.csv', 'a+')
mylist = [1,2,3,4,5]
mystr = ','.join([str(var) for var in mylist])
#csv_fp = csv.writer(fp) #处理成支持csv文件操作的对象
fp.write(mystr)
fp.write('\n')
fp.write(mystr)
fp.close()


#读
fp = open('1.csv', 'r',encoding='utf-8')
mystr = fp.read()

mylist = mystr.strip().split('\n') #有空字符

for var in mylist:
	print(var.split(','))

fp.close()

6
---------------
爬虫
web
自动化运维
数据分析
测试
QT,MFC,VC,VB