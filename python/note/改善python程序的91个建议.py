# coding=utf-8
# 2019-1-28
# 改善python程序的91个建议

# %占位符
value = {'name':'yauno', 'sex':'man'}
print('name %(name)s , sex %(sex)s' % value)
# str.format


# ' 与 "的区别
print('"test"')
print("\"test\"")

# 常量的管理


# 12: 不推荐使用type来进行检查
# isinstance(object, classoinfo)
print(isinstance('string', str))


# 13. 涉及除法运算时，尽量先将操作数转换为浮点类型再做运算

# 14. 警惕使用eval()的安全漏洞

# 17. unicode
# 在2.6之后可以使用 import_unicode_literals自动将定义的普通字符识别为Uicode字符串, 这样字符串的行为将保持和pythoh3一致

# 19. import
# (1) 命名空间的冲突
# (2) 循环嵌套导入问题： 不使用 from .. import ... 直接使用 import ...


# 21. ++i 与 i += 1

# 23. else
# (1)
def print_prime(n):
	for i in range(n):
		for j in range(2, i):
			if i % j == 0:
				break # 这里终止后不执行后面打印操作
		else:
			print("%s is prime." % i) # 内嵌for 循环正常执行完后执行打印操作

print_prime(10)


# (2)
try:
	pass
except:
	pass
else:
	pass
finally:
	pass


# 25. finally
def finally_test(a):
	try:
		print("\ntesting...")
		if a <= 0:
			raise ValueError("data can not be negative.")
		else:
			return a
	except ValueError as e:
		print("%s" % e)
	finally:
		print("end")
		return -1

for i in range(-1, 2):
	ret = finally_test(i) # 最后返回永远都是-1, 因为返回a之前要执行finall, 而finally直接就返回了-1
	print("return value: %s" % ret)