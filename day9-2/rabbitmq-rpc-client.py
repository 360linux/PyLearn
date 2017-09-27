#!/usr/bin/env python
import pika
import uuid
host="127.0.0.1"
user="liping"
password="leap1234"
credentials=pika.PlainCredentials(username=user,password=password)
para=pika.ConnectionParameters(host=host,virtual_host="/leap",credentials=credentials)

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(parameters=para)

        self.channel = self.connection.channel()
        # self.channel.exchange_declare(exchange="", type="direct")
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()
# for i in xrange(50,88):
print(" [x] Requesting fib(60)")
response = fibonacci_rpc.call(60)
print(" [.] Got %r" % response)