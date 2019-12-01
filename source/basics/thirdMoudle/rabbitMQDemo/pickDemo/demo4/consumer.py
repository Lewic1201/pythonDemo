import pika
import time

# 声明socket实例
connect = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# 声明一个管道  虽然在之前的produce代码中声明过一次管道，
# 但是在不知道produce中的管道是否运行之前（如果未运行,consumers中也不声明的话就会报错），
# 在consumers中也声明一次是一种正确的做法
channel = connect.channel()

# 声明queue
# channel.queue_declare(queue="test")  # 队列非持久化
channel.queue_declare(queue="test1", durable=True)  # 队列持久化


# 回调函数
def callback(ch, method, properites, body):
    time.sleep(2)
    print("-----", ch, method, properites, body)
    print("Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动确认收到消息，添加手动确认时，no_ack必须为False,不然就会报错


channel.basic_consume(callback,
                      queue="test1",
                      no_ack=False)

print("Waiting for messages")
# 这个start只要一启动，就一直运行，它不止收一条，而是永远收下去，没有消息就在这边卡住
channel.start_consuming()
