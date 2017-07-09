#coding=utf-8
from Calculator import count
import unittest
class testcount(unittest.TestCase):
    def setUp(self):
        print "start to test"
    @unittest.skipIf(3>2,'pass')   
    def test_add(self):
        j = count(2,3)
        self.assertEqual(j.add(), 6, "test failed")
        
    def tearDown(self):
        print "end"
    
#    ut = unittest.TestLoader
#    ut.discover(start_dir, pattern, top_level_dir)
        
#    unittest.defaultTestLoader.discover(start_dir, pattern, top_level_dir)  
        
if __name__ =='__main__':
    unittest.main()  #执行当前unittest测试用例