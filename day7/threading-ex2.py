#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
import random

def threadfunc(n):
    semaphore.acquire()
    time.sleep(random.random() * 10)
    print "run the thread:%s" %n
    semaphore.release()




if __name__=="__main__":
    num = 0
    semaphore=threading.BoundedSemaphore(15)
    for i in xrange(20):
        t=threading.Thread(target=threadfunc,args=(i,))
        t.start()
