# coding:utf-8
# 2019-2-1

"""
导致引用计数+1的情况
    对象被创建，例如a=23
    对象被引用，例如b=a
    对象被作为参数，传入到一个函数中，例如func(a)
    对象作为一个元素，存储在容器中，例如list1=[a,a]

导致引用计数-1的情况
    对象的别名被显式销毁，例如del a
    对象的别名被赋予新的对象，例如a=24
    一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
    对象所在的容器被销毁，或从容器中删除对象
"""
import gc

class A(object):
    pass

class B(object):
    pass

def foo():
    collected = gc.collect()
    print("start gc.collect(): ", collected)
    a = A()
    b = B()
    a.b = b 
    b.a = a 

    del a 
    del b
    collected = gc.collect()
    print("end gc.collect(): ", collected)
    grbage = gc.garbage()
    print("gc.garbage(): ", garbage)

if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK) #设置gc模块的日志
    foo()