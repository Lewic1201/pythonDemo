"""
Some common decorator tools
"""
# import datetime
from functools import wraps


# def logging(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         """print log before a function."""
#         print("[DEBUG] {}: enter {}()".format(datetime.time, func.__name__))
#         return func(*args, **kwargs)
#
#     return wrapper


def print_def(func):
    """打印函数的入参和返回结果"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('-' * 100)
            print("[METHOD]: {}()".format(func.__name__))
            print("[INPUT]: ", *args)
            ret = func(*args, **kwargs)
            print("[RESULT]:", ret)
            return ret
        except Exception as err:
            print(err)

    return wrapper


def print_cls(func):
    """打印类方法的入参和返回结果"""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            print('-' * 100)
            print("[METHOD]: {}()".format(func.__name__))
            print("[INPUT]:  ", *args)
            ret = func(self, *args, **kwargs)
            print("[RESULT]: ", ret)
            return ret
        except Exception as err:
            print(err)

    return wrapper
