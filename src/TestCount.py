'''
Created on Apr 26, 2017

@author: zhuo3.chen
'''

from Calculator import count

class TestCount():
    
    def test_add(self):
        j = count(2,3)
        sum = j.add()
        
#        m = count(3,4)
#        sum1=m.add()al
#        
#        print sum
#        print sum1
        
        try:
            assert(sum == 6),'the test is failed!'
        except AssertionError as msg:
            print msg
#        
#        
ta = TestCount()
ta.test_add()