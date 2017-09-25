#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-9 下午4:59
# @Author  : Liping
# @Site    : 
# @File    : socket-epoll-server-ex1.py
# @Software: PyCharm
import select
import Queue
import sys
import socket

loop=True
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",10001)
s.bind(server_address)
s.listen(10)
s.setblocking(0)
epoll=select.epoll()
epoll.register(s.fileno(),eventmask=select.EPOLLIN)
message_queue={}
con_dict={s.fileno():s,}

while loop:
    print "wait for a connection"
    events=epoll.poll(6)
    print  events
    if not events:
        print "no connection,continue"
        continue
    print "has %d events to handle" %len(events)
    for fd,event in events:
        sock=con_dict[fd]
        if fd==s.fileno:
            con,addr=s.accept()
            print  "client connect",addr
            con.setblocking(0)
            epoll.register(con.fileno(),eventmask=select.EPOLLIN)
            message_queue[con]=Queue.Queue()
            con_dict[con.fileno()]=con
        elif event and select.EPOLLHUP:
            print "client closed"
            epoll.unregister(fd)
            con_dict[fd].close()
            del con_dict[fd]
        elif event and select.EPOLLIN:
            data=con_dict[fd].recv(1024)
            if data:
                print "receive data",data,"from client",sock.getpeername()
                message_queue[sock].put(data)
                epoll.modify(fd,select.EPOLLOUT)
        elif event and select.EPOLLOUT:
            try:
                msg=message_queue[sock].get_nowait()
            except Queue.Empty:
                print sock.getpeername,"empty queue"
                epoll.modify(fd,select.EPOLLIN)
            else:
                print "发送数据：", data, "客户端：", sock.getpeername()
                sock.sendall(msg)

epoll.unregister(s.fileno())
epoll.close()
s.close()

