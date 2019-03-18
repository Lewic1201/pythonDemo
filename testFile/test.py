# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
#
#
# f('spam')

# Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
# Arguments: spam eggs

# import re
#
# s = 'adsfb12,3124ldsj,fksa34'
# r = re.findall(r'[\d,]*', s)
# print(r)
# rr = ''.join(r)
# print(rr)

print('\033[5;33;0m' + "[RESULT]:" + '\033[0m')
# import chardet
#
# data = u'12312中国'.encode('gbk')
# print(chardet.detect(data))


# from importlib import import_module
#
# modules = ['os', 'sys', 're']
# for m in modules:
#     locals()[m] = import_module(m)
#
# a = os.path.join('a','b')
# print(a)