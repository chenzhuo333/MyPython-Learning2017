# coding=utf8

import json

data =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } #定义一个字典
myjson = json.dumps(data)
print myjson
 
text = json.loads(myjson)
 
print text['a']
 
 
data1 =  [{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }]#定义一个列表字典
 
myjson1 = json.dumps(data1)
print myjson1
text1 = json.loads(myjson1)
print text1[0]['a']