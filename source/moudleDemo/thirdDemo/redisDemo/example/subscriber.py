from redisHelper import RedisHelper


"""
客户端
打印生产者生产的消息
"""
obj = RedisHelper()
redis_sub = obj.subscribe()  # 调用订阅方法

while True:
    msg = redis_sub.parse_response()
    print(msg)
