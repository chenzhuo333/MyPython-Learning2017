#coding=utf-8

from selenium.webdriver import Remote

lists = {'http://127.0.0.1:4444/wd/hub':'firefox',  #若想用其他浏览器，需要下载对应的webdriver
         'http://127.0.0.1:5555/wd/hub':'firefox'
        }

for host,browser in lists.items():
    
    print host, browser
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform':'ANY',
                                          'browserName':browser,
                                          'version':'',
                                          'javascriptEnabled':True
                                          
                                          })
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys("remote")
    driver.find_element_by_id('su').click()
    driver.quit()