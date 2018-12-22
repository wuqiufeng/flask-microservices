# -*- coding: utf-8 -*-
# @Time    : 18-12-22 下午12:46
# @Author  : Fuhz
# @Email   : 
# @File    : push_msg.py
# ---------------------
from sqlalchemy import Text, String, Integer, Column

from app.models.base import Base


class JpushMsg(Base):
    id = Column(Integer, primary_key=True)
    account = Column(String(64), nullable=False)
    alert = Column(String(128))
    contents = Column(Text, nullable=False)
