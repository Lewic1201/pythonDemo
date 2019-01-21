class A(object):
    def __init__(self, a):
        print('init', a)

    def foo1(self):
        # self.foo2()
        # self.foo3()
        print("Hello", self)

    @staticmethod
    def foo2():
        print("hello")

    @classmethod
    def foo3(cls):
        print("hello", cls)


if __name__ == '__main__':
    # a = A()
    # a.foo1()
    # a.foo2()
    # a.foo3()
    # print(a)
    #
    # A.foo1(A)
    # A.foo1(a)
    # A.foo2()
    # A.foo3()
    # print(A)
    a = A('a')
    b = A
    b.foo3()
    a.foo1()
