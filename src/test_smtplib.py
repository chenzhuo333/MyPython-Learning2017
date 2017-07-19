#coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib

#发送邮件服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户/密码
user = 'bestlove662@163.com'
password = '2121221cz'

#发送邮箱
sender = 'bestlove662@163.com'

#接受邮箱
receiver = 'zhuo3.chen@symbio.com'

#邮件主题
subject = 'Python email test'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['subject'] = Header(subject,'utf-8')
msg['From'] = 'bestlove662@163.com'   #网易的邮箱验证了from和to信息，如果没有就是垃圾邮箱，发送失败
msg['To'] = 'zhuo3.chen@symbio.com'

#链接并发送邮件
smtp = smtplib.SMTP() #如果是SSL协议需要改成.SMTP_SSL()
smtp.connect(smtpserver,25)
# smtp.set_debuglevel(1)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()