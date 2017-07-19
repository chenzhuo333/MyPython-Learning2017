#coding=utf8
'''
Created on May 3, 2017

@author: zhuo3.chen
'''
class parentpage():
    url_p="'this url is parent's" #类参数,类函数需要用@classmethod装饰器
    def __init__(self, number_a,number_b):
        self.a = number_a  #实例参数
        self.b = number_b
        print "init from parent"
        
    def sayhi(self):
        print "please notice that "+self.url_c