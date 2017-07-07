#coding=utf-8
import os
print __file__#__file__返回当前py文件的绝对路径，包含py文件
dir = os.path.dirname(__file__)#os.path.dirname返回某路径的目录(上一层)
print dir

dir1 = os.path.dirname(os.path.dirname(__file__))#连续使用的话就是上上层目录
print dir1

dir2 = os.path.abspath(__file__)
print dir2