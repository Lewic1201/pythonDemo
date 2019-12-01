#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

# hostname = '192.168.1.133'
hostname = 'localhost'
parameters = pika.ConnectionParameters(hostname)
connection = pika.BlockingConnection(parameters)

# 创建通道
channel = connection.channel()
# 声明队列
channel.queue_declare(queue='count_queue')
print(' [*] Waiting for n')


# 算法
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 设置回调函数
def on_request(ch, method, props, body):
    n = int(body)
    response = fib(n)
    print(" [*] fib(%s)" % n, '=', response)
    # 将结果反馈
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 公平调度
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='count_queue')
print(" [*] Awaiting count_queue requests")
channel.start_consuming()
connection.close()
