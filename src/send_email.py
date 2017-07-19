'''
Created on May 2, 2017

@author: zhuo3.chen
'''

from smtplib import SMTP

sm = SMTP()
sm.connect('imap.symbio.com', '587')
sm.login('zhuo3.chen@symbio.com', 'Qwert,%2002')
sm.sendmail('zhuo3.chen@symbio.com', 'chenzhuo333@qq.com', 'this is a test email from python')
sm.quit()
