#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 10:33
# @Author  : Administrator
# @File    : checkApi.py
# @Software: PyCharm
# @context :

import yaml
import json
import pprint
import difflib


def get_conf(yaml_file=None):
    if yaml_file is None:
        yaml_file = 'api_conf.yaml'

    with open(yaml_file, encoding='utf-8') as yf:
        context = yf.read()
        conf_data = yaml.load(context, Loader=yaml.FullLoader)

        pprint.pprint(conf_data)

    if not conf_data:
        raise Exception('获取配置文件api信息失败!')
    return conf_data


def get_url_list(conf_data):
    url_list = []
    try:
        metadata = conf_data.get('api', None)

        param = {'pid': '123456', 'token': '332'}

        now = metadata.get('head', None)['now']
        origin = metadata.get('head', None)['origin']

        origin_url_prefix = metadata['web']['http'] + origin['host'] + ':' + str(origin['port'])
        now_url_prefix = metadata['web']['http'] + now['host'] + ':' + str(now['port'])

        apis = metadata.get('interface', None)

        uri_list = []
        for api_name in apis:
            api_info = apis.get(api_name)
            uri_mid = api_info.get('uri', '')

            if api_info.get('used', True):
                uri_list.append(uri_mid)
            else:
                continue

            uri_suffix_list = api_info.get('uri_suffix_list', [])
            uri_suffix_dict = api_info.get('uri_suffix_dict', dict())

            if uri_suffix_list:
                for suffix in uri_suffix_list:
                    uri = uri_mid + suffix
                    uri_list.append(uri)

            if uri_suffix_dict:
                for d in uri_suffix_dict:
                    if d.get('used', True):
                        uri = uri_mid + d.get('txt', '')
                        uri_list.append(uri)

        for uri in uri_list:
            # 合入projectId
            uri_final = uri.format(**param)

            uri_group = {'origin_url': origin_url_prefix + uri_final,
                         'now_url': now_url_prefix + uri_final,
                         'method': 'GET'}

            url_list.append(uri_group)

        pprint.pprint(url_list)
        return url_list

    except Exception as err:
        print(err)
        raise


def check_res(str1, str2):
    origin_json = json.loads(str1)
    now_json = json.loads(str2)
    # origin_json = dict()
    # now_json = dict()

    for key in origin_json.keys():
        value_eval = origin_json[str(key)]
        value_test = now_json[str(key)]

        diff = difflib.SequenceMatcher(None, value_eval, value_test).quick_ratio()
        print(key, diff)


def check_dict(d1, d2):
    """
    比对嵌套的数据体的异同
    :param d1:
    :param d2:
    :return:
    """
    diff = []

    def add_diff(v1, v2, msg=None):
        if v1 is None:
            v1 = 'None'
        if v2 is None:
            v2 = 'None'
        if msg:
            diff.append("%s%s%s%s%s" % (str(v1), '-' * 10, msg, '-' * 10, str(v2)))
        else:
            diff.append("%s%s%s" % (str(v1), '-' * 20, str(v2)))

    def check(v1, v2):
        # print(v1,v2)
        if type(v1) != type(v2):
            add_diff(v1, v2, True)
            return
        if isinstance(v1, (str, int, bool, float)):
            if v1 != v2:
                add_diff(v1, v2)
        elif isinstance(v1, (tuple, list)):
            size = len(v1)
            if len(v2) != size:
                add_diff(v1, v2, size)
            else:
                for i in range(size):
                    check(v1[i], v2[i])
        elif isinstance(v1, set):
            pass
        elif isinstance(v1, dict):
            if v1.keys() != v2.keys():
                add_diff(v1, v2, 'size')
            else:
                for k in v1:
                    check(v1[k], v2[k])
        elif v1 is None:
            if v2 is not None:
                add_diff(v1, v2, 'null')
        else:
            print(type(v1))
        return

    check(d1, d2)
    print(diff)
    return diff


if __name__ == '__main__':
    pass
    # conf_data = get_conf()
    # url_data = get_url_list(conf_data)

    str1 = """
{"api": {"head": {"now": {"host": "127.0.0.1", "port": 5002},
              "origin": {"host": "127.0.0.1", "port": 5001}},
     "interface": {"getSnapshot": {"uri": "/v2/{pid}/snapshots",
                                   "uri_suffix_dict": [{"txt": "?limit=2",
                                                        "used": true},
                                                       {"txt": "?limit=2&sort=id"}],
                                   "uri_suffix_list": ["?limit=3&offset=1"],
                                   "used": true}},
     "web": {"http": "https://"},
     "test_float2": 2.13,
     "test_float": 2.13
     }}
"""

    str2 = """
{"api": {"head": {"now": {"host": "127.0.0.1", "port": 5003},
              "origin": {"host": "127.0.0.1", "port": 5001}},
     "interface": {"getSnapshot": {"uri": "/v2/{pid}/snapshots",
                                   "uri_suffix_dict": [{"txt": "?limit=2",
                                                        "used": true},
                                                       {"txt": "?limit=2&sort=id"}],
                                   "uri_suffix_list": ["?limit=3&offset=1"],
                                   "used": true}},
     "web": {"http": "https://"},
     "test_float2": 2.14,
     "test_float": 2.13,
     "testNone": null
     }}
"""
    # check_res(str1, str2)
    origin_json = json.loads(str1)
    now_json = json.loads(str2)
    # origin_dict = json.dumps(origin_json)
    # now_dict = json.dumps(now_json)
    check_dict(origin_json, now_json)
