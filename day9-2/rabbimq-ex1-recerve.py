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


# routing_keys=sys.argv[1] if len(sys.argv) >2 else "anonymous.info"
# message=' '.join(sys.argv[2:])  or "hellor world"
# channelmq.basic_publish(exchange="topic_log",routing_key=routing_keys,body=message)
# print "[x]  send %r:%r"  %(routing_keys,message)
# con.close()
result = channelmq.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channelmq.queue_bind(exchange='topic_log',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channelmq.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channelmq.start_consuming()