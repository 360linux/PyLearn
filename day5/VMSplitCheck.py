#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-20 下午8:29
# @Author  : Liping
# @Site    : 
# @File    : VMSplitCheck.py
# @Software: PyCharm

import  commands
from credentials import get_nova_creds
from novaclient import  client
import  libvirt


creds=get_nova_creds()
nova=client.Client("2.0",**creds)
HyperList=nova.hypervisors.list()
HyperHostname=[]
for i in HyperList:
    HyperHostname.append(i.hypervisor_hostname)

