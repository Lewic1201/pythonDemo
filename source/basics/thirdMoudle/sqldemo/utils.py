import pymysql
from source.basics.thirdMoudle.sqldemo.config import Config
from source.utils.decorators import print_cls
from source.utils.logs import logger


class Sql():
    def __init__(self):
        conf = Config()
        self.host = conf.get_config('mysql', 'host')
        self.port = conf.get_config('mysql', 'port')
        self.user = conf.get_config('mysql', 'user')
        self.password = conf.get_config('mysql', 'password')
        self.db = conf.get_config('mysql', 'database')
        self.conn = self.sql_connect()

    def sql_connect(self):
        logger.info("%s %s %s %s %s" % (self.host, self.port, self.user, self.password, self.db))
        return pymysql.connect(self.host, self.user, self.password, self.db)

    def sql_execute(self, sql_str):
        try:
            cursor = self.conn.cursor()
            effect_row = cursor.execute(sql_str)
            return effect_row
        except Exception as err:
            raise Exception('Sql execute failed, please check sql_str')

    def sql_commit(self):
        self.conn.commit()

    def sql_close(self):
        self.conn.close()


if __name__ == '__main__':
    try:
        sql = Sql()
    except Exception:
        raise
    try:
        ret = sql.sql_execute('select * from user_info')
        print(ret)
    finally:
        sql.sql_close()
