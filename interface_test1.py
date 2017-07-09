'''
Created on May 3, 2017

@author: zhuo3.chen
'''
from interface_test import parentpage

class childpage(parentpage):
    
    url_c = "this url is child's"
#    def __init__(self, number_a,number_b,c):            #reload the __init__function from parent
#        self.a = number_a
#        self.b = number_b
#        print "init from child"
        
    def saygoodbye(self):
        print self.url_p



if __name__ == '__main__':
    
    cp = childpage(2,5)
    cp.saygoodbye()
    cp.sayhi()