#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import uuid


class Client(object):
    def __init__(self):
        # hostname = '192.168.1.133'
        hostname = 'localhost'
        parameters = pika.ConnectionParameters(hostname)
        self.connection = pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()
        # 定义接收返回消息的队列
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)
        self.response = None
        self.corr_id = ''

    # 定义接收到返回消息的处理方法
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def request(self, n):
        # self.response = None
        self.corr_id = str(uuid.uuid4())
        # 发送计算请求，并声明返回队列
        self.channel.basic_publish(exchange='',
                                   routing_key='count_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        # 接收返回的数据
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


client = Client()

print(" [*] Requesting fib(30)")
response = client.request(30)
print(" [*] Got fib(30)= %r" % response)
