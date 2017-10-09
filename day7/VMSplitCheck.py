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
from collections import Counter,defaultdict

q=Queue()

def getHypervisor():
    HypervisorHostname = []
    pattern = re.compile(r'node-\d\.domain.tld')
    creds = get_nova_creds()
    nova = client.Client('2', **creds)
    for i in nova.hypervisors.list():
        match = pattern.search(i.hypervisor_hostname)
        if match:
            HypervisorHostname.append(match.group())
    return  HypervisorHostname

def getVM(node):
    try:
        virtcon=libvirt.open("qemu+ssh://%s/system" %node)
    except libvirtError,e:
        print "wrong to connect"
    for id  in virtcon.listDomainsID():
        vminfo=virtcon.lookupByID(id)
        q.put((node,vminfo.name()))

def getVMList():
    InstanceNameList=[]
    # a=getHypervisor()
    # HyperDict = {}.fromkeys(a, [])
    HyperDict=defaultdict(list)
    while not q.empty():
        node,vm=q.get()
        InstanceNameList.append(vm)
        HyperDict[node].append(vm)
    return InstanceNameList,HyperDict

def VMSplitCheck(instancelist,nodedict):
    SplitList=[]
    SplitDict=defaultdict(list)
    c=Counter(instancelist)
    for k,v in c.iteritems():
        if v>=2:
            SplitList.append(k)
    if len(SplitList)==0:
        print "no split vm"
    else:
       for i in SplitList:
           for k,v in nodedict.iteritems():
               if i in v:
                   SplitDict[i].append(k)
    return SplitDict

def main():
    hypername=getHypervisor()
    p=Pool()
    for i in hypername:
        p.apply_async(getVM,args=(i,))
    p.close()
    p.join()

    inslist,hydict=getVMList()
    vmsplit=VMSplitCheck(inslist,hydict)
    print vmsplit



if "__name__" =="__main__":
    main()




