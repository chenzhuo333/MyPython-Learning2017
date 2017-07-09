# coding=utf8

#--------------------元祖列表------------------
x = [('hh','aa'),('bb','dd'),('cc','ee')]
 
 
print dir(x) #里面有__iter__说明是可迭代的

x1=iter(x) #用iter方法将一个可迭代的对象转换为迭代器，就可以用next()方法进行迭代，python3中是__next__
print x1.next()
