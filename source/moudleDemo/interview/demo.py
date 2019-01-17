# print 'hello world'

# import thread

class New_int():
    def __add__(self,other):
        print 'self1:',self
        print 'other1:',other
        return int.__div__(self,other)
    def __sub__(self, other):
        print 'self2:',self
        print 'other2:', other
        return int.__add__(self,other)

# if __name__ == '__main__':
#     a = New_int(5)
#     b = New_int(3)
#     print a+b


a = New_int(5)
b = New_int(3)
print a+b

