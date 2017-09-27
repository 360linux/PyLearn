
import pika
import sys

host="127.0.0.1"
user="liping"
password="leap1234"
credentials=pika.PlainCredentials(username=user,password=password)
para=pika.ConnectionParameters(host=host,virtual_host="/leap",credentials=credentials)
con=pika.BlockingConnection(parameters=para)
channel=con.channel()
channel.queue_declare(queue="rpc")
# channel.exchange_declare(exchange="",type="direct")
def fib(n):
    if n==0:
        return  0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def on_response(ch,method,property,body):
    n=int(body)
    print  "[.] fib(%s)" % n
    response=fib(n)
    channel.basic_publish(exchange="",routing_key=property.reply_to,properties=pika.BasicProperties(correlation_id= \
                    property.correlation_id),body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_response,queue="rpc")
print  " [x] Awaiting RPC requests"
channel.start_consuming()