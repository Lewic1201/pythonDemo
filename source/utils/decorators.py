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
            print('\033[5;35;0m' + "[METHOD]: {}()".format(func.__name__) + '\033[0m')
            print('\033[5;34;0m' + "[INPUT]: ", *args, '\033[0m')
            ret = func(*args, **kwargs)
            print('\033[5;33;0m' + "[RESULT]:", ret, '\033[0m')
            return ret
        except Exception as err:
            print('\033[5;31;0m' + err + '\033[0m')

    return wrapper


def print_cls(func):
    """打印类方法的入参和返回结果"""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            print('-' * 100)
            print('\033[5;35;0m' + "[METHOD]: {}()".format(func.__name__) + '\033[0m')
            print('\033[5;34;0m' + "[INPUT]: ", *args, '\033[0m')
            ret = func(self, *args, **kwargs)
            print('\033[5;33;0m' + "[RESULT]:", ret, '\033[0m')
            return ret
        except Exception as err:
            print('\033[5;31;0m' + err + '\033[0m')

    return wrapper
