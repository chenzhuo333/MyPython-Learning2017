#coding=utf-8
# make sure you have install mysql with table sign_guest in it firstly, pymysql is must as well
from pymysql import cursors, connect
 
conn = connect(host='127.0.0.1',
               user='root',
               password='admin123456',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)
 
try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO sign_guest (realname,phone,email,sign,event_id,create_time) VALUES ("tom",18800110002,"tom@mail.com",0,1,NOW());'
         
        cursor.execute(sql)
         
        conn.commit()
         
        with conn.cursor() as cursor:
            sql="SELECT realname,phone,email,sign FROM sign_guest WHERE phone =18800110002"
            cursor.execute(sql)
            result = cursor.fetchone()
            print result
finally:
    conn.close()

# sql="SELECT realname,phone,email,sign FROM sign_guest WHERE phone =%s" % ('18800110002')
# 
# print sql