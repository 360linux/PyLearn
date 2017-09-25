import  paramiko
host="192.168.36.188"
port=22
user='root'
password='passw0rd'
t=paramiko.Transport((host,port))
t.connect(username=user,password=password)

ssh=paramiko.SSHClient()
ssh._transport=t

