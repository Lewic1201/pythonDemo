class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, gender, course):
        genders = gender + '-'
        super(Teacher, self).__init__(name, genders)
        self.course = course


t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)
print(t.gender)

"""
python
带参数的多重继承

1. 不带参数的多重继承
"""


class A(object):
    def show_x(self):
        print('A')


class B(object):
    def show_y(self):
        print('B')


class C(object):
    def show_z(self):
        print('C')


class D(A, B, C):
    pass


# 测试
if __name__ == '__main__':
    d = D()
    d.show_x()  # A
    d.show_y()  # B
    d.show_z()  # C
"""
2. 带参数的多重继承
"""


# 作者：hhh5460
# 时间：2017.07.18

class A(object):
    def __init__(self, x=0):
        self._x = x

    def show_x(self):
        print(self._x)

    def show_name(self):
        print('A')


class B(object):
    def __init__(self, y=0):
        self._y = y

    def show_y(self):
        print(self._y)

    def show_name(self):
        print('B')


class C(object):
    def __init__(self, z=0):
        self._z = z

    def show_z(self):
        print(self._z)

    def show_name(self):
        print('C')


# 注意下面两类D、E，都是继承A、B、C，且A类的优先级最高。但是三条__init__语句的顺序是相反的
class D(A, B, C):
    def __init__(self, x=0, y=0, z=0):
        C.__init__(self, z)  # init C
        B.__init__(self, y)  # init B
        A.__init__(self, x)  # init A （A最优先）


class E(A, B, C):
    def __init__(self, x=0, y=0, z=0):
        super(E, self).__init__(x)  # init A （A最优先）  # 此句可简写成：super().__init__(x)
        super(A, self).__init__(y)  # init B
        super(B, self).__init__(z)  # init C


# 测试
if __name__ == '__main__':
    d = D(1, 2, 3)
    d.show_x()  # 1
    d.show_y()  # 2
    d.show_z()  # 3
    d.show_name()  # A

    e = E(1, 2, 3)
    e.show_x()  # 1
    e.show_y()  # 2
    e.show_z()  # 3
    e.show_name()  # A
