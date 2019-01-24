import os
import re
import shutil


def get_data():
    """
    清洗 package_name的数据
    :return: [[]]
    """
    with open('package_name.txt', 'r', encoding='utf-8') as pn:
        context = pn.read()

    main_data = context.split('\n\n\n')
    print(context)
    print(main_data)

    datas = []
    # 处理数据 [[原始数据,中文部分,英文部分,生成的类名,生成的文件名,文件内容,包名,...],...]
    for i in main_data:
        tmp = []

        ch_ctx = i.split('\n')[0]
        en_ctx = i.split('\n')[1]

        # 类名
        classname = en_ctx.replace(' Controller', '').replace(' ', '')

        # 文件名
        filename = 'test_' + (en_ctx.replace(' Controller', '').replace(' ', '_')).lower() + '.py'

        # 文件代码
        coder = '''# coding: utf-8

import sys
import unittest
from api.basetest import WebRequests
from utils import util_tool
from utils.logs import APILog as Logger
from utils.configread import Config


class %sTest(unittest.TestCase):
    """%s"""

    @classmethod
    def setUpClass(cls):
        """当前测试类第一次运行前执行"""
        standard_headers = {'Content-Type': 'application/json'}
        cls.headers = util_tool.add_token(standard_headers)
        cls.base_url = Config().get_conf('api', 'baseURL')
        cls.case_conf = Config(conf_type='json')
        cls.client = WebRequests(cls.base_url, cls.headers)

    @classmethod
    def tearDownClass(cls):
        """当前测试类最后一次运行后执行"""
        Logger.info('Test case over')

    def setUp(self):
        """每个测试用例运行前"""
        pass

    def tearDown(self):
        """每个测试用例运行后"""
        pass
''' % (classname, ch_ctx)

        # tmp[原始数据,中文部分,英文部分,生成的类名,生成的文件名,文件内容,包名,...]
        tmp.append(i)
        tmp.append(ch_ctx)
        tmp.append(en_ctx)
        tmp.append(classname)
        tmp.append(filename)
        tmp.append(coder)
        tmp.append(filename[5:-3])

        datas.append(tmp)

    return datas


def create_file(datas, path='.\\tmp'):
    """
    根据上面数据生成文件
    :param datas:  [[0原始数据,1中文部分,2英文部分,3生成的类名,4生成的文件名,5文件内容,6包名,...],...]
    :param path: 生成路径
    :return: 返回一个路径,方便删除
    """
    if path[0] in ['.', '\\', '/']:
        path = os.path.join(__file__, '..\\', path)
    if not os.path.exists(path):
        os.makedirs(path)
    for data in datas:
        package_name = os.path.join(path, data[6])
        if not os.path.exists(package_name):
            os.makedirs(package_name)
        file_name = os.path.join(path, data[6], data[4])
        print(os.path.abspath(file_name))
        with open(file_name, 'w', encoding='utf-8') as case_file:
            case_file.write(data[5])

        init_file_name = os.path.join(path, data[6], '__init__.py')
        print(os.path.abspath(init_file_name))
        with open(init_file_name, 'w', encoding='utf-8') as init_file:
            init_file.write('')
        # break

    return os.path.abspath(path)


if __name__ == '__main__':
    datas = get_data()

    # 生成临时文件
    file_path = create_file(datas)

    # # 删除临时文件
    # shutil.rmtree(file_path)
