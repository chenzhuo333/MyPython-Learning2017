
import multiprocessing

def printhi():
    print "hi"
    


t=multiprocessing.Process(target=printhi,args='')

if __name__=='__main__':
    t.start()