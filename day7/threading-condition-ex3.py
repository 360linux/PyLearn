#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-14 下午11:15
# @Author  : liping
# @File    : threading-condition-ex3.py

import threading


def run(n):
    con.acquire()
    con.wait()
    print("run the thread: %s" % n)
    con.release()


if __name__ == '__main__':

    con = threading.Condition()
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()

    while True:
        inp = input('>>>')
        if inp == 'q':
            break
        con.acquire()
        con.notify(int(inp))
        con.release()