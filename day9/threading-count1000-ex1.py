#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-3 下午7:07
# @Author  : Aries
# @Site    : 
# @File    : threading-count1000-ex1.py
# @Software: PyCharm

import threading
import  time
num=0
lock=threading.Lock()
class Timer(threading.Thread):
    def __init__(self,count,interval):
        # super(Timer,self).__init__(self)
        threading.Thread.__init__(self)
        self.interval=interval
        self.count=count
    def run(self):
        global num
        while num<self.count:
            lock.acquire()
            # if num>self.count:
            #     lock.release()
            #     break
            num+=1
            print "Thread name:%s,%d" %(self.getName(),num)
            lock.release()
            time.sleep(self.interval)
if __name__=='__main__':
    t1=Timer(100,5)
    t2=Timer(100,5.5)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
