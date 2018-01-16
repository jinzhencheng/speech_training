# -*- coding:utf-8 -*-
# Created by Jin(jinzhencheng@outlook.com) at 2018/01/16.

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Admin(Base):

    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class MyUser(Base):

    __tablename__ = "my_user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    gender = Column(String)
    address = Column(String)
    age = Column(Integer)
    real_name = Column(String)

