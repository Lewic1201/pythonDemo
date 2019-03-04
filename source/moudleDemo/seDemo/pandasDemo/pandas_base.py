import pandas as pd
import numpy as np

from pandas import Series, DataFrame
from source.utils.decorators import print_classparams as pcp


@pcp  # 自动打印类变量
class pand:
    s = Series([1, 2, 3.0, 'abc'])
    t = Series(data=[1, 3, 5, 7], index=['a', 'b', 'x', 'y'])
    ti = t.index
    tv = t.values
    data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    df = DataFrame(data)
    df2 = DataFrame(data, index=['one', 'two', 'three', 'four', 'five'],
                    columns=['year', 'state', 'pop', 'debt'])
    ser = Series(list('abcdefg'))
    serc = ser

    population_dict = {'California': 38332521,
                       'Texas': 26448193,
                       'New York': 19651127,
                       'Florida': 19552860,
                       'Illinois': 12882135}
    population = pd.Series(population_dict)

    An = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
    An2 = np.array([(0, 0.0), (0, 0.0), (0, 0.0)],
                   dtype=[('A', '<i8'), ('B', '<f8')])
    An3 = pd.DataFrame(An)

    ind = pd.Index([2, 3, 5, 7, 11])
    ind1 = ind[1]
    ind2 = ind[::2]
    ind3 = ind.size, ind.shape, ind.ndim, ind.dtype

    pdf = pd.DataFrame(np.random.rand(3, 2),
                       columns=['foo', 'bar'],
                       index=['a', 'b', 'c'])

    rng = np.random.RandomState(42)
    ser1 = pd.Series(rng.randint(0, 10, 4))
    ne = np.exp(ser1)


if __name__ == '__main__':
    print(pand())
