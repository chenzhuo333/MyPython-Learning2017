def foo():#当在函数外想使用函数内的变量，就可以在函数中再定义一个函数用来返回函数的变量并返回这个内嵌函数，这个内嵌函数就是闭包
    a = 3
    def bar():
        return a
    return bar
if __name__=='__main__':
    f = foo()
    print f()
# 
# def sayhi(func,b):
#     
#     def sayhi2(a):
#         
#         print "i'm sayhi2"+str(a)
#         func(b)
#         
#     return sayhi2
#         
#         
# 
# 
# def saihi3(ss):
#     print "i'm sayhi3"+str(ss)
#     
#     
# 
# 
# if __name__=='__main__':
#     b = sayhi(saihi3,"zhuo")
#     p = b("chen")
    

def ChangeInt( a ):
    a = 10
    return a
b = 2
a1=ChangeInt(b)
print b
print a1