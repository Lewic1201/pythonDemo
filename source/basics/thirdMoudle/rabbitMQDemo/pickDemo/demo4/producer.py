import pika

# 声明一个socket 实例
connect = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# 声明一个管道
channel = connect.channel()
# 声明queue名称为test
# channel.queue_declare(queue="test") # 队列非持久化
channel.queue_declare(queue="test1", durable=True)  # 队列持久化


# RabbitMQ的消息永远不会被直接发送到队列中，它总是需要经过一次交换
channel.basic_publish(exchange='',
                      routing_key="test1",
                      body="hello word",
                      # make message persistent=>使消息持久化的特性
                      properties=pika.BasicProperties(delivery_mode=2, ),
                      )

print("Sent 'hello world'")

connect.close()
