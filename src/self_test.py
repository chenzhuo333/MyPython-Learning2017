#coding=utf-8

class selftest:
    t2 = 400 #类参数
    
    def __init__(self): #如果要在类里面定义实例化参数，只能在__init__初始化方法中定义实例参数，否则在外面定义的都是类参数或者函数参数
#         t=0
        self.t=200 #实例参数

    def selffunc2(self):
        t1=300
        print self.t #实例参数
        print t1  #函数参数
    
    
if __name__ == '__main__':
    
    s = selftest()
#     print selftest.t #报错，因为t是实例参，不能通过类调用，只能通过实例s.t
#     print s.t1       #报错，因为t1是函数参，不能被实例调用，只能在类的函数中被调用
#     print s.t2       #报错，因为t2是类参，不能被实例调用，只能通过类.t2来调用
    print s.t
    print selftest.t2
    s.selffunc2()