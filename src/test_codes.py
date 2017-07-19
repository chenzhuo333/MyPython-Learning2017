#coding=utf-8

#python给我们提供了一个包codecs进行文件的读取，这个包中的open()函数可以指定编码的类型：

import codecs
f = codecs.open('text.text','r+',encoding='utf-8')#必须事先知道文件的编码格式，这里文件编码是使用的utf-8
content = f.read()#如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误
f.write('你想要写入的信息')
f.close()