import pymysql
from src.sqldemo.config import Config


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
        return pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db)

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
