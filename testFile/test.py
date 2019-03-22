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

import re

RE_HAS_CHINESE = [u".*[\u4e00-\u9fa5]+.*", '包含中文']

pat1 = re.compile(u"([\u4e00-\u9fa5]+.*)")

context = []
with open('test.ini', 'rb') as ff:
    try:
        lines = ff.readlines()

        for line in lines:
            line = line.decode('utf-8')
            zh = re.search(pat1, line)
            if zh:
                ss = zh.group()
                line = line.replace(ss, '#$#' + ss)
            else:
                if line.strip() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    line = line[-3] * 19 + line
            context.append(line)
    except Exception:
        raise
with open('test', 'w') as ff:
    ff.writelines(context)
