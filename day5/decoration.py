#!/usr/bin/env python
#-*- coding:utf-8 -*-

# def fib(max):
#     n,a,b=1,1,2
#     while n<max:
#         yield b
#         a,b=b,a+b
#         n +=1
# g=fib(16)
# print g
#
# print g.next()
# g.send(6)
# print g.next()
# print '休息一会'
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()


__author__ = "Alex Li"

# import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        baozi = yield
#
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
# c = consumer("ChenRonghua")
# c.next()
#
# #b1= "韭菜馅"
# #c.send(b1)
# #c.next()
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.next()
#     c2.next()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了1个包子,分两半!")
#         c.send(i)
#         c2.send(i)
#
# producer("alex")


import  shutil

import  zipfile
z=zipfile.ZipFile('buy.zip','w')
try:
    z.write('/home/liping/py/buy.py')
except OSError,e:
    print  'openfile error',e
z.close()

