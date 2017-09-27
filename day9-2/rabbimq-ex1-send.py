import pika
import sys

host="127.0.0.1"
user="liping"
password="leap1234"
credentials=pika.PlainCredentials(username=user,password=password)
para=pika.ConnectionParameters(host=host,virtual_host="/leap",credentials=credentials)
con=pika.BlockingConnection(parameters=para)
channelmq=con.channel()
channelmq.exchange_declare(exchange="topic_log",type="topic")
routing_keys=sys.argv[1] if len(sys.argv) >2 else "anonymous.info"
message=' '.join(sys.argv[2:])  or "hellor world"
channelmq.basic_publish(exchange="topic_log",routing_key=routing_keys,body=message)
print "[x]  send %r:%r"  %(routing_keys,message)
con.close()