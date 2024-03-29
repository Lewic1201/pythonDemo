"""
Some common decorator tools
"""
import logging
import traceback
import os
import pprint
import time

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


def print_manage(description='', ifdoc=False, iftime=False):
    """输出函数返回的结果"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if description:
                    headline = '-' * 50 + str(description) + '-' * 180
                else:
                    headline = '-' * 50 + ' RUN ' + func.__name__ + '() ' + '-' * 180
                print('\033[5;35;0m' + headline + '\033[0m')

                ret = func(*args, **kwargs)
                if len(str(ret)) > 200:
                    print('\033[5;33;0m' + "[RESULT]:" + '\033[0m')
                    pprint.pprint(ret)
                else:
                    print('\033[5;33;0m' + "[RESULT]:", str(ret) + '\033[0m')
                return ret
            except Exception as err:
                print('\033[5;31;0m' + str(err) + '\033[0m')
                raise

        return wrapper

    return decorator


def prints(func):
    """输出函数返回的结果"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            headline = '-' * 50 + ' RUN ' + func.__name__ + '() ' + '-' * 180
            print('\033[5;35;0m' + headline + '\033[0m')

            ret = func(*args, **kwargs)
            if len(str(ret)) > 200:
                pprint.pprint(ret)
            else:
                print('\033[5;33;0m' + str(ret) + '\033[0m')
            return ret
        except Exception as err:
            print('\033[5;31;0m' + str(err) + '\033[0m')
            raise

    return wrapper


def print_def(func):
    """打印函数的入参和返回结果"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('-' * 100)
            print('\033[5;35;0m' + "[METHOD]: {}()".format(func.__name__) + '\033[0m')
            print('\033[5;34;0m' + "[INPUT]: ", *args, '\033[0m')
            ret = func(*args, **kwargs)
            if len(str(ret)) > 200:
                print('\033[5;33;0m' + "[RESULT]:" + '\033[0m')
                pprint.pprint(ret)
            else:
                print('\033[5;33;0m' + "[RESULT]:", str(ret) + '\033[0m')
            return ret
        except Exception as err:
            print('\033[5;31;0m' + str(err) + '\033[0m')
            raise

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
            if len(str(ret)) > 200:
                print('\033[5;33;0m' + "[RESULT]:" + '\033[0m')
                pprint.pprint(ret)
            else:
                print('\033[5;33;0m' + "[RESULT]:", str(ret) + '\033[0m')
            return ret
        except Exception as err:
            print('\033[5;31;0m' + str(err) + '\033[0m')
            raise

    return wrapper


def print_class_params(obj):
    """打印所有的类变量"""

    # 添加函数属性
    def strs(self):
        dir_list = self.__dir__()
        classname = self.__class__.__name__
        ret = ''
        for i in dir_list:
            if i[:2] != '__':
                value = str(getattr(obj, i))

                # 不加颜色打印
                # ret += "%s.%s: %s\\n" % (classname, i, value)

                # 加颜色打印
                ret += '\033[5;34;0m' + classname + '\033[0m' + '.'
                ret += '\033[5;35;0m' + i + '\033[0m' + ': \n'
                ret += '\033[5;33;0m' + value + '\033[0m' + '\n'
        return ret

    obj.__str__ = strs
    return obj


def times(func):
    """计算函数花费的时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            start_str = '=' * 50 + ' RUN ' + func.__name__ + '() ' + '=' * 180

            print('\033[5;35;0m' + start_str + '\033[0m')
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()

            print('\033[5;33;0m' + "[RUN TIME]:", end - start, '\033[0m')
            return ret
        except Exception as err:
            print('\033[5;31;0m' + str(err) + '\033[0m')
            raise

    return wrapper
