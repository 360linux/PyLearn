#!/usr/bin/env python
# -*- coding:utf8 -*-

import threading, time

def run(n):
    semaphore.acquire()
    print("begin to run the thread: %s" % n)
    time.sleep(6)
    print "finish run:%s" %n
    semaphore.release()


if __name__ == '__main__':

    num = 0
    semaphore = threading.BoundedSemaphore(10)  # 最多允许5个线程同时运行
    for i in xrange(50):
        t = threading.Thread(target=run, args=(i,))
        t.start()