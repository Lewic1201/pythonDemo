# print 'hello world'

# import thread

class New_int:
    def __init__(self, x):
        self.num = x

    def __add__(self, other):
        print('self1:', self)
        print('other1:', other)
        return self.num - other.num

    def __sub__(self, other):
        print('self2:', self)
        print('other2:', other)
        return int.__add__(self.num, other.num)


# if __name__ == '__main__':
#     a = New_int(5)
#     b = New_int(3)
#     print a+b


a = New_int(5)
b = New_int(3)
print(a + b)
print(a - b)
