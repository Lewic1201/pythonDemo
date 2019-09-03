class Base(object):
    """DB driver is injected in the init method."""

    def __init__(self):
        print("1233#$")
        super(Base, self).__init__()
        print("123#$")


class Son(Base):
    def __init__(self):
        super().__init__()

        print(312)


a = Son()
object()

print(isinstance(a, Base))
print(isinstance(a, Son))
print(issubclass(Son, Base))
