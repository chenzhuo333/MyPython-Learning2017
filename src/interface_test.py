'''
Created on May 3, 2017

@author: zhuo3.chen
'''
class parentpage():
    url_p="'this url is parent's"
    def __init__(self, number_a,number_b):
        self.a = number_a
        self.b = number_b
        print "init from parent"
        
    def sayhi(self):
        print "please notice that "+self.url_c