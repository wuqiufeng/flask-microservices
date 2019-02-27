# -*- coding: utf-8 -*-
# @Time    : 18-12-18 下午3:45
# @Author  : Fuhz
# @Email   : 
# @File    : __init__.py.py
# ---------------------
from contextlib import contextmanager

import redis as redis
from sqlalchemy import create_engine, event
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.orm import sessionmaker

from app import config

#
# SETTINGS = config["default"]
# redis_pool = redis.ConnectionPool(host=SETTINGS.REDIS_HOST, port=SETTINGS.REDIS_PORT, db=0, password=SETTINGS.REDIS_PASSWD, encoding='utf-8')
# redis_client = redis.Redis(connection_pool=redis_pool)


def checkout_listener(dbapi_con, con_record, con_proxy):
    try:
        try:
            dbapi_con.ping(False)
        except TypeError:
            dbapi_con.ping()
    except dbapi_con.OperationalError as exc:
        if exc.args[0] in (2006, 2013, 2014, 2045, 2055):
            raise DisconnectionError()
        else:
            raise


def session_factory(db_uri=config['default'].SQLALCHEMY_DATABASE_URI):
    engine = create_engine(db_uri, echo=config["default"].PRINT_SQL,pool_size = 100, pool_recycle=3600)
    event.listen(engine, 'checkout', checkout_listener)
    return sessionmaker(bind=engine)


Session = session_factory()

@contextmanager
def action_session():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


@contextmanager
def query_session():
    session = Session()
    try:
        yield session
    except Exception as e:
        raise e
    finally:
        session.close()