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
    time.sleep(random.randint(1,2))
    test1.append(n)
    sem.release()


sem=threading.BoundedSemaphore(2)
for i in range(10):
    t=threading.Thread(target=testfuc1,args=(i,))
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()
print  test1