# -*- coding: utf-8 -*-
# @Time    : 18-12-18 下午3:57
# @Author  : Fuhz
# @Email   :
# @File    : config.py
# ---------------------
import os


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ace123@111.231.87.209:3306/test"
    # Token生成串
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or "38ea77df71614caeb001b3b1c1c608d7"
    # Token过期时间
    JWT_EXP_TIME = 1 * 60 * 60 * 72
    # 极光
    JPUSH_API_KEY = "977813ed9ea938e2e56c9608"
    JPUSH_MASTER_SECRET = "c23492ffbf7e3348db3be6c1"



class IntConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ace123@111.231.87.209:3306/test"


class DevConfig(IntConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ace123@111.231.87.209:3306/test"


config = {
    "development": DevConfig,
    "default": Config
}