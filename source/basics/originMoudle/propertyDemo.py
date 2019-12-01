class Student(object):
    sex = 'M'

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self.birth

    # @property
    # def sex(self, value):
    #     self._sex = value


if __name__ == '__main__':
    ss = Student()
    ss.birth = 1994
    print(ss.birth)
    print(ss.age)
    ss.sex = 'F'
    print(ss.sex)
    # age.getter()
