# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
#
#
# f('spam')

# Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
# Arguments: spam eggs

import re

s = 'adsfb12,3124ldsj,fksa34'
r = re.findall(r'[\d,]*', s)
print(r)
rr = ''.join(r)
print(rr)