#coding=utf-8
class A:
    x = 7   # this property is not changed 
    
    
B = A()
B.x+=1
print B.x #实例对象里的x加1
print A.x #类对象不变

del B.x #删除实例对象的x后， 实例对象的x变为类对象里的x值

print B.x



class C:
    y = [1,2,3] # this property is allowed to change，因为列表对象是可以迭代的
    
D = C()
D.y.append("4")

print D.y
print C.y


class E:
    def printhi(self):
        print "hi this is classE"
        
F=E()        
F.printhi()


class F:
    lang ="java"      #类变量，只能通过调用类来使用
    
    def __init__(self, lang):
        self.lang = lang   #实例变量，只能通过实例化类，然后使用
        
    
print F.lang

G=F('python')
print G.lang
    