#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-4 下午3:57
# @Author  : Liping
# @Site    : 
# @File    : ceph-ex1.py
# @Software: PyCharm
import rados

# c = rados.Rados(conffile='/home/liping/ceph.conf', conf=dict(keyring='/home/liping/ceph.client.admin.keyring'))
# c.connect()
c = rados.Rados(conffile='/home/liping/ceph.conf', conf=dict(keyring='/home/liping/ceph.client.admin.keyring',mon_initial_members="192.168.15,2"))
c.connect()