import datetime
import time
from functools import wraps


def print1(fun):
    def wrap(*args, **kwargs):
        print('print1 before')
        ret = fun(*args, **kwargs)
        print('print1 after')
        return ret

    return wrap


@property
@print1
def hello(a, b=0):
    print(a, b)
    return "hello" * a + str(b)


# print(hello(2, b=9))

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print("[DEBUG {}]: enter {}()".format(time.strftime('%Y-%m-%d %H:%M:%S'), func.__name__))
        return func(*args, **kwargs)

    return wrapper


@logging
def say(something):
    """say something"""
    print("say {}!".format(something))

say(1)
print(say.__name__)  # wrapper
print(say.__doc__)  # wrapper
