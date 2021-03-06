import configparser
from os import path

CONF_NAME = path.abspath('data.db')


class Config:
    config_dic = {}

    @classmethod
    def get_config(cls, sector, item):
        value = None
        try:
            # value = cls.config_dic[sector][item]
            if value:
                return value
            cf = configparser.ConfigParser()
            cf.read(CONF_NAME, encoding='utf8')  # 注意setting.ini配置文件的路径
            value = cf.get(sector, item)
            cls.config_dic = value
        except KeyError:
            raise
        finally:
            return value


# if __name__ == '__main__':
#     con = ConfigParser()
#     res = con.get_config('logging', 'level')
#     print(res)
