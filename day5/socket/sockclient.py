import socket

ip=('127.0.0.1',8090)
sk= day5.socket.socket()
sk.connect(ip)

# print sk.getsockname()

# print sk.getpeername()
sk.sendall('sockClient')
server_reply=sk.recv(1024)

print server_reply

sk.close()