# coding:utf-8

import configparser
import json
import os
from source.utils.logs import logger


CONFIG_FILE = '/config/config.ini'
JSON_FILE = '/config/case_json.db'


class Dictionary(dict):
    """
    把config.ini中的参数添加值dict
    """

    def __getattr__(self, keyname):
        # 如果key值不存在则返回默认值"not find config keyname"
        return self.get(keyname, "配置文件中没有找到对应的keyname")


class Config(object):
    """
    ConfigParser二次封装，在字典中获取value
    """

    def __init__(self, conf_type='str'):
        # 设置conf.ini路径
        if conf_type == 'str':
            self.conf_file = CONFIG_FILE
        elif conf_type == 'json':
            self.conf_file = JSON_FILE
        else:
            raise Exception('不存在此类型')
        current_dir = os.path.dirname(__file__)
        root_dir = os.path.dirname(current_dir)
        file_name = root_dir + self.conf_file
        # 实例化ConfigParser对象
        self.config = configparser.ConfigParser()
        self.config.read(file_name)
        # 根据section把key、value写入字典
        for section in self.config.sections():
            setattr(self, section, Dictionary())
            for keyname, value in self.config.items(section):
                setattr(getattr(self, section), keyname, value)

    def get_conf(self, section, param_key=None):
        """
        :param section:
        :param param_key:
        :return: param_value
        :rtype str
        """
        if param_key is None:
            return getattr(self, section)
        else:
            param_key = param_key.lower()
        if section not in self.config.sections():
            logger.info("%s 找不到该 section" % self.conf_file)
        return getattr(getattr(self, section), param_key)

    def get_req_data(self, section, param_key=None):
        """
        读取用例要发送的data
        :param section:
        :param param_key:
        :return param_value
        :rtype dict
        """
        try:
            if self.conf_file != JSON_FILE:
                logger.error("配置文件初始化传入conf_type不是'json'")
                return {}
            if param_key is None:
                return getattr(self, section)
            else:
                param_key = param_key.lower()
            if section not in self.config.sections():
                logger.info("%s 找不到该 section" % self.conf_file)

            param_value = getattr(getattr(self, section), param_key)
            if param_value:
                data_dict = json.loads(param_value)
            else:
                data_dict = {}
            return data_dict
        except ValueError:
            logger.error("%s文件中该参数非json格式" % self.conf_file)
        except Exception as err:
            logger.error(str(err))

# if __name__ == "__main__":
#     db = Config()
#     info = db.get_conf("token", 'test')
#     print info
#     print type(info)
#     import json
#     dict1 = json.loads(info)
#     print dict1,type(dict1)
