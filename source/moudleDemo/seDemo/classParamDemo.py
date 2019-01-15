# https://www.jianshu.com/p/7a44488705dc
class ClsA:
    param1 = 1
    _param2 = 2
    __param3 = 3

    def meth(self):
        return 4

    def _meth2(self):
        return 5

    def __meth3(self):
        return 6


if __name__ == '__main__':
    a = ClsA()
    print(a.param1)
    print(a.meth())
    # print(a._ClsA_meth2())
    # print(a.__ClsA_meth2())
    print(a._ClsA__meth3())
    # print(a.__ClsA_meth3())
    # print(a.__ClsA_param3)


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

    # def get_name(self):
    #     return self.__name

    def get_score(self):
        return self.__score


bar = Student('Bart Simpson', 59)
# print(bar.get_name())
print(bar._Student__name)
