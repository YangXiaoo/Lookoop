
# coding: utf-8

# In[1]:


# 28. .format使用方式
# (1) 使用位置符号
print("my name is {0}, {1:,} years old in hex is {1:#x}, in oct is {1:#}".format("yauno", 24))


# In[5]:


# (2) 使用名称
print("my name is {name}, {year} years old".format(name='yauno', year=24))


# In[6]:


# (3) 通过属性
class Test():
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def __str__(self):
        return "my name is {self.name}, {self.year} years old.".format( =self)


# In[7]:


str(Test('yauno', 24))


# In[8]:


# (4) 格式化元组
tup = ('yauno', 24)
print("my name is {0[0]}, {0[1]} years old.".format(tup))


# In[21]:


# 35. stacticmethod 与 classmethod区别
# 两者都是给类使用的

import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    @staticmethod
    def now(): #用Date.now()的形式去产生实例,该实例用的是当前时间
        t=time.localtime() #获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回
    
    @staticmethod
    def tomorrow():#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)


# In[22]:



a=Date('1987', 11, 27) #自己定义时间
b=Date.now() #采用当前时间
c=Date.tomorrow() #采用明天的时间

print(a.year,a.month,a.day)
print(b.year,b.month,b.day)
print(c.year,c.month,c.day)


# In[25]:


import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    @classmethod
    def now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)
    
class TestDate(Date):
    def __str__(self):
        return 'year: {self.year}, month: {self.month}, day: {self.day}'.format(self=self)


# In[26]:


test = TestDate.now()
print(test)


# In[37]:


# 37. sorted 与 sort()的使用
from operator import itemgetter

test_data = [['a',1,'aa'], ['b', 2, 'bb']]
func = itemgetter(1, 0)
func(test_data)


# In[8]:


# 55. __init__不是构造方法
class Test(object):
    def __new__(cls, x, y):
        print("__new__")
        print(cls)
        return super(Test, cls).__new__(cls)
    
    def __init__(self, x, y):
        print("\n__init__")
        self.x = x
        self.y = y
        


# In[9]:


t = Test(2, 3)


# In[23]:


class A(object):
    def __init__(self, x=2):
        print("A.__init__")
        self.x = x

class B(A):
    def __init__(self, x=None):
        super(B, self).__init__() # 继承父类私有变量
        print("B.__init__")
        self.y = x
        


# In[27]:


t = B()
t.x


# In[29]:


# 工厂模式
class shape(object):
    def __init__(object):
        pass
    def draw(self):
        pass
    
class Triangle(shape):
    def __init__(self):
        pass
    def draw(self):
        print("triangle")
        
class Circle(shape):
    def __init__(self):
        pass
    def draw(self):
        print("circle")
        
class ShapeFactory(object):
    shapes = {'triangle':Triangle, 'circle':Circle}
    
    def __new__(cls, name):
        if name in ShapeFactory.shapes.keys():
            print("creating %s" % name)
            return ShapeFactory.shapes[name]()
        else:
            print("creating shape.")
            return shape()


# In[30]:


t = ShapeFactory('circle').draw()


# In[31]:


ShapeFactory('xxx').draw()


# In[32]:


locals()


# In[40]:


# 56. 理解名字查找机制--变量域
# 变量搜索方向：Local -> Enclosed -> Global -> Built-in
def test(arg=None):
    global v_1
    v_1 = 'a'
    def inner():
        v_1 = 'b'
        v_2 = 'c'
        print(v_1)
    inner()
    print(v_1)
    # print(v_2)


# In[41]:


test()


# In[45]:


def foo(arg):
    a = arg
    def bar():
        nonlocal a
        b = a * 2
        a = b * 2
        print(a)
    return bar


# In[46]:


t = foo(1)()


# In[50]:


# 57. 为什么需要self参数

def foo(arg):
    return arg.x + arg.y

class Test(object):
    def __init__(self, x_p, y_p):
        self.x = x_p
        self.y = y_p
        


# In[51]:


Test.foo = foo


# In[52]:


t = Test(1,2)
t.foo()


# In[53]:


Test.__dict__


# In[58]:


class MyClass(object):
#         def __init__(self):
#             pass
       def my_func(self):
           pass


# In[59]:


MyClass.my_func


# In[61]:


MyClass.__dict__['my_func']


# In[60]:


t = MyClass()
t.my_func


# In[62]:


dir(t)


# In[47]:


# 62. __metaclass__
"""
1. 你可以自由的、动态的修改/增加/删除 类的或者实例中的方法或者属性

2. 批量的对某些方法使用decorator，而不需要每次都在方法的上面加入@decorator_func

3. 当引入第三方库的时候，如果该库某些类需要patch的时候可以用metaclass

4. 可以用于序列化(参见yaml这个库的实现，我没怎么仔细看）

5. 提供接口注册，接口格式检查等

6. 自动委托(auto delegate)

# http://blog.jobbole.com/21351/
# https://jianpx.iteye.com/blog/908121
"""
class Metaclass(type):
    def __new__(cls, name, bases, dct):
        print( 'HAHAHA')
        dct['a'] = 1
        return type.__new__(cls, name, bases, dct)
__metaclass__ = Metaclass

print( 'before Create OBJ')
class OBJ(object):
    pass
print('after Create OBJ')
print( OBJ.a)


# In[39]:


def ma(cls):  
    print( 'method a')  
  
def mb(cls):  
    print( 'method b')  
  
method_dict = {  
    'ma': ma,  
    'mb': mb,  
}  
global method_dict

class DynamicMethod(type):  
    def __new__(cls, name, bases, dct): 
        print(name)
        if name[:3] == 'Abc':  
            dct.update(method_dict)  
            print(dct)
        return type.__new__(cls, name, bases, dct)  
  
    def __init__(cls, name, bases, dct):  
        print(name)
        super(DynamicMethod, cls).__init__(name, bases, dct)  
# __metaclass__ = DynamicMethod  
  
class AbcTest(object):  
    __metaclass__ = DynamicMethod  
    def mc(self, x):  
        print (x * 3 ) 
  
class NotAbc(object):  
    __metaclass__ = DynamicMethod  
    def md(self, x):  
        print( x * 3)  

MyClass = type('MyClass', (), method_dict)

def main():  
    a = AbcTest()  
    a.mb()
    a.ma()  
    a.mc(3)
  
    b = NotAbc()  
    print( dir(b))  


# In[42]:


t = MyClass()
t.mb()


# In[49]:


class Mymeta(type):
    def __new__(cls, name, bases, dct):
        print("__new__ ", name)
        return super(Mymeta, cls).__new__(cls, name, bases, dct)


# In[50]:


class A(object):
    pass


# In[51]:


t = A()


# In[2]:


# 66. Python的生成器
def foo(arg=None):
    print("start foo.")
    try:
        while True:
            try:
                arg = yield arg # 第二次调用的时候会返回 None
            except Exception as e:
                print(str(e))
    finally:
        print("end foo")
                


# In[3]:


g = foo(1)


# In[5]:


g.__next__()


# In[11]:


g.send(2)


# In[12]:


g.send(3)


# In[13]:


g.close()


# In[14]:


# 69. 对象的管理与垃圾回收
import gc


# In[15]:


print(gc.isenabled())


# In[16]:


gc.get_threshold()

