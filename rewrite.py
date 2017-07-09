'''
Created on May 9, 2017

@author: zhuo3.chen
'''
class A(object):
    def __init__(self, name):
        self.name=name
        print "name:", self.name
    def getName(self):
        return 'A ' + self.name

class B(A):
    def __init__(self, name): #重写了父类的构造函数
        super(B, self).__init__(name) # 用super调用父类的构造函数就可以继续舒勇父类的构造函数
        print "hi"
        self.name =  name
    def getName(self):
        return 'B '+self.name
    
if __name__=='__main__':
    b=B('hello')
    print b.getName()