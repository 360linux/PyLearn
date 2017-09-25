#!/usr/bin/env python
#-*- coding:utf-8 -*-

import  paramiko
import  sys
import  select
import  os

host="192.168.36.188"
port=22
pkey=paramiko.RSAKey.from_private_key_file('/home/liping/.ssh/id_rsa')
t=paramiko.Transport((host,port))
t.connect(username='root',pkey=pkey)
ssh=paramiko.SSHClient()
ssh._transport=t
stdin,stdout,stderr=ssh.exec_command('df -h')
sftp=paramiko.SFTPClient.from_transport(t)
sftp.put(localpath="/home/liping/.ssh/id_rsa",remotepath='/tmp/id_rsa')