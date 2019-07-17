#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
参考链接 https://www.cnblogs.com/jfl-xx/p/7324285.html
"""

import pika
import random

number = random.randint(1, 1000)
hello = 'hello world:%s' % number


def send_mq(queue_name='hello', body=hello):
    # 新建连接，rabbitmq安装在本地则hostname为'localhost'
    # hostname = '192.168.1.133'
    hostname = 'localhost'
    parameters = pika.ConnectionParameters(hostname)
    connection = pika.BlockingConnection(parameters)

    try:
        # 创建通道
        channel = connection.channel()
        # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
        channel.queue_declare(queue=queue_name, durable=True)

        # 交换机; 队列名,写明将消息发往哪个队列; 消息内容
        # routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=body,
                              properties=pika.BasicProperties(delivery_mode=2))

        print(" [x] Sent %s" % body)
    except Exception:
        raise
    finally:
        # print('hello')
        connection.close()


if __name__ == '__main__':
    send_mq('message')
