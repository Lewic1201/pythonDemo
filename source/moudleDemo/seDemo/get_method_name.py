import sys
import inspect


def a():
    """
    test
    :return:
    """
    print(sys._getframe().f_code.co_name)


# print(a.__name__)

# getattr(a, '__name__')


def timeit(func):
    def run(*argv):
        print(func.__name__)
        if argv:
            ret = func(*argv)
        else:
            ret = func()
        return ret

    return run


@timeit
def t(a):
    print(a)


def get_current_function_name():
    return inspect.stack()[1][3]


class MyClass:
    def function_one(self):
        print("%s.%s invoked" % (self.__class__.__name__, get_current_function_name()))


if __name__ == "__main__":
    myclass = MyClass()
    myclass.function_one()
    a()
    t(1)
