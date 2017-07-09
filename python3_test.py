#coding=utf-8
import os
if 3!=2:
    print '1'
    
for i in range(5):
    print i
    
data = [{'a':123,'b':321}] #字典列表
print data[0]['a']

data1 = [('chen',123),('zhuo',321)]

print data1[0][1]

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')

print base_dir