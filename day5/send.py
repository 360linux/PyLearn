#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
f=open('/home/liping/py/yesterday2','r')
print f.read()
f.close()
'''

# '''
# import  sys,time
# for i in range(20):
#     sys.stdout.write('#')
#     sys.stdout.flush()
#     time.sleep(0.2)
# '''
# import  sys
#
# f1= open('/home/liping/py/yesterday2', 'r')
# f2=open('/home/liping/py/yesterday3',mode='w')
# old=sys.argv[1]
# new=sys.argv[2]
# for line in f1:
#     if old in line:
#         line=line.replace(old,new)
#     f2.write(line)
# f1.close()
# f2.close()

import time
user,passwd = 'alex','abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print "wrapper func args:"
            if auth_type == "local":
                username = raw_input("Username:").strip()
                password = raw_input("Password:").strip()
                if user == username and passwd == password:
                    print "\033[32;1mUser has passed authentication\033[0m"
                    res = func(*args, **kwargs)  # from home
                    print  "---after authenticaion "
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print  "搞毛线ldap,不会。。。。"

        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")
@auth(auth_type="local") # home = wrapper()
def home():
    print("welcome to home  page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs  page")

index()
home()
bbs()