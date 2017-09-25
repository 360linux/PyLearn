#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-15 上午11:54
# @Author  : Liping
# @Site    : 
# @File    : traceback-ex.py
# @Software: PyCharm


import sys, traceback

try:
    s = raw_input("input>>>:")
    int(s)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'lineno': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__,
        'message': exc_value.message,
    }

    del (exc_type, exc_value, exc_traceback)
    print traceback_details
    f = file('test1.txt', 'a')
    f.write("%s %s %s %s %s\n" % (
    traceback_details['filename'], traceback_details['lineno'], traceback_details['name'], traceback_details['type'],
    traceback_details['message'],))
    f.flush()
    f.close()