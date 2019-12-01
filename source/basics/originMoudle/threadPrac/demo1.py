import threading
import time


def func1(name):
    time.sleep(2)
    print(name, time.ctime())


def prac1():
    t1 = threading.Thread(name='t01', target=func1, args=('t001',))
    t2 = threading.Thread(name='t02', target=func1, args=('t002',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main process over')


# prac1()
class Sayhi(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # time.sleep(2)
        print(self.name, time.ctime())


ss = Sayhi('t003')

# lock = threading.Lock()
# for i in range(10):
#     lock.acquire()
#     try:
#         ss.run()
#     finally:
#         lock.release()
ss.run()
ss.run()
ss.run()
ss.run()
ss.run()
ss.run()
ss.run()
print('main process over')
