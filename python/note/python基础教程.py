#date(2018-4-9	)
#Python基础教程(第三版)
#【Beginning Python From Novice to Professional - Third Edition】
Linux下安装
----------
[root]# cd /usr/local/src
[root]# wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
[root]# tar zxvf Python-3.6.5.tgz
[root]# cd Python-3.6.5
[root]# ./configure
[root]# make & make install

基础知识
--------
1)字符串
	(1)使用'''xxx'''
	(2)使用转移符换行
	(3)原始字符串 r
2)基本函数
	abs(number)
	bytes(string,encodeing)
	cmath.sqrt(number)
	float(object)
	input(prompt)
	int(object)
	math.ceil(number)
	math.floor(number)
	math.sqrt(number)
	pow(x,y)
	repr(object)
	round(number)
	str(object)

3)序列-列表和元组
	(1)区别
		列表[]可以修改，元组()不可以修改
	(2)操作
		索引，切片，相加(拼接)，相乘，成员资格检查
	(3)切片
		第一个索引指定的元素包含在切片内，第二个索引指定的元素不包含在切片内。
		第一个指定索引位于第二个指定索引的后面则为空序列
		number[-3:0] 返回空
		number[0:10:2] 2个步长
4)列表
	删除，切片赋值
	(1)列表方法
		list('print')		#字符串转为列表
		lst=[1,2,3]
		lst.append(4) 		#附加到列表末尾
		lst.clear()  		#清空列表
		lit_a=lst.copy() 	#复制列表而非关联
		lis.count(1) 		#1出现的次数
		a=[5,6,7]
		lst.extend(a)		#用一个表扩展另一个表
		lst.index(2)		#2第一次出现的索引
		lst_a.insert(1,'new') 	#[1,new,2,3,4]
		lst_a.pop()			# 从列表中删除末尾最后一个元素，并返回这一元素 4
		lst_a.remove('new') #删除第一个指定值的元素,修改列表不返回值 
		lst_reverse()		#列表倒序
		lst_a.sort()		#就地排序
		sorted(lst) 		#排序的另一个用法
		lst_a.sort(key=len) #按长度排序
		lst_a.sort(reverse=True) #倒序排列
5)元组
	*不能修改
	24, #包含一个值的元组 (24,)
	tuple([1,2,3])	#(1,2,3)
	tuple('abc')	#('a', 'b', 'c')



字符串
------
1)设置字符串
	"{foo}{1}{bar}{0}".format(3,1,bar=2,foo=0) #结果 '0123'
	print("{pi!s}{pi!r}{pi!a}{num:f}{num:b}".format(pi="π",num=42))
	#上段结果为： π 'π' '\u03c0' 42.000000 101010
	b 将整数表示为二进制数
	c 将整数解读为Unicode码
	d 将整数视为十进制数进行处理，整数默认使用的说明符
	e 用科学表示法
	f 将小数表示为定点数
	g 自动在定点表示法和科学表示法之间做出判断
	o 将整数表示为八进制数
	s 保持字符串的格式不变 
	x 将整数表示为十六进制数并使用小写字母
	% 将数表示为百分比值
2)字符串方法
	< > ^ 
	center( , ) #居中,第二个参数为填充
	find() 		#返回字符串中第一个字符的索引
	join		#合并序列的元素，必须都是字符串
	lower()		#返回字符串的小写版本
	replace()	#替换
	split('\n')		#以换行符拆分
	strip()		#将字符串开头和末尾的空白删除
3)打印print
	print(a,b,sep="_")	#自定义分隔符
	print(a,end='')		#自定义结束符

字典 
----
键值对称为项，创建dict
1)基本操作
	创建方式：
		1.大括号包裹键值对:mydict={1:'a',2:'b'}
		2.工厂法创建：mydict=dict(([1,'a'],[2,'b']))
		3.字典内建法：mydict=dict.fromkeys([1,2,3,4,5],'a'),不能独立分配
	len(d) 	#返回键值对数
	d[k]	#返回与k相关联的值
	d[k]=v 	#将值v关联到键k
	del d[k]#删除键为K的项
	k in d 	#检查是否在内，查找的是键

2)函数
	format_map()#映射
	clear() 	#浅复制
	deepcopy()	#深复制
	fromkeys()	#创建新字典其中包含指定的键
	get()		#根据键得到值
	items()		#返回一个包含所有字典项的列表
	keys()		#返回字典视图，不包含重复的值
	pop()		#根据键删除该键值对
	popitem()	#随机删除键值对
	set_default	#获取指定键相关的值，若不存在则创建
	update()	#用一个字典中的项更新另一个字典
	values()	#返回一个由字典中的值组成的字典视图，可能包含重复值


抽象
----
放在函数开头的字符串成为文档字符串。
1)全局变量
	globals()['var'] #使用全局变量var
	global var #声明var为全局变量
2)递归
	递归函数通常包括两部分：
		基线条件(针对最小的问题)：满足这个条件时函数将直接返回一个值
		递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分。
	(1)幂
		def power(x,n):
			if n == 0:
				return 1
			else:
				return x * power(x,n-1)
	(2)阶乘
		def factorial(n):
			if n == 1:
				return 1
			else:
				return n * factorial(n-1)
	(3)二分查找
		def search(sequence, number, lower=0, upper=None)
		#得到的值为索引
			if upper is None:
				upper = len(sequence) - 1 #索引上限
			if lower == upper:
				# assert 其让它运行时崩溃，不如在它出现错误条件时就崩溃（返回错误）
			 	assert number == sequence[upper] 
			 	return upper
			 else: 
			 	middle = (lower + upper) // 2
			 	if number > sequence[middle]:
			 		return search(sequence, number, middle+1, upper)
			 	else:
			 		return search(sequence, number, lower, middle) 

类
---

__metaclass__ = type

class Person: #类
	def set_name(self, name): #属性
		self.name = name

	def get_name(self):
		return self.name

	def greet(self):
		print("Hello,{}.".format(self.name))

	def __passwod(self):  #私有方法
		self.passwd = 123456

a = Person()  #a为实例
b = Person()  #b实例
捕获错误
-------
查看实列


# zip() 函数
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]