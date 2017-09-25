import socket
import  select

ip='127.0.0.1'
port=8090
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind((ip,port))
sk.settimeout(3)
sk.setblocking(0)
sk.listen(8)

print sk

inputs=[sk,]

while True:
    rlist,wlist,elist=select.select(inputs,[],inputs,6)
    print "the rlist:",rlist
    # print rlist[0]
    print  "the write:",wlist
    print "the error",elist
    for r in rlist:
        if r==sk:
            print "begin to accept"
            conn,addr=sk.accept()
            inputs.append(conn)
        else:
            recdata = r.recv(1024)
            if recdata:
                print "receive data: %s from %s,port is %d" %(recdata,addr[0],addr[1])
            else:
                inputs.remove(r)

sk.close()