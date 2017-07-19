#coding=utf-8

class F:
    lang ="java"      #类变量，只能通过调用类来使用
    def __init__(self, lang):
        self.lang = lang   #实例变量，只能通过实例化类，然后使用
    
    @classmethod  #类装饰器，表明这是一个类方法， 用来调用类属性，不需要实例化类
    def get_class_attr(cls):
        return cls.lang
    
print F.lang

r=F.get_class_attr()

print r

G=F('python')
print G.lang

print dir(F)
print G.__dict__