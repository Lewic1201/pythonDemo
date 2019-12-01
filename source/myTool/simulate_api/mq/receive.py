#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika
import time


def recv(quene_name):
    # hostname = '192.168.1.133'
    hostname = 'localhost'
    parameters = pika.ConnectionParameters(hostname)
    connection = pika.BlockingConnection(parameters)

    # 创建通道
    channel = connection.channel()
    channel.queue_declare(queue=quene_name, durable=True)

    def callback(ch, method, properties, body):
        # time.sleep(15)
        print(" [x] Received %r" % (body,))
        # 返回给生产者消息
        channel.basic_ack(delivery_tag=method.delivery_tag)

    # 告诉rabbitmq使用callback来接收信息
    channel.basic_consume(quene_name, callback)

    # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理,按ctrl+c退出
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    # recv('message')
    # recv('notifications')
    recv('hello')
