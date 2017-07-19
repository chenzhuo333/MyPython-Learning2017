#coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
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

#发送的附件
sendfile = open("/Users/symbio/Documents/公司记录.txt","r").read()

#定义附件的格式
att = MIMEText(sendfile,'base64','utf-8') 
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename="log.txt"'

msgRoot = MIMEMultipart('related') #发送附件的邮件模块
msgRoot['Subject'] = subject
msgRoot['From'] = 'bestlove662@163.com'   #网易的邮箱验证了from和to信息，如果没有就是垃圾邮箱，发送失败
msgRoot['To'] = 'zhuo3.chen@symbio.com'
msgRoot.attach(att)

#链接并发送邮件
smtp = smtplib.SMTP() #如果是SSL协议需要改成.SMTP_SSL()
smtp.connect(smtpserver,25)
# smtp.set_debuglevel(1)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()