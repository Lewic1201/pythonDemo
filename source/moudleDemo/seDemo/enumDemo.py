my_Enum = {
    'red': 1,
    'yellow': 2,
    'blue': 3
}
print(my_Enum['red'])

from enum import IntEnum


class my_Enum(IntEnum):
    red = 1,
    green = 2,
    blue = 3,
    what = 3,
    yellow = 9


# 按名字取出枚举的值
print(my_Enum['red'])
print(my_Enum['what'])
# 枚举的值返回枚举名字
print(my_Enum(9))
print(my_Enum['red'].name)
print(my_Enum['red'].value)
# 可以用for in迭代
for i in my_Enum:
    print(i.name, '->', i.value)
