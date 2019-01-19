#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path
import re

DATA_PATH = os.path.abspath(os.path.join(__file__, '..\\word.data'))


class PinYin(object):
    def __init__(self, dict_file=DATA_PATH):
        self.word_dict = {}
        self.dict_file = dict_file
        self.load_word()

    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with open(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]

    def hanzi2pinyin(self, string=""):
        """
        汉字转拼音
        :param string:
        :return:
        :rtype: list
        """
        result = []
        # if not isinstance(string, unicode):
        #     string = string.decode("utf-8")
        try:
            for char in string:
                if re.match('\s', char):
                    result.append(char)
                    continue
                key = '%X' % ord(char)
                value = self.word_dict.get(key, char).split()[0]
                if len(value) == 1:
                    # 忽略其它字符
                    result.append(value)
                else:
                    # 去掉注音
                    word = value[:-1].lower()
                    result.append(word)
        except Exception:
            raise
        return result

    def hanzi2pinyin_split(self, string="", split=""):
        """
        汉字转拼音
        :param string:
        :param split: 连接符
        :return:
        :rtype: str
        """
        result = self.hanzi2pinyin(string=string)
        # if split == "":
        #     return result
        # else:
        #     return split.join(result)
        return split.join(result)


# if __name__ == "__main__":
#     test = PinYin()
    # string = "钓鱼岛\t是\n中,,. .\\afds国的12321"
    # print("in: %s" % string)
    # print("out: %s" % str(test.hanzi2pinyin(string=string)))
    # print("out: %s" % test.hanzi2pinyin_split(string=string, split="-"))
    # print("out: %s" % test.hanzi2pinyin_split(string=string))
    # print(DATA_PATH)
