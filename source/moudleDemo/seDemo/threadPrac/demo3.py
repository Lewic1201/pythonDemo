from threading import Thread
from random import randint
import time

count = 100


def buyTicket(name, num):
    global count
    if count > 0:
        # time.sleep(0.1)
        count = count - num
        # time.sleep(0.1)
        count = count + num
        # print('%s buy %s ticket,count = %s' % (name, num, count))
        return True
    else:
        print('%s buy ticket failed')
        return False


def runThread():
    for i in range(200000):
        buynum = randint(1, 4)
        buyTicket('people%s' % i, buynum)


if __name__ == '__main__':
    t1 = Thread(target=runThread())
    t2 = Thread(target=runThread())
    t3 = Thread(target=runThread())
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(count)
    pass

# # import time, threading
#
# # 假定这是你的银行存款:
# balance = 0
#
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
#
# t1 = Thread(target=run_thread, args=(5,))
# t2 = Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
