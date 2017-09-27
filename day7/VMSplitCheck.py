#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-22 下午3:31
# @Author  : liping
# @File    : VMSplitCheck.py
import re
import libvirt
from credentials import get_nova_creds
from novaclient import client
from multiprocessing import Pool,Queue

pattern = re.compile(r'node-\d\.domain.tld')
q=Queue()
HypervisorHostname = []
creds = get_nova_creds()
nova = client.Client('2', **creds)
for i in nova.hypervisors.list():
    match = pattern.search(i.hypervisor_hostname)
    if match:
        HypervisorHostname.append(match.group())

HyperDict = {}.fromkeys(HypervisorHostname, [])

def getVM(node):
    try:
        virtcon=libvirt.open("qemu+ssh://%s/system" %node)
    except libvirtError,e:
        print "wrong to connect"
    for id  in virtcon.listDomainsID():
        vminfo=virtcon.lookupByID(id)
        q.put(vminfo.name())

InstanceNameList=[]
while not q.empty():
    InstanceNameList.append(q.get())

for 
