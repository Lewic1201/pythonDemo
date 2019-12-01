from redisHelper import RedisHelper  # 如果报错,请忽略,pycharm显示有问题

"""
消息生产者
运行一次发一次消息
"""

obj = RedisHelper()
obj.publish('hello')  # 发布
