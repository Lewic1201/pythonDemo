import numpy as np


class NumpyDemo:
    a = np.array([1, 4, 2, 5, 3])
    b = np.array([1, 2, 3, 4], dtype='float32')
    c = np.array([range(i, i + 3) for i in [2, 4, 6]])
    # d = np.zeros(10, dtype='int')
    d = np.zeros((3, 6), dtype='int')
    e = np.ones((3, 5), dtype=float)
    f = np.full((4,5),3.14)
    g = np.arange(10,23,2)
    a1 = np.linspace(0,1,4)
    a2 = np.random.random((3,3))
    # a3 = np.random.normal(0,1,(30,40))
    a3 = np.random.normal(0,1,(3,4))
    a4 = np.random.randint(0,10,(3,4))
    a5 = np.eye(3)
    a6 = np.empty(4)


    def __str__(self):
        dir_list = self.__dir__()
        # print(dir_list)
        for i in dir_list:
            if i[:2] != '__':
                exec('print("%s: \\n",NumpyDemo.%s)' % (i, i))
        return ''


if __name__ == '__main__':
    npdo = NumpyDemo()
    print(npdo.__class__.__name__)
    print(npdo)
