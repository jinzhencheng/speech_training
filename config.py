# -*- coding:utf-8 -*-
# Created by Jin(jinzhencheng@outlook.com) at 2018/01/15.

class GeneralConfig():
    DEFAULT_LOG_FILENAME = "speech_training.log"
    pass

class MySQLConfig():

    HOST = "localhost"
    PORT = 3306
    URI = None
    USERNAME = "root"
    PASSWORD = "root"
    DEFAULT_POOL_MAX_SIZE = 100

    @staticmethod
    def create_db_uri(db_name, username=USERNAME, password=PASSWORD, host=HOST, port=PORT):
        if not db_name:
            return
        uri = "mysql+mysqldb://%s:%s@%s:%d/%s?charset=utf8" % (username, password, host, port, db_name)
        return uri
    pass

