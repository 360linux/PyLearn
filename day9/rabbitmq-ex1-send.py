import  pika
import  sys


username="liping"
password="leap1234"
host="127.0.0.1"
port=5672
credential=pika.PlainCredentials(username=username,password=password)
para=pika.ConnectionParameters(host=host,port=port,credentials=credential,virtual_host="/log")
con=pika.BlockingConnection(parameters=para)
channel=con.channel()
channel.exchange_declare(exchange="topic_logs",type="topic")
routing_key=sys.argv[1] if len(sys.argv)>2 else "anonymous.info"
message=' '.join(sys.argv[2:]) or "test message"
channel.basic_publish(exchange="topic_logs",routing_key=routing_key,body=message)

print "[x]  send %r:%r"  %(routing_key,message)
con.close()