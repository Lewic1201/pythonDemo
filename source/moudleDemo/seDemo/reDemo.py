import re

# 中文
pattern_chinese = u"[\u4e00-\u9fa5]+"

stri = 'a我sdf张阿萨.a德.we浪123;"费\\空+/*-adsf间!~!阿%$里斯柯达\n'

# print(re.findall(pattern_chinese, stri))

a = int('0x4e00', 16) - int('0x9fa5', 16)
# print(a)

str1 = 'A123  來    asdlkfjaslkalsdkfj.mp3'
pattern_01 = re.compile(r'^(\w\d{3})(\s{3,})(.*)(\.\w{2,4})$')
pattern_02 = re.compile(u".*[\u4e00-\u9fa5]+.*")

ret = re.match(pattern_02, str1)
print(ret)
ret2 = re.search(pattern_chinese, stri).group()
ret3 = stri.replace(ret2, '***' + ret2)
print(type(ret2))
print(ret2)
print(ret3)
