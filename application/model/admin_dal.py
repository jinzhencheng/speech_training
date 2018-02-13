# -*- coding:utf-8 -*-
# Created by Jin(jinzhencheng@outlook.com) at 2018/02/13.

from application.util import db_helper
from application.util import logger
from application.entity import Admin
from sqlalchemy import and_

mysql_helper = db_helper.MySQLHelper("speech_training")
my_logger = logger.get_logger()

def login(username, password):
    mysql_helper.open_driver()
    admin = None
    try:
        admin = mysql_helper.session.query(Admin).filter(and_(Admin.username == username,Admin.password == password)).first()
    except Exception, e:
        my_logger.error("Admin login error occurred, details:", e.message)
    finally:
        mysql_helper.close_driver()
    return admin
