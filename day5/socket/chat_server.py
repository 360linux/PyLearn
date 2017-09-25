import socket

bindinfo=('127.0.0.1',8090)

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(bindinfo)
sk.listen(6)

while True:
    conn,addr=sk.accept()
    mesg="welcom friends from %s,port is %d" %(addr[0],addr[1])
    # print mesg
    conn.sendall(mesg)
    flag=True
    while flag:
        data=conn.recv(1024)
        if data=='exit':
            flag=False
        elif data=='0':
            conn.sendall("your balance ")
        else:
            conn.sendall("wrong choise")

    conn.close()


