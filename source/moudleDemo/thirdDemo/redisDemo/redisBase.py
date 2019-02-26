import redis

"""
http://www.cnblogs.com/melonjiang/p/5342383.html#undefined
http://www.cnblogs.com/melonjiang/p/5342505.html
"""

HOST = 'localhost'


def simple_connect():
    r = redis.Redis(host=HOST, port=6379, db=0)
    r.set('name', 'zhangsan')  # 添加
    print(r.get('name'))  # 获取


# simple_connect()


def pool_connect():
    """
    redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
    默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，
    这样就可以实现多个Redis实例共享一个连接池。

    :return:
    """
    pool = redis.ConnectionPool(host=HOST, port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set('name1', 'zhangsan1')  # 添加
    print(r.get('name1'))  # 获取


pool_connect()


def pipline_connect():
    """
    redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
    如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
    并且默认情况下一次pipline 是原子性操作。

    :return:
    """
    pool = redis.ConnectionPool(host='192.168.0.110', port=6379)
    r = redis.Redis(connection_pool=pool)

    pipe = r.pipeline(transaction=True)

    r.set('name', 'zhangsan')
    r.set('name', 'lisi')

    pipe.execute()


pipline_connect()
