#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
# channel.exchange_declare(exchange="topic_logs",type="topic")

q=channel.queue_declare(exclusive=True)
q_name=q.method.queue
binding_keys=sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0] )
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange="topic_logs",queue=q_name,routing_key=binding_key)


print "[*] Waiting for logs. To exit press CTRL+C"

def callback(ch,method,properties,body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,queue=q_name,no_ack=True)

channel.start_consuming()