# -*- coding: utf-8 -*-
# @Time    : 18-12-21 下午3:48
# @Author  : Fuhz
# @Email   : 
# @File    : base.py
# ---------------------
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlcmemy, BaseQuery
from datetime import datetime
from sqlalchemy import Column, SmallInteger, DateTime

class SQLAlchemy(_SQLAlcmemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column(DateTime)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = datetime.now()

    def __getitem__(self, item):
        return getattr(self, item)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 0