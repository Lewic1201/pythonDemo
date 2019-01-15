from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector (%r, %r)' % (self.x, self.y)

    def __abs__(self):
        '''
        默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对__bool__ 或者 __len__ 函数有自己的实现。
        bool(x) 的背后是调用x.__bool__() 的结果；如果不存在 __bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。
        若返回 0，则 bool 会返回 False；否则返回True。
        '''
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

