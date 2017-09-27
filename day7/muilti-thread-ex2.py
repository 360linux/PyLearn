#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-7 下午11:19
# @Author  : liping
# @File    : muilti-thread.py

import threading
import time
import random

test1=[]
thread_list=[]
def testfuc1(n):
    sem.acquire()
    print i
    n1=random.randint(1,3)
    print "thread %s being to sleep %d s" %(t.getName(),n1)
    time.sleep(n1)
    test1.append(n)
    sem.release()

sem=threading.BoundedSemaphore(5)
for i in range(10):
    t=threading.Thread(target=testfuc1,args=(i,))
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()
print  test1