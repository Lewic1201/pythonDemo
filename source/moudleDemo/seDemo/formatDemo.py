"""
format 函数
"""


# 通过关键字
print('{名字}今天{动作}'.format(名字='陈某某', 动作='拍视频'))
grade = {'name': '陈某某', 'fenshu': '59'}

# 通过关键字，可用字典当关键字传入值时，在字典前加**即可通过位置
print('{name}电工考了{fenshu}'.format(**grade))

# 通过位置
print('{1}今天{0}'.format('拍视频', '陈某某'))
print('{0}今天{1}'.format('陈某某', '拍视频'))

# 填充和对齐^<>分别表示居中、左对齐、右对齐，后面带宽度
print('{:^14}'.format('陈某某'))
print('{:>14}'.format('陈某某'))
print('{:<14}'.format('陈某某'))
print('{:*<14}'.format('陈某某'))
print('{:&>14}'.format('陈某某'))

# 精度和类型f精度常和f一起使用
print('{:.1f}'.format(4.234324525254))
print('{:.4f}'.format(4.1))

# 进制转化，b o d x 分别表示二、八、十、十六进制
print('{:b}'.format(250))
print('{:o}'.format(250))
print('{:d}'.format(250))
print('{:x}'.format(250))

# 千分位分隔符，这种情况只针对与数字
print('{:,}'.format(100000000))
print('{:,}'.format(235445.234235))
