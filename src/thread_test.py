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
    
'''
有时我们需要的是，子线程运行完，才继续运行主线程，这时就可以用join方法（在线程启动后面）；

但是有时候我们需要的是，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon(true)方法 (在线程启动前面) 
默认是false，可以不用写出来
'''