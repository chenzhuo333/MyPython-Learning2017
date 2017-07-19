#coding=utf-8

import threading

import time

def music(musicname):
    time.sleep(5)
    print ("I was listening to music: %s" %(musicname))
#     time.sleep(5)
        
        
def movie(movicename):
    print ("I was looking the movie:%s" %(movicename))
        
        
threads = []

t1 = threading.Thread(target=music,args=('阿凡达',))#args参数必须是元祖形式，因此只有一个参数时需要加个逗号表示元祖
# t1.start()
threads.append(t1)

t2 = threading.Thread(target=movie,args=('爱情买卖',))
threads.append(t2)


if __name__ == "__main__":
    

    for t in threads:
#       t.setDaemon(False)# 默认非守护线程（可以不写），主线程结束后，子线程继续运行，直到结束
#       t.setDaemon(True) # 设置成守护线程，主线程结束后，不管子线程是否完成，一起退出
        t.start()
#       t.join() #若join加在单个线程启动的后面，那么就会一个一个线程的跑
    for t in threads:
        t.join() #若join单独写一个循环，那么子线程会同时启动，只是主线程要等待所有子线程结束才能执行
#     t1.start()
#     t2.start()
    print ("end time is %s" %(time.ctime()))
    
'''
有时我们需要的是，子线程运行完，才继续运行主线程，这时就可以用join方法（在线程启动后面）；

但是有时候我们需要的是，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon(true)方法 (在线程启动前面) 
默认是false，可以不用写出来
'''