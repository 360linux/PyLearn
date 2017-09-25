import socket

ip=('127.0.0.1',8090)
sk= day5.socket.socket()
sk.bind(ip)
sk.listen(6)

while True:
    conn,addr=sk.accept()
    rec_data=conn.recv(1024)
    print rec_data
    conn.sendall('i am sockserver')
    conn.close()