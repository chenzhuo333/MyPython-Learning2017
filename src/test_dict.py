# coding=utf8

x3=(['a','b'],['c','d'])
   
x4= dict(x3)#用dict方法将列表元祖转换成字典
print x4

x5=[('a','b'),('d','e')]
x6=dict(x5) #也可以将元祖列表转换成字典

x7=['a','b','c','d'] 
x8=dict(x7) #报错，传入的对象不是mapping对象(一对一)


x9=[('a','b','f'),('d','e','w')]
x10=dict(x9)#报错，传入的对象不是mapping对象(一对一)