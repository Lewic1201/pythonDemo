import time
from collections import deque


def lists(scale):
    start = time.time()
    a = []
    for i in range(scale):
        a.insert(0, i)
    end = time.time()
    print(end - start, end='')

    start = time.time()
    b = []
    for i in range(scale):
        b.append(i)
    end = time.time()
    print(' --', end - start)


def deques(scale):
    start = time.time()
    d = deque()
    for j in range(scale):
        d.insert(0, j)
    end = time.time()
    print(end - start)

    start = time.time()
    e = deque()
    for i in range(scale):
        e.append(i)
    end = time.time()
    print(' --', end - start)


lists(100000)
lists(110000)
lists(120000)
lists(130000)
lists(140000)
lists(150000)
deques(100000)
deques(110000)
deques(120000)
deques(130000)
deques(140000)
deques(150000)
