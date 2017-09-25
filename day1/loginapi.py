from getpass import getpass
import sys

userfile="userinfo.txt"
lockfile="lock.txt"

WrongPassCode=200

def userlock(user):
    print "your pass input error beyond 3 times"
    with open(lockfile,"a")  as f:
        f.writelines(user+"\n")
    sys.exit()

def logincheck(user,password):
    with open(lockfile,"a+")  as f:
        for i in f.readlines():
            if  user==i.strip("\n"):
                print "your count is locked "
                sys.exit(8)
        else:
                user_list=[]
                with open(userfile,"r") as f:
                    for i in f.readlines():
                        usernamefile,passwordfile=i.strip('\n').split()
                        user_list.append(usernamefile)
                        if user==usernamefile :
                            if password==passwordfile:
                                print "welcom to login to platform:%s" %user
                                break
                            else:
                                print "your input password is wrong,please check it "
                                return WrongPassCode
                if user not in user_list:
                    print "the input user is not exist"
                    sys.exit(9)

def registry():
    while True:
        username=raw_input("input the registry username,exit or e to quit:")
        if username=="exit" or username=="e":
            sys.exit()
        else:
            with  open(userfile, "a+")  as f:
                for i in f.readlines():
                    user=i.strip('\n').split()[0]
                    if user==username:
                        print "the username %s has exist,please choose another" % username
                        break
                else:
                    while True:
                        password=getpass("please input the password,no space,8-12 long:")
                        if  len(password) <8 or len(password)>12:
                            print "the passwork is not fill the requrement,please input again "
                            continue
                        else:
                            password=password.replace(" ","")
                            try:
                                f.writelines(username+"\t"+password+"\n")
                                print "registry successful"
                            except IOError,e:
                                print "write registry info file failed",e
                            sys.exit()

def main():
    flag=True
    while flag:
        chose=raw_input("please chose a operation,0 for login,1 for registry,e for quit:")
        if chose=="0":
            i=1
            user = raw_input("input login username:")
            while flag:
                password = getpass("input login password:")
                loginstatus=logincheck(user,password)
                if loginstatus:
                    i+=1
                else:
                    flag=False
                if i>3:
                    userlock(user)
        elif chose=='1':
            registry()
        elif chose=="e":
            sys.exit()
        else:
            print "you chose is wrong"
            continue

if __name__== "__main__":
    main()