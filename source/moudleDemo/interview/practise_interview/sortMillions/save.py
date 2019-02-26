import redis
import random
import time

from collections import deque

# LISTNAME = 'millions'
LISTNAME = 'mm'
# LISTNAME = 'mm2'


def create_num():
    """
    redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
    如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
    并且默认情况下一次pipline 是原子性操作。

    :return:
    """
    start = time.time()

    pool = redis.ConnectionPool(host='localhost', port=6379)
    r = redis.Redis(connection_pool=pool)

    pipe = r.pipeline(transaction=True)

    for i in range(10000000):
        num = random.randint(0, 9999999)
        r.rpush(LISTNAME, num)

    pipe.execute()

    end = time.time()
    print('set success, time:', end - start)


def get_list():
    pool = redis.ConnectionPool(host='localhost', port=6379)
    r = redis.Redis(connection_pool=pool)

    pipe = r.pipeline(transaction=True)

    llen = r.llen(LISTNAME)
    ls = r.lrange(LISTNAME, 0, llen)

    pipe.execute()

    return ls


def save_file():
    with open('data_list.txt', 'w') as ff:
        for i in get_list():
            ff.write(i.decode('utf-8'))
            ff.write('\n')


def queue_list():
    ls = get_list()
    queue = deque()
    for i in ls:
        queue.append(int(i.decode('utf-8')))
    return queue


if __name__ == '__main__':
    start = time.time()

    # create_num()
    # # print(get_list())
    # save_file()

    end = time.time()
    # print(queue_list())

    print('time:', end - start)
