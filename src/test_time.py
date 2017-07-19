# coding=utf8
import time
now_time = time.time()    # 例：1466426831
print now_time
server_time = str(now_time).split('.')[0]
print server_time
# 获取时间差
time_difference = int(server_time) - int(now_time)
print time_difference
if time_difference >= 60 :
    print "timeout"
    
else:
    print "no timeout"