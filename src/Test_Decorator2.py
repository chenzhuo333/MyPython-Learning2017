#coding=utf8
import logging

'''不带参装饰器'''
def use_logging(func):
    def wrapper(*args, **kwargs): #wrapper的参数传递给func的参数，请看Decorator3文件
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# def bar():
#     print('i am bar')
#     
# bar = use_logging(bar)
# bar()

@use_logging
def foo():
    print 'i am foo'
    
foo()

'''带参装饰器'''
def use_logging1(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
     
    return decorator
 
@use_logging1(level="warn")
def foo1(name='foo'):
    print("i am %s" % name)
 
foo1()

