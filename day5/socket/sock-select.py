import select
import threading
import sys

while True:
    readable, writeable, error = select.select([sys.stdin,],[],[],1)
    print readable
    print sys.stdin
    if sys.stdin in readable:
        print 'select get stdin',sys.stdin.readline()