# coding=utf8

'''--------------------元祖列表------------------'''
x = [('hh','aa'),('bb','dd'),('cc','ee')]
     
for a,b in x: #列表元祖字典集合等对象都可以通过这种循环迭代，跟字典的item()方法类似，item就是将字典转换成元祖列表(其中一种mapping)罢了。
    print a,b
         
print x[0][0] #也可以用这种方式访问
   
    
'''#---------------------字典列表-----------------'''
x2 = [{'hh':'aa','ww':'hha'},{'bb':'dd','tt':'tete'},{'cc':'ee','yy':'mm'}]
for i in range(len(x2)): #方法1，打印所有key value的值
    for k,y in x2[i].items():
        print k+':'+y
            
for a,b in x2:#由于里面存的字典，只会打印key,不会打印value
    print a,b
'''# #---------------------列表元祖-----------------'''
x3=(['a','b','h'],['c','d','x'])
     
for a,b,c in x3: #列表元祖也可以用这种方法，有多少值，就需要多少个参数在for循环里去接收
    print a,b,c
 
'''#-------------------列表------------------'''
   
x8=['aaa','bbb','ccc','ddd','eee','fff','ggg']
   
for a in x8: 
    print a
     
'''#--------------------------字典---------------------------'''
x10 ={'hh':'aa','ww':'hha','bb':'dd','tt':'tete'}
for i in x10:
    print i #只打印key
x9={'hh':'aa','ww':'hha'},{'bb':'dd','tt':'tete'},{'cc':'ee','yy':'mm'}#默认是数组
for a,b in x9:#只打印key,和上面的字典同理
    print a,b
      
'''#-------------------------元祖--------------------------'''
      
x10='a','b','c' #如果没有(),python默认是定义为元祖
  
  
#---------------------集合-----------------
x1={'a','b','c','d'}
   
print dir(x1) #也是可迭代的，但是没有index属性，因此集合没有索引
# print x1[0] #由于没有索引，会报错

