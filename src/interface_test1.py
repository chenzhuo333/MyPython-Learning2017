#coding=utf8
from interface_test import parentpage

class childpage(parentpage): #子类实例将拥有父类的一切属性，包括类属性和实例属性
    
    url_c = "this url is child's"
#    def __init__(self, number_a,number_b,c):            #reload the __init__function from parent
#        self.a = number_a
#        self.b = number_b
#        print "init from child"
        
    def saygoodbye(self):
        print self.url_p #url_p是类变量，通过类和实例都可以调用，此处是通过实例调用



if __name__ == '__main__':
    
    cp = childpage(2,5)#因为没有重构构造器，因此调用父类的构造器。
    cp.saygoodbye()
    cp.sayhi()
    print cp.a