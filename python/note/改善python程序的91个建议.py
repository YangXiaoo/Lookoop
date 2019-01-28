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