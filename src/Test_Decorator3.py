#coding=utf8

import logging

'''闭包'''
def A(func):
    def wrapper(*args, **kwargs): #wrapper的参数传递给func的参数
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@A
def B(a,b):
    print "a is:"+str(a)
    print "b is:"+str(b)
    
B(2,3)   #加了装饰器的函数，调用函数就等于调用装饰器函数，因此参数也是传给了装饰器返回的wrapper对象，最后又传给了B自己

#调用方式等价于：

# a=A(B)
# a(2,3)