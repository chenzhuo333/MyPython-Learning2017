#coding=utf-8

import threading

import time

def music(musicname,loop):
    for i in range(loop):
        print ("I was listening to %s! %s" %(musicname,time.ctime()))
        time.sleep(2)
        
        
def movie(moviename,loop):
    for i in range(loop):
        print ("I was looking the %s! %s" %(moviename,time.ctime()))
        time.sleep(3)
        
        
threads = []

t1 = threading.Thread(target=music,args=('阿凡达',2))
# t1.start()
threads.append(t1)

t2 = threading.Thread(target=movie,args=('爱情买卖',2))
threads.append(t2)
# t2.start()
t3 = threading.Thread(target=movie,args=('nice',2))


if __name__ == "__main__":
    
    for t in threads:
        t.start()
#        t.join() 
    for t in threads:
        t.join()
#     t1.start()
#     t2.start()
    print ("end time is %s" %(time.ctime()))