# coding:utf-8
# 2019-2-15

# https://www.cnblogs.com/wangyongsong/p/6750454.html
# 编写类时需要采用很多不同的方式来创建实例，而我们只有一个__init__函数，此时静态方法就派上用场了

import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    @staticmethod
    def now(): # 用Date.now()的形式去产生实例,该实例用的是当前时间
        t = time.localtime() # 获取结构化的时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday) # 新建实例并且返回
    
    @staticmethod
    def tomorrow(): # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

a = Date('1987', 11, 27) # 自己定义时间
b = Date.now() # 采用当前时间
c = Date.tomorrow() # 采用明天的时间

print(a.year, a.month, a.day)
print(b.year, b.month, b.day)
print(c.year, c.month, c.day)