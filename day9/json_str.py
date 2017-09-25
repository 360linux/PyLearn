#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午3:19
# @Author  : Liping
# @Site    : 
# @File    : json_str.py
# @Software: PyCharm
import json
a={'br-ex':'172.16.20.3'}
b=str(a)
json.loads(b,encoding="utf-8")