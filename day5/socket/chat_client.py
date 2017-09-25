import socket

bindinfo=('127.0.0.1',8090)
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(bindinfo)
sk.settimeout(3)

while True:
    data=sk.recv(1024)
    print "receice: %s" %data
    inp=raw_input("please input something:")
    sk.sendall(inp)
    if inp=='exit' or inp=='quit':
        break

sk.close()