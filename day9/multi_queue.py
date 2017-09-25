#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午10:44
# @Author  : Liping
# @Site    : 
# @File    : multi_queue.py
# @Software: PyCharm
import Queue
from multiprocessing import Pool,Queue
# q=Queue.Queue()
import time
q=Queue()
nodelist=[]
def put(i):
    print i
    time.sleep(1)
    q.put(i)

def main():
    p=Pool(2)
    for j in xrange(20):
        p.apply_async(put,args=(j,))
    p.close()
    p.join()

    while not q.empty():
        a=q.get()
        nodelist.append(a)
if __name__ == '__main__':
    main()
    print  nodelist