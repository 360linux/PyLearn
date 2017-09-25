#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-8 下午8:38
# @Author  : Liping
# @Site    : 
# @File    : a.py
# @Software: PyCharm
import  subprocess
try:
    service_result = subprocess.check_output("dfff", shell=True)
    print "this is:",service_result
    print type(service_result)
except subprocess.CalledProcessError, e:
    #  service_result=e
    print "liping:",e

    type(e)
