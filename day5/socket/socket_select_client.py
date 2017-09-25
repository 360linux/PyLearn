import socket
import  select

ip='127.0.0.1'
port=8090

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect((ip,port))

while True:
    content=raw_input("please input some:")
    sk.sendall(content)
sk.close()