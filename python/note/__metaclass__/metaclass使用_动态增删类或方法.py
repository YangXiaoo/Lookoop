# coding:utf-8
class Mymeta(type):
    def __new__(cls, name, bases, dct):
        print("__new__ ", name)
        return super(Mymeta, cls).__new__(cls, name, bases, dct)

class A(object):
	__metaclass__ = Mymeta
 
t = A()

def ma(cls):  
    print( 'method a')  
  
def mb(cls):  
    print( 'method b')  
  
method_dict = {  
    'ma': ma,  
    'mb': mb,  
}  

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
__metaclass__ = DynamicMethod  
  
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

if __name__ == '__main__':
	main()