#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 19:35
# @Author  : Administrator
# @File    : englishSentence.py
# @Software: PyCharm
# @context :

import random
import copy

stringA = '''
shmily. mimanchi. lewic. lpf. lwx.
Study and lose weight.
empire of angels.
docker linux python.
a long long long dream.
take the money , fuck the world.
serendipity.
Be a nerd, Be a geek.
I do not know go where,but I have been on the road.
The quick brown fox jumps over a lazy dog.
I think that that that that that student wrote on the blackboard was wrong.
I know. You know. I know that you know. I know that you know that I know.
 Pain past is pleasure.
While there is life, there is hope.
There are other fishes in the sea.
Never trouble trouble till trouble troubles you. 
2B or not 2B, that is a question.
Can you can a can as a canner can can a can?
Fifty-five flags freely flutter from the floating frigate.
Few free fruit flies fly from flames.
We never really grow up, we only learn how to act in public.
'''
stringA = stringA.replace('\n',' ')
list_str = stringA.split('.')
result_str = []
for i in list_str:
    data = i.strip().upper()+'. '
    result_str.append(data)
# print(list_str)
# print(result_str)

text_list = copy.deepcopy(result_str)
for num in range(100):
    try:
        insert_index = random.randint(0,len(text_list)-1)
        str_index = random.randint(0,len(list_str)-1)
        text_list.insert(insert_index,result_str[str_index])
    except Exception as e:
        print(e)
        continue
text = ''
for a_txt in text_list:
    text += a_txt

print(text)