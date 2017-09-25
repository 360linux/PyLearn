#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-15 下午3:38
# @Author  : Liping
# @Site    : 
# @File    : get_ip.py
# @Software: PyCharm

import paramiko
import commands
from multiprocessing import Pool,Queue
import re
import os
# import  json
node_list=[]
problem_ip=[]
ip_dict={
    "br-mgmt":[],
    "br-ex":[],
    "br-storage":[],
    "br-storagepub":[],
    "br-roller":[]
}
q=Queue()
hosts_file='/tmp/hosts'
p1=re.compile(r'node-[0-9]{1,}')
with open(hosts_file,'r') as f:
    for i in f:
        # print i
        node=p1.search(i)
        if node:
            node_list.append(node.group())
        # print node_list
def get_ip(node):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshkey=os.path.join(os.environ['HOME'],'.ssh','id_rsa')
    pkeyfile=paramiko.RSAKey.from_private_key_file(sshkey)
    ssh.connect(hostname=node,username='root',port=22,pkey=pkeyfile)
    com='ip a |grep global|grep -w  -E  "br-mgmt|br-roller|br-storagepub|br-storage|br-ex"'
    try:
        stdin,stdout,stderr=ssh.exec_command(com)
        if stdout:
            for i in stdout.readlines():
                ip=re.search(r"\b(\d{1,3}\.){3}\d{1,3}",i.strip()).group()
                brname=re.search(r"br-[a-z]+",i.strip()).group()
     #           ip_dict[brname].append(ip)
     #            q.put('{"%s":"%s"}' %(brname,ip))
                print "this is in %s : %s:ip %s"  %(node,brname,ip)
                q.put((brname,ip))
        ssh.close()
    except paramiko.AuthenticationException,e:
        print "fails to execute the command",e

# get_ip("node-2")

def ping(ip):
    status,output=commands.getstatusoutput("ping %s -i %f -c %d" %(ip,0.5,10))
    if status:
        # problem_ip.append(ip)
        q.put(ip)

def main():
    p=Pool()
    print node_list
    for n in node_list: 
        p.apply_async(get_ip,args=(n,))
        # get_ip(n)
    p.close()
    p.join()


    while not q.empty():
        # print a
        # b=json.loads(a)
        # for k,v in b.iteritems():
        # brIP=q.get()
        # print brIP
        k,v=q.get()
        ip_dict[k].append(v)

    p1=Pool()
    for k,v in ip_dict.iteritems():
        for i in v:
            p1.apply_async(ping,args=(i,))
    p1.close()
    p1.join()

if __name__=="__main__":
    main()
