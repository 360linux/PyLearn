#!/usr/bin/env python
#-*- coding: utf-8 -*-
# data = {
#     '北京':{
#         "昌平":{
#             "沙河":["oldboy","test"],
#             "天通苑":["链家地产","我爱我家"]
#         },
#         "朝阳":{
#             "望京":["奔驰","陌陌"],
#             "国贸":["CICC","HP"],
#             "东直门":["Advent","飞信"],
#         },
#         "海淀":{},
#     },
#     '山东':{
#         "德州":{},
#         "青岛":{},
#         "济南":{}
#     },
#     '广东':{
#         "东莞":{},
#         "常熟":{},
#         "佛山":{},
#     },
#
# }

import time
def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print  "the func run time  is %s" %(stop_time-start_time)
    return deco
@timer
def test1():
    time.sleep(1)
    print  'in the test1'

@timer
def test2(name,age):
    time.sleep(2)
    print  "test2:",name,age

test1()
test2("alex",22)