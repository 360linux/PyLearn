#!/usr/bin/env python
#-*- coding:utf-8 -*-


import paramiko
import sys
import select
import os
import tty
import termios

host="192.168.36.188"
port=22
pkey=paramiko.RSAKey.from_private_key_file('/home/liping/.ssh/id_rsa')
t=paramiko.Transport((host,port))
# t.connect(username='root',pkey=pkey)
t.start_client()
t.auth_publickey(username='root',key=pkey)
channel=t.open_session()
channel.get_pty()
channel.invoke_shell()

oldtty = termios.tcgetattr(sys.stdin)
try:
    tty.setraw(sys.stdin)
    channel.settimeout(0)

    while True:
        rlist,wlist,elist=select.select([channel,sys.stdin,],[],[])
        if sys.stdin in rlist:
            input_cmd = sys.stdin.read(1)
        # 将命令发送给服务器
            channel.sendall(input_cmd)

        # 服务器返回了结果,channel通道接受到结果,发生变化 select感知到
        if channel in rlist:
            # 获取结果
            result = channel.recv(1024)
            # print len(result)
            # 断开连接后退出
            if len(result) == 0:
                print("\r\n**** EOF **** \r\n")
                break
            # 输出到屏幕
            sys.stdout.write(result.decode())
            sys.stdout.flush()

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    # 关闭通道
channel.close()
# 关闭链接
t.close()