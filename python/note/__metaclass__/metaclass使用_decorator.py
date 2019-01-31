from types import FunctionType  
  
def login_required(func):  
    print 'login check logic here'  
    return func  
  
  
class LoginDecorator(type):  
    def __new__(cls, name, bases, dct):  
        for name, value in dct.iteritems():  
            if name not in ('__metaclass__', '__init__', '__module__') and\  
                type(value) == FunctionType:  
                value = login_required(value)  
  
            dct[name] = value  
        return type.__new__(cls, name, bases, dct)  
  
  
class Operation(object):  
    __metaclass__ = LoginDecorator  
  
    def delete(self, x):  
        print 'deleted %s' % str(x)  
  
  
def main():  
    op = Operation()  
    op.delete('test')  