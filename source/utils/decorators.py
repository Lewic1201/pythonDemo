"""
Some common decorator tools
"""
import logging
import traceback
import os
from functools import wraps
from logging.handlers import TimedRotatingFileHandler
from source.utils.logs import logger as logs

LOG_PATH = os.path.abspath(os.path.join(__file__, "..\\..\\"))


def logger(func):
    """写入全局日志文件"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        logs.info('-' * 100)
        logs.info("[METHOD]: {}()".format(func.__name__))
        logs.info("[INPUT]:  ", *args)
        ret = func(*args, **kwargs)
        logs.info("[RESULT]: ", ret)
        return ret

    return wrapper


# 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
def loggerInFile(filename=LOG_PATH):
    """独立的日志装饰器"""

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):  # 1
            log_file_path = filename  # 日志按日期滚动，保留5天
            logger0 = logging.getLogger()
            logger0.setLevel(logging.INFO)
            handler = TimedRotatingFileHandler(log_file_path,
                                               when="d",
                                               interval=1,
                                               backupCount=5)
            formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger0.addHandler(handler)
            try:
                logger0.info("Arguments were: %s, %s" % (args, kwargs))
                result = func(*args, **kwargs)  # 2
                logger0.info("Result were: %s" % result)
            except:
                logger0.error(traceback.format_exc())

        return inner

    return decorator


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
