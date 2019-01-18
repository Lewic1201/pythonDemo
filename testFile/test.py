import re
import sys


def a():
    """
    test
    :return:
    """
    pass

    print(sys._getframe().f_code.co_name)

a()
# print(a.__name__)

# getattr(a, '__name__')
