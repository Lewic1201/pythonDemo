#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 23:02
# @Author  : Administrator
# @File    : trans.py
# @Software: PyCharm
# @context : 翻译工具,自动检测 (通过调用有道接口) Trans().translate('文本')

import requests
import urllib.parse
import time
import random
import hashlib
import json


class Trans(object):
    """翻译工具"""

    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def _getData(self, search_name):
        # salt =i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)
        salt = ((time.time() * 1000) + random.randint(1, 10))
        # sign = n.md5("fanyideskweb" + t + i + "ebSeFb%=XZ%T[KZ)c(sy!")
        sign_text = "fanyideskweb" + search_name + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
        sign = hashlib.md5((sign_text.encode('utf-8'))).hexdigest()
        paydata = {
            'i': search_name,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
        }
        return paydata

    def _getHeader(self):
        header = {
            'Host': 'fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-846616837@1.80.219.201; '
                      'OUTFOX_SEARCH_USER_ID_NCOO=129549097.60835753; '
                      'UM_distinctid=15ff309f18ddc-094cb5494ad815-5d4e211f-1fa400-15ff309f18e449; '
                      '_ga=GA1.2.184261795.1517119351; '
                      '__guid=204659719.2556877880764680700.1518435624954.942; '
                      'JSESSIONID=aaa3A5BLhtTrh4TPX_mgw; '
                      'monitor_count=2; '
                      '___rl__test__cookies=1518488731567'
        }
        return header

    def _getRequest(self, paydata, header):
        _data = urllib.parse.urlencode(paydata).encode('utf-8')
        _header = header
        response = requests.post(self.url, data=_data, headers=_header)
        return response.text

    def _getResult(self, response):
        result_text = json.loads(response)
        # src = result_text['translateResult'][0][0]['src']
        tgt = result_text['translateResult'][0][0]['tgt']
        return tgt

    def translate(self, search_name):
        """
        主要翻译方法
        :param search_name: 需要翻译的文本
        :return: 英文或汉字
        :rtype: str
        """
        # app = search()
        if search_name.strip()[0] in '0123456789':
            return search_name
        paydata = self._getData(search_name)
        header = self._getHeader()
        response = self._getRequest(paydata, header)
        tgt = self._getResult(response)
        return tgt

    def get_translate_split(self, text, split=''):
        result = self.translate(text)
        ret = split.join(result.split())
        return ret


if __name__ == '__main__':
    ss = Trans()
    print(ss.translate('测试'))
    print(ss.translate('知りたいのですが'))
    print(ss.translate('사랑해요'))
    print(ss.translate('administrator'))

    print(ss.translate('我是administrator'))
    print(ss.translate('administrator是我'))
    print(ss.translate('知りたいのですが,and you'))
    print(ss.translate('hehe知りたいのですが'))
    # print(ss.get_translate_split('asd','_'))
