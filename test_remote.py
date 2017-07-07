#coding=utf-8

from selenium.webdriver import Remote
import time
from selenium.webdriver.common.by import By

driver = Remote(command_executor = 'http://127.0.0.1:4444/wd/hub',
                desired_capabilities={'platform':'ANY',
                                      'browserName':'firefox',
                                      'version':'',
                                      'javascriptEnabled':True
                                      }                        
                )

driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#driver.find_element_by_id('kw').send_keys("remote")
#driver.find_element_by_id('su').click()
driver.find_element(By.ID,"kw").send_keys("remote")
driver.find_element(By.ID,"su").click()

time.sleep(3)
driver.quit()